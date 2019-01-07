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
	+ Packet rate: R
	+ Packet deadline: PD<sub>i</sub>
	+ FWP deadline: FD<sub>i</sub>
	+ System overhead (include scheduling overhead, context switch overhead, ipi overhead, etc.): S
	+ Worst case computation time: C<sub>i</sub>
	+ Worst case scheduling latency: L<sub>i</sub>

+ This system model is different from the classic EDF system model in following aspects according to Liu and James's paper:
	1. classic EDF system model schedule tasks, so we have to convert packets to FWPs using some function which takes all packets in the run queue of a FWP as input value and outputs FWP deadline: f<sub>1</sub>(P<sub>0</sub>, ... , P<sub>n</sub>) -> FD<sub>i</sub>. A possible implementation of f<sub>1</sub> could be: f<sub>1</sub>(P<sub>0</sub>, ... , P<sub>n</sub>) = p2d(P<sub>0</sub>). Because according to assumption ii, the first packet in the run queue has the earliest deadline.
	2. classic EDF system model deals with periodic tasks? (not sure)
	3. tasks are independent which means current processing packet doesn't depend on the initialization or the completion of other tasks. (X)
	4. each task must be completed before the next request comes. (not sure)

+ Schedulability analyze:
	+ We can use the Theorem 7 of Liu and James's paper which says the EDF algorithm is feasible if and only if: (C<sub>1</sub>/T<sub>1</sub>)+(C<sub>2</sub>/T<sub>2</sub>)+ ... +(C<sub>1</sub>/T<sub>1</sub>) <= 1.
	+ There is a gap between the analysis of our system and Liu and James's theorem. We need to analyze the schedulability of each packet instead of each tasks. According to f<sub>1</sub>, DP<sub>i</sub> >= DP<sub>i</sub>. In other words, since the deadline of current FWP is the earliest deadline among the deadline of all packets in its run queue, if f<sub>i</sub> is schedulable all packets in f<sub>i</sub> are schedulable.

## Evaluation
+ Infrastructure: two Dell R740 servers connected to each other through port enp59s0f0 (10G) (needs detailed information about the servers). Do we need connect more ports to create different packet flow comes from different ports. (?)

### Performance evaluation:
+ Schedualbility test:
	+ Generate different packet flows which push the utility of the system and calculate the packet flows which meet their deadline.
	+ X axis packet rate (?), Y axis percent of the packets which meet its deadline.

+ Latency and throughput test:

### Comparison cases

This is the section that is often the most difficult and will consume the majority of the space.
You really want to get down to the details of what the systems being compared are, what are the relevant aspects of their setup, and what are the structures of any tables, and the x/y axis/different lines are for each graph.
Getting to this level of detail is difficult, and requires planning and starting this outline 2 months before the deadline.
The outline file should be formatted by default with a section for "story", one for "motivation", and one for "experiments".

Create a subsection within "Experiments" for each of the classes of experiments.  
There are often at least:

- *Motivation* - why are current systems insufficient?
- *Applications* - what higher-level applications can benefit from your system?
- *Parameter studies* - what are the parameters that impact the benefit or the properties of your system?  
    For example, things like the working set, rate of arrivals, size of requests, memory allocations, etc...  
    These are often the easiest to figure out as they are very much intertwined with the technical details you've spent months working on!
- *Microbenchmarks* - these study the atomic costs of the system with the intent of giving the reader an understanding of the underlying bounds of the system and compare, where possible, against comparable operations on existing systems.

Create a subsub section within each of these for each experiment.

Please start out with the motivation (as above) asking the question, "what do existing systems lack, or what is wrong with existing systems?", and from there create experiments that fairly *demonstrate those shortcomings*.  
First and foremost, you're trying answer the question "what value does your system add", and focus on results that fairly showcase that.
Only after you establish value, do you look at experiments to characterize all aspects of the system (where it is weak, where it is strong, workload characterizations, etc...).

For each experiment, the first thing you should do is write down the question you're trying to answer with the experiment.
Literally write it down.
For example:

**Question:** What is the maximum interference on high-priority tasks that systems can experience from IPIs?

Then list the following:

- System setups - which systems are you comparing, how are they set up?
- Workloads - what is the workload on each system?
- Graph/Table details - the axis and parameters of the graphs/tables.  
    This is the hardest part, and will take a lot of thought.
    The dominant question is how to best represent the phenomenon you're studying, and how to *best answer the question* (from above).
    
Once you have a first draft of all of this, get Gabe involved!
If you have trouble putting any of this together, get Gabe involved, and talk to your peers!
You'll iterate on this document quite a bit, so don't get too attached to anything.
The story of a paper can change quite a bit as you get results, but you have to have an initial plan, and a goal.