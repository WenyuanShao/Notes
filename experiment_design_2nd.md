# Basic parameters

#### Utilization: 

Utilization is calculated by calculating the scheduler idle time. Utilization could be affected by many parameters such as WCET, packet rate, flow number. It is relatively hard to modify WCET and packet rate. As a result, I plan to modify the utilization by changing the number of flows needs to be processed on the same core.

#### % of deadline met (or missed):

+ % of deadline met might be better than % of the deadline missed.
+ The % of the deadline met is going to be calculated on the client side. The deadline of the same flow on the server side should be smaller than the deadline of it on the client side. According to my current experiments, DL<sub>client</sub> = 2 * DL<sub>server</sub> could be reasonable.
+ **How can we define the % of deadlines met (or missed).  (Still thinking)** If one packet in the flow missed its deadline, does this mean that any other packets came after the current packet will miss its deadline. Or in another word, will it affect future packets in the same flow  
+ **Not very easy to tell % of deadline meet will show the advantage of our system. Instead, we might want to use % lateness. (?) **

#### Latency:

+ The latency could be get from the client side.
+ Since there are many flow which have different deadline, packet rate. How can we plot them in the same graph.
+ As a result, latency make very little sense to me. Plot latency might not be a very good idea
+ But there are some other information we can get from the latency, such as we can get the % of the packets which missed its deadline by tracking the latency.

#### Throughput:

+ The throughput of the system will be only affected by the system overhead which is introduced by changing scheduling policies.
+ We can add up the throughput of every flows to get the total throughput go the system.

#### OFFSET:

Currently, we can support different OFFSET for different flows. Considering we cannot show all of the different OFFSETs, choosing a static OFFSET might be a better choice. The OFFSET will be changed among a interval of _[0, MIN(flowdeadline)]_. 

#### Bin size:

For bitmap edf, every bit in the bitmap represents a period of time which the deadline of one nf could be in. Adjusting bin size might have some influence on the performance since it will affect the reclaim the bits. The bin size should closely related to the size of a timer tick. As a result, to better understand this, I think we need to have a parameter study for bin size and even different length of the timer tick.

# experiment design

### Microbenchmark

There should be a microbenchmark for different scheduling algorithms to prove bitmap base scheduling is sufficient.

**Experiment design:**

+ This microbenchmark should be done above Linux.

+ We are going to evaluate retree, bitmap edf, bitmap fprr, three types of scheduling algorithms.

+ We will measure both insert and remove overheads in the microbenchmark.

+ For rbtree, the microbenchmark should flush cache between every insert and remove operation. e.g.

  ```
  flush_cache();
  rbtree_remove();
  flush_cache();
  rb_tree_insert();
  ```

+ The expected results are tail of the overheads and standard deviation of the results.

**Aiming graph:**

**Graph 1 (histogram):**

+ X-axis: different scheduling algorithms + thread number (10, 100, 1000). There in total will be 9 bars.

+ Y-axis: latency (cycles).
+ Each bar shows the average latency, a showed bar shows the 99% tail and a small interval inside shows the standard deviation.

### parameter study:

**Basic experiment design:**

The purpose of parameter study is to understand (or explain) the pessimisms we've added in the system and some other parameters which might have influences on system performance.

+ Use UDP echoserver.
	+ The udp echo server will SPIN for certain amount of time.
	+ We will change SPIN time to achieve simulate different system utilization.
	+ Get throughput and % of deadline missed on the client side. 
	

**expected result:**

+ When utilization is low, our system tend to have similar throughput and % of deadline missed as LINUX and fprr EOS.

+ When utilization approaching to 1, our system tend to have better throughput and % of deadline missed than fprr EOS. fprr EOS is tend to have better result of both parameters than LINUX.

+ **We hope to see some evidence which shows the bounded lateness of the system.**


**Aiming graph:**

The parameters we are going to evaluate includes: chain length, offset size, bitmap bin size (smaller than a timer tick or greater than a timer tick). 

Using utilization as x-axis maybe reasonable. However, since there are many parameters can affect utilization (eg. SPIN time, flow number, packet rate which will affect period, etc). I plan to only control the utilization by modifying the SPIN time of every nf.

We also need a Linux compare case, we use a multiprocess echoserver as a Linux compare case. For parameter study of chain length greater than 1, we have Linux echo server send packets to other processes through a pipeline. 

**Graph1: (utilization study)**

Experiment details: 

+ Every flow has a different deadline. Clients are aware of the deadlines by knowing the server port which it communicate with;
+ The chain length is 1; 50 fwp (chain)s per core; the related deadline of these 50 fwps are from 20ms to 70ms.
+ Each udp echo server will spin for a short time to simulate the overhead of an application.
+ Modify utilizations by modifying the execution time.
+ The flows have a smaller deadline tend to have a smaller execution time and smaller period and vice versa. 
+ *(Not Sure)* The utilization is balanced across flows. Which means flow with smaller relative deadline has the same utilization as flow has greater deadline. (Having both smaller sending rate and smaller execution time.) **correspond to graph details 3**

