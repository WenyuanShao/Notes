# experiment design

## Parameter studies:
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
	1. Comparison graph: (compares EOS configured using heap and bitmap)
		+ x-axis: utilization of the whole system
		+ y-axis: percent of the flows which meet its deadline and throughput
		+ Two lines of percent of the tasks meet its deadline for different scheduling algorithm. And two lines for throughput.
	2. Parameter study graph:
		+ "offset" study graph: 
			+ x-axis: different offset value;
			+ y-axis: percant of the flows which meet its deadline.
			+ Multiple lines for different utilization of the system (low (0.1), around (0.5), high	(> 0.8))


## Real case experiments:
+ Click related applications, for example, fire wall, bridge, etc.
+ Applications EOS already have, TLS, ARMNN, memcached, echoserver.

+ MQTT application:
	+ chain structure: firewall -> MQTT ->firewall
	+ compare against EOS with different configuration and LINUX
	+ Aiming Graph:
		+ x-axis: utilization of the whole system
		+ y-axis: percent of the tasks which meet its deadline
		+ Multiple lines for different scheduling policy and system configuration.

+ Distributed Cache:
	+ chain structure: firewall -> MEMCACHED -> firewall
	+ Compare against EOS with different configuration and LINUX.
	+ Aiming Graph:
		+ x-axis: utilization of the whole system
		+ y-axis: percent of the tasks which meets its deadline
		+ Multiple lines for different comparison cases

+ Long NF chain:
	+ chain structure: a longer chain (5-15).
	+ No merges considered.
	+ Aiming graph:
		+ x-axis: Lenght of the chain.
		+ y-axis: percent of the flows meet its deadline.
		+ Multiple lines for different overall utilization.

