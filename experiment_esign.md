#experiment design

## Parameter studies: (include hacks， trade off...)
	+ We can use dummy NFs in parameter study tests. (NFs with just while loops which makes the NF spin for a while)
	+ We can allocate a chain of n NFs which are forked from the same template, like [dummy NF]1 -> [dummy NF]2 -> [dummy NF]3.
	+ We can adjust the spin time of each NF according to the index of the NF.
	+ Fwp manager track the index of each NF, each NF can make a sinv call to fwp manger to get the index. (use the hypercall which already exists)

	+ Possible comparison cases:
		1. EOS compares against EOS with different configuration.
			+ Schedule with end to end deadline          |     Scheduler with split deadline (split according to WCET of each NF)
				- split deadline is based on WCET of each NF (how long the NF will be spinning). 


			+ EOS with offset 0                          ->    EOS with offset n
			+ EOS using heap (or red black tree)         |     EOS using n level bitmap

		2. EOS compares against LINUX (may not be necessary for parameter study)

	+ How to benchmark it? 
		+ Use a TCP echoserver benchmark or memcached benchmark. Since packet needs to be passed through some protocols using a TCP or UDP benchmark should be reasonable.

	+ Aiming graphs:
		1. One comparison graph: which compares EOS scheduling with end to end deadline against using split deadline. 
			+ x-axis: different task set; (different in the WCET of each task for example WCET of NF1 > WCET of NF2 vs WCET of NF1 > WCET of NF2) 
			+ y-axis: latency and throughput.
		2. One parameter study graph:
			a. "offset" study graph: 
				+ x-axis: different offset value;
				+ y-axis: latency and throughput.


## Real case experiments: (could be one or multiple types of NFs, length of the chain is greater 1)
	+ Click related applications, for example, fire wall, bridge, etc.
	+ Applications EOS already have, TLS, ARMNN, memcached, echoserver.
	+ Other applications (quadcopter)? 

	+ Comparison cases:
		1。 compare against EOS with different configuration
		2. compare against LINUX configured using EDF

	+ Aiming graphs:
		1. Comparison graph: which compares EOS against EOS with other configuration and LINUX:
			+ x-axis: clients number;
			+ y-axis: latency and throughput.