Graph details:

1. X-axis: utilization.
2. Y-axis: 99% tail latency of the client which has the smallest deadline.
3. Have 3 lines each for Linux, EOS with fprr and EOS with edf.
   + Can have multiple lines for different utilization distribution. (For example, lowest deadline flow requires a  higher utilization, or other flows having greater utilization demand)

**Graph2: (pessimism study)**

Experiment detail:

This graph is going to show how's the pessimism we've added affect the tail latencies of all clients. The parameters which will add pessimisms include: OFFSET, timer tick and bin size.

Graph details:

Use histogram. (Not sure, but I think it might be a good choice if we want to combine all three causes of pessimism in one graph)

+ X-axis: different tests (e.g. offset 100us utilization 85%, etc)

+ Y-axis: 99% tail latency

+ Detailed tests:

  | Tests                                                        |
  | ------------------------------------------------------------ |
  | Offset: 0, utilization: 90%, timer tick: 500us, bin size = timer tick |
  | Offset: 250us (half timer tick), utilization: 90%,timer tick: 500us, bin size = timer tick (I think half a timer tick offset is enough to show the downside of having a large offset) |
  | Offset: 10us (just dealing with the client batching), utilization: 90%, timer tick: 500us, bin size = timer tick |
  | Timer tick: 250us, utilization: 90%, offset: 10us (I think a very small offset is enough), bin size = timer tick |
  | Timer tick: 500us, utilization: 90%, offset: 10us, bin size = timer tick |
  | Timer tick: 750us, utilization: 90%, offset: 10us ,bin size = timer tick |
  | Timer tick: 500us, utilization: 90%, offset: 10us, bin size = 1/4*timer tick |
  | Timer tick: 500us, utilization: 90%, offset: 10us, bin size = 1/2*timer tick |
  | Timer tick: 500us, utilization: 90%, offset: 10us, bin size = 1.5*timer tick |

**Graph3: (chain length)**

Experiment details:

+ There's only one type of fwp chain.
+ The total utilization remains unchanged when adjust the chain length. (control variable)
+ Starts with evenly distributed execution times which means every chain node has the same spin time.
+ Then try head of the chain have greater execution time. (Not sure, maybe will show better results)
+ The linux compare case will have separate processes as NFs and use pipe for interprocess communication.

Graph details:

+ X-axis: chain length: 1, 2, 4, 8; per core chain number: 64, 32, 16, 8
+ Y-axis: 99% tail latency
+ Have multiple lines for Linux, EOS with fprr and EOS with edf each having different total utilization (80%, 90%)

## Real case experiments:

### MQTT application:

**Story**: Edge might be a good place running a MQTT server...

**Experiment design:**

+ compare against fprr EOS and LINUX
+ There are two flows goes into one NF chain which means there are multiple MQTT brokers connect to one MQTT publisher.
+ One subscriber publish the message to server. Server will publish the message to every subscriber which subscribe to this channel.
+ We benchmark the performance on the subscriber which sends the publication to the server.
+ The Linux compare case is multithreaded, which will have less protection.

**Aiming Graph:** 

We are going to push the utilization of the server by adding more clients. 

+ X-axis: number of client flows 
	
+ Y-axis: 99% tail latency.
	
+ Three lines for the throughput of EOS, fprr EOS and LINUX.
	
### ~~Distributed Cache (removed)~~:

**Story**: We can built a distributed data-store for location tracking of _IOT_ devices.
	
**Experiment design**

+ chain structure: firewall -> MEMCACHED -> firewall
+ Compare against EOS with different configuration and LINUX.
+ The Geologic dataset is just a pair of data which includes latitude, longitude and time which parts with the IOT device identification. 

**Aiming Graph:**

+ X-axis: number of client flows 

+ Y-axis: 99% tail latency.

+ Three lines for the throughput of EOS, fprr EOS and LINUX. 

### Edge Inference:

**Experiment design**

+ Input data can only be fit in three three packets so these three packets will be batched in the ring. Which means the deadline of these three packets equals the deadline of the last packet.

**Aiming graph:**

+ x-axis: number of client flows
+ y-axis: 99% tail latency
+ Multiple lines for edf EOS, fprr EOS and LINUX

### EKF

**Experiment design**

+ I think this application is a good place to have some chain structure, since ekf computation will not dominates the total overhead.
+ Chain structure: firewall, UDP related NF, ekf, firewall

+ Every sensor reading can fit into one packet.
+ Use udp to communicate.
+ The Linux compare case is a multiprocess udp server.

**Aiming graph:**

- x-axis: number of client flows
- y-axis: 99% tail latency
- Multiple lines for edf EOS, fprr EOS and LINUX