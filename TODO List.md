# TODO List

# Flow Table:
- We do have a flow table for different flows now.
	- Current using flow mapping:
		1. a flow  to chain mapping, simple mapping using (client port - offset) to get the correspond fwp ID. (hashtable needed?)
		2. We need a more SDN like flow table:
			i.  still using client port to map to the correspond fwp.
			ii. The flow table is an array and each node is a structure contains information such as: ip address, DDL, correspond fwp ID, *offset* (the length of the DDLs which determines one packet would be allowed to copy to fwp ring buffer or not) **the size of offset needs to be determined**. 

# Notification:
- currently MCA only send a notification when the ring buffer of which the packets are copied into is empty. Using a simple cross core thread wake up (sl_xcore_wake_up (?))
	- It might still be sufficient since we do not need more information. However, using channel maybe helpful since we can pass more information along with the notification. (if MCA and scheduler store the DDL separately which means they have to calculate the DDL of the fwp separately.)
	- If using mechanism like channels, we maybe able to pass the DDL of the fwp with the original notification. 
- I still think shared memory is a better idea. Reasons are listed below:
	1. Since MCA should also be aware of the DDL of the current fwp which packets are going to be copied in. By using shared memory we only have to calculate the DDL once.
	2. If the MCA and scheduler maintain their own copies of the DDL. They need to calculate the DDL of the fwp separately. However, put more overhead to the MCA is dangerous since we still wants MCA to have a very good performance.
	3. However, still not very confident if shared memory between MCA and each scheduler would cause any risk or not.
- In which case, should the MCA decide to copy the packets to the correspond fwp.
	1. This is decided by the *offset*. If DDL<sub>curr</sub> + offset > DDL<sub>new</sub> MCA should copy the packet into the correspond fwp and if not MCA should delay the copy. 

# The DDL of the fwp:
- When to change the DDL tighter:
	- Every time MCA decided to copy a new packet into one fwp. (notification happens)
		- this would be the only time the DDL of the fwp would be modified tighter. If we assume no merge.
	- When the merge happens this might possible
- When to change the DDL looser.
	- When timer tick happens if the current processing fwp didn't finish processing all of packets in its ring buffer
	- When merge happens. (also be a notification, fwp to fwp notification)
- How to calculate the DDL of one fwp
	- The DDL of a fwp should be the smallest DDL among all of the packets in its ring buffer.
	- Using a bitmap would help to reduce the time taken to get the smallest DDL.
	- The size of the bitmap is bounded by *offset* I've described before.
	- Considering it is possible that multiple fwps share the same DDL, we also need to maintain an array list which contains all of the fwps with their correspond DDL.

# Timer Tick
- We need timer tick for sure.
	- If there is not timer tick. fwp could be able to run forever, there are risk conditions there.
- Timer tick some how bound the worst case process time of the fwp. 
	- As a result we need to weaken that affect. 
		1. use fine grained timer tick. However, using fine grained timer tick means waken the scheduler more often which will result in more overhead. **Select the timer tick size is important**
		2. Maybe use a dynamic timer tick. Change the size of the timer tick every time the scheduler is waken. Algorithm remains to be discussed. But the input value would be (DDLs of all fwps in the run queue, the size of the batches of packets in each fwp, the offset size of each fwp).
		
