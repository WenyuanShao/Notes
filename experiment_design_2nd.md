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

# experiment design

### parameter study:

**experiment design:**
+ Use TCP/echoserver and let multiple flows goes into one fwp.
	+ The echo will let the NF SPIN for a while to simulate some process overhead.
	+ The SPIN time will also be used as the base of partition deadline.
	+ Length of the chain is 2 with WCET<sub>NF<sub>1</sub></sub> = 4*WCET<sub>NF<sub>2</sub></sub> .
	+ Get throughput and % of deadline missed from client side. 
	+ We will change the flow number to get different utilization of the system.
	+ If we TCP we need to have multiple flows goes into one NF chain to show the affect of _OFFSET_.
	
+ Use UDP echoserver?

**expected result:**

+ When utilization is low, our system tend to have similar throughput and % of deadline missed as LINUX and RR EOS.

+ When utilization approaching to 1, our system tend to have better throughput and % of deadline missed than RR EOS. RR EOS is tend to have better result of both parameters than LINUX.

+ Our system tend to have better throughput since _OFFSET_ will reduce content switch overhead. (When compare to RR EOS)

+ Our system tend to have less packets which missed its deadline since

	+ First, we use EDF which will have a better schedulability especially when task<sub>1</sub> has a very early overall deadline while the first subtask of it takes most of execution time.
	+ We have less system overhead and scheduling overhead than LINUX.

**Aiming graph:**

There's two graph for the parameter study. The purpose of this graph is to show how the _utilization_ and _OFFSET_ affect the throughput and % of deadline missing.

Using utilization as x-axis maybe reasonable. However, since there are many parameters can affect utilization (eg. SPIN time, flow number, packet rate which will affect period, etc). I plan to only control the utilization by changing the number of flows.

**Graph1:**

+ X-axis: **flow number**

+ Y-axis-left: throughput. 

+ Y-axis-right: % of deadline met.

+ There are six lines each for RR EOS, LINUX and EOS with _OFFSET_ equals _0_. Three of them are for throughput and the others are for deadline meet (or miss) rate. I prefer using the percent of deadline meet.

**Graph2:**

+ X-axis: _OFFSET_ from _0_ to _MIN(flowdeadline)_
+ Y-axis-left: throughput.
+ Y-axis-right: % of deadline met.
+ We can have 2 lines for the throughput and 2 for deadline met. These two lines represent different utilization one for utilization smaller than 1and the other one is greater than 1.

**Graph3**

+ X-axis: chain length
+ Y-axis-left: throughput.
+ Y-axis-right: total lateness
+ We need another experiment for different length of chain. We can have three lines each for EOS, RR EOS, LINUX

**Graph4 (maybe?)**

This is a more basic performance experiment. More like a microbenchmark

+ X-axis: thread number
+ Y-axis: scheduling latency / scheduling overhead

## Real case experiments:

### MQTT application:

**Story**: Edge might be a good place running a MQTT server.

**Experiment design:**

+ chain structure: firewall -> MQTT ->firewall

+ On LINUX we have click objects and MQTT on different processes and connect them follow the same structure as EOS. 

+ compare against RR EOS and LINUX

+ There are multiple flows goes into one NF chain which means there are multiple MQTT brokers connect to one MQTT publisher.

**Aiming Graph:** 

Instead of using utilization as x-axis, using number of flows (clients / MQTT brokers) might be a better idea. Since, utilization could be affected by multiple parameters. For example, WCET, flow number, packet rate (period). What we can control in this experiment is flow number, utilization is the result of changing the number of flows.

+ X-axis: number of flows. 
	
+ Y-axis-left :throughput.
	
+ Y-axis-right: percent of the tasks which meet its deadline.
	
+ Three lines for the throughput of EOS, RR EOS and LINUX. The other three are for the % of deadline met.
	
### Distributed Cache:

**Story**: We can built a distributed data-store for location tracking of _IOT_ devices.
	
**Experiment design**

+ chain structure: firewall -> MEMCACHED -> firewall
+ Compare against EOS with different configuration and LINUX.
+ The Geologic dataset is just a pair of data which includes latitude, longitude and time which parts with the IOT device identification. 

**Aiming Graph:**

+ X-axis: flow number.

+ Y-axis-left: throughput

+ Y-axis-right: % of the tasks which meets its deadline

+ Three lines for the throughput of EOS, RR EOS and LINUX. The other three are for the % of deadline met.

### Edge Inference:

**Story:** It would be very reasonable to put some inference on Edge servers. Moreover, _firewall -> inference -> firewall_ is a very reasonable chain structure.

**Experiment design**

+ chain structure: _UDP related NF, firewall, inference, firewall_
+ Input data can only be fit in three three packets so these three packets will be batched in the ring. 

**Aiming graph:**	

+ x-axis: flow number.
	
+ y-axis: % of the flows meet its deadline.
	
+ Multiple lines for EOS, RR EOS and LINUX