# Discussion Note
## Assumption:
- All packets in a flow have the same deadline.
	- If a flow contain n packets P0, P1, … , Pn, with the deadline d. Then each packet  (P0, P1, … , Pn) has the same deadline d.
- All same flows arrives at different time have same relative deadline
	- p2d(p @ t0) < p2d(p @ t1) when t0 < t1. 
	- Other systems cannot have fwp chain per flow, so need multiple deadlines per fwp chain. (This could be another contribution.)

## Notation:
- p2d(p) -> d
- fwp2d(fwp) -> d

## Problems to solve: 
- Prob 1: 
	- Multiple fops get packets. (?)
	- When do we recompute deadlines.
- Prob 2: 
	- If packets of multiple deadline go through a fwp chain, how to schedule.
		- If the assumption 2 stands, for the packets in the ring buffer of a specific fwp, the packet arrived earlier should have closer deadline than the packets arrived after. 
- Prob 3: 
	- How can we know the deadline of an fwp with n enqueued packet with different deadline?
		- The deadline of an fwp should equals the closet deadline of all packets within its ring buffer. If the assumption 2 stands, the deadline of the first packet in its ring buffer will have the closest deadline. (O(1)) So we do not have to go through every packets in the ring buffer. (O(n))
	- How can know an fwp has processed a packet with a specific deadline? (I will rephrase it as who will recompute the deadline of a fwp. When and how it will recompute the deadline.) It could be divided into two parts:
		1. When does fwp2d(fwp) get modified to be closer? -> When the fwp is waked up.
		2. When does fwp2d(fwp) get modified to be further? -> When the fwp is blocked.  (I am not sure. Because when an fwp is blocked, it has been removed from the run queue. Its deadline will be modified when it has been waked up.)
	- The length of the ring buffer should be bounded. Large rings will result in pessimistic deadlines. 
		-MMA applies back pressure and does not transfer into a ring of a specific size. Handle all packet in ring at priority of the deadline of the highest priority packets.

## Behavior analysis
- MCA copies packet into a fwp whose ring buffer is empty.
	- MCA should send a notification to the scheduler of that core and the scheduler will change the state of the correspond fwp, recompute its deadline and put it into the run queue.
- If an fwp finish processing its packets (its ring buffer is empty), it will call schedule to block it and remove it from the run queue. Charge its deadline to be further. (Again, I am not sure.)
- If the scheduler decides to preempt current running fwp, it should recompute the deadline of current running fwp and add it back to run queue.
