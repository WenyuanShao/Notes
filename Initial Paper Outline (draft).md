# Initial Paper Outline (draft)

## Motivation

### Problems with the current systems
+ Currently, edge computing requires a very high throughput as well as an optimal latency. However, most of the existing Edges OSes focus on improving the throughput while they pay less attention to the latency. Considering that one of the main reasons of using edge is to reduce the cost of sending packets across routes to data center or clouds. Optimizing the end to end latency of each packet is reasonable and necessary.
+ The other limit of current OSes is that they can only schedule tasks (threads). However, edge computing requires a more fine grained scheduling policy to deal with each packets. It could be another possible motivation of this paper.

### Experiments to show the deficiency
+ To show the limit of the end to end latency and schedulability of existing OSes, we could generate several packet flows which is latency sensitive which means they have a relatively earlier deadline. (We should have more evidence to prove the limitation of current OSes.)

## Story

As the development of Internet of Thing IoT, there is a growing demand of low latency packet processing. The emerge of Edge Computing makes it possible to meet this demand by providing an additional layer between IoT devices and mega cloud. Edge server is closer to IoT devices which will reduce the cost of sending packets across routes to data center or mega clouds and processing these packets in near real-time. 

Although many works has been done on edge computing. However, there are still some problems remain to be solved: 

+ Since edge server has to process a large number of packets including some latency sensitive packets. It is a big challenge to meet the deadline of some **important tasks** while still maintain a high throughput.
+ Current OSes can only schedule tasks (or threads). However, edgeOS needs a more fine grained scheduling policy which can schedule packets instead of tasks (or threads).

### Scheduling policy 
+ Two assumptions has been made:
	1. All packets in a flow have the same deadline.
		+ If a flow contain n packets P<sub>0</sub>, P<sub>1</sub>, ... , P<sub>n</sub>, with the deadline d. Then each packet (P<sub>0</sub>, P<sub>1</sub>, ... , P<sub>n</sub>) has the same deadline d.
	2. All same flows arrives at different time have same relative deadline
		+ p2d(p @ t<sub>0</sub>) < p2d(p @ t1) when t0 < t1. 
		+ Other systems cannot have fwp chain per flow, so need multiple deadlines per fwp chain. (This could be another contribution.)

+ System model:
	+ Packet rate: R<sub>i</sub>
	+ Packet deadline: PD<sub>i</sub>
	+ FWP deadline: FD<sub>i</sub>
	+ System overhead (include scheduling overhead, context switch overhead, ipi overhead, etc.): S
	+ Worst case computation time: C<sub>i</sub>
	+ Worst case scheduling latency: L<sub>i</sub>
	+ Period 

+ This system model is different from the classic EDF system model in following aspects according to Liu and James's paper:
	1. classic EDF system model schedule tasks, so we have to convert packets to FWPs using some function which takes all packets in the run queue of a FWP as input value and outputs FWP deadline: f<sub>1</sub>(P<sub>0</sub>, ... , P<sub>n</sub>) -> FD<sub>i</sub>. A possible implementation of f<sub>1</sub> could be: f<sub>1</sub>(P<sub>0</sub>, ... , P<sub>n</sub>) = p2d(P<sub>0</sub>). Because according to assumption ii, the first packet in the run queue has the earliest deadline.
	2. classic EDF system model deals with periodic tasks? (if 3 stands, deadline is the period)
	3. tasks are independent which means current processing packet doesn't depend on the initialization or the completion of other tasks. (X)
	4. each task must be completed before the next request comes. (not sure we should have this assumption])

+ Schedulability analyze:
	+ We can use the Theorem 7 of Liu and James's paper which says the EDF algorithm is feasible if and only if: (C<sub>1</sub>/T<sub>1</sub>)+(C<sub>2</sub>/T<sub>2</sub>)+ ... +(C<sub>1</sub>/T<sub>1</sub>) <= 1. However, there are several gaps need to be considered.
		+ In our system model, the FWPs don't happen periodically. f<sub>2</sub>(R<sub>i</sub>, PD<sub>i</sub>)->T<sub>i</sub>	
		+ There are not guarantee that each FWP must be completed before the next request of it comes (which is our system is the packet or cluster of packets aren't done processing when the next packet or cluster of packet comes). (?) 
		+ The last gap is that we need to analyze the schedulability of each packet instead of each tasks. According to f<sub>1</sub>, DP<sub>i</sub> >= DP<sub>i</sub>. In other words, since the deadline of current FWP is the earliest deadline among the deadline of all packets in its run queue, if f<sub>i</sub> is schedulable all packets in f<sub>i</sub> are schedulable.
	+ Considering the gaps mentioned before, we can modify the Theorem a bit: 

## Evaluation
+ Infrastructure: two Dell R740 servers connected to each other through port enp59s0f0 (10G) (needs detailed information about the servers). Do we need connect more ports to create different packet flow comes from different ports. (?)

### Performance evaluation: (lack application...)
+ Schedualbility test: 
	+ We need this test to show our system actually have better schedulability than existing systems.
	+ Application: memcached, etc...
	+ Systems setup: Linux, original version of EdgeOS, ... (needs to come up more?)
	+ Workloads: generate different packet flows (have different start and destination ports) with different packet rate, deadline and WCET.
	+ X axis is utility, Y axis is the percent of the packets which meet its deadline.

+ Latency test: 
	+ This test is going to show our system actually have better schedulability than existing systems.
	+ Application: memcached, etc...
	+ Systems setup: Linux, original version of EdgeOS, ... (needs to come up more?)
	+ Workloads: generate different packet flows (have different start and destination ports) with different packet rate, deadline and WCET.
	+ X axis is utility (instances), Y axis is average latency.

+ throughput test:
	+ It will be more convincing if we can prove that our system will have a better latency while maintaining relatively high throughput.
	+ Application: memcached, etc...
	+ Systems setup: Linux, original version of EdgeOS, ... (needs to come up more?)
	+ Workloads: generate different packet flows (have different start and destination ports) with different packet rate, deadline and WCET.
	+ X axis is utility (instances), Y axis is throughput.

+ Response time CDF graph:
	+ This graph will show the cumulative probability of response time of existing systems. (I think we still needs this graph since we want to optimize the end to end latency)
	+ Application: memcached, etc...
	+ Systems setup: Linux, original version of EdgeOS, ... (needs to come up more?)
	+ Workloads: generate different packet flows (have different start and destination ports) with different packet rate, deadline and WCET.
	+ X axis is utility (response time), Y axis is cumulative probability.