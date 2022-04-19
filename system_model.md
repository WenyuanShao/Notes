This paper is focusing on a multi-tenant infrastructure in which each tenant provides multiple stages of computation.
Consider for tenant T<sub>i</sub>, it provides multiple network Applications {A<sub>i1</sub>, A<sub>i2</sub>, ...}. 
The network application A<sub>ij</sub> consists of k stages of computation {S<sup>1</sup> <sub>ij</sub>, S<sup>2</sup> <sub>ij</sub>,... ,S<sup>k</sup> <sub>ij</sub>}.
Client c is continuously sending packets to the edge cloud requesting the application A<sub>ij</sub>.
For simplicity, in this paper, we ignore any kind of packet losses happens on the client side or during the transaction from the client to the edge cloud.
Additionally, the edge cloud should provide isolated execution for different clients because multiple clients can send requests asking for the same network application.

Packet P<sub>n</sub> is the nth packet from client c requesting application A<sub>ij</sub>.
It has a relative deadline D<sub>ij</sub>.
P<sub>n</sub> reaches the edge cloud at R<sub>n</sub><sup>0</sup>, P<sub>n</sub> will be copied to S<sup>1</sup> <sub>ij</sub> at T<sub>n</sub><sup>0</sup>. 
Besides, Packet P<sub>n</sub> will reach the computation stage S<sup>t</sup> <sub>ij</sub> at R<sub>n</sub><sup>t</sup> and generates a message for the following computation stage at T<sub>n</sub> <sup>t</sup>.
We also denote the beginning and end of the execution of stage S<sup>t</sup> <sub>ij</sub> for the packet P<sub>n</sub> as s<sub>n</sub><sup>t</sup> and e<sub>n</sub> <sup>t</sup>.
Note that e<sub>n</sub> <sup>t</sup> - s<sub>n</sub> <sup>t</sup> is the actual execution time of S<sup>t</sup> <sub>ij</sub>.
This paper makes no assumptions on the worst case execution time of any computations.
There will be delays between P<sub>n</sub> arrives and execution starts (Δ<sub>head</sub>) as well as execution ends and message sent out (Δ<sub>tail</sub>).
Δ<sub>head</sub> contains batching delay Δ<sub>batch</sub> and scheduling delay Δ<sub>sched</sub>.
Δ<sub>s</sub> is the transaction delay.
Δ<sub>copy</sub> = R<sub>n</sub><sup>t</sup> - T<sub>n</sub><sup>t-1</sup> is used to denote the packet copy delay.
We are talking about constant size of packets (<=1024 Bytes), thus Δ<sub>copy</sub> is constant and can be ignored.
We can denote the end-to-end latency of packet P<sub>n</sub> as L<sub>n</sub>, L<sub>n</sub> equals T<sub>n</sub> <sup>k</sup> - R<sub>n</sub> <sup>0</sup>.
The Packet P<sub>n</sub> meets its deadline means L<sub>n</sub> <= D<sub>n</sub>.

The goal of this paper is to schedule tasks based on its end-to-end deadline and practically make more deadlines even when the system is highly utilized.
To provide predictable scheduling on dynamic workloads, we have to make the following assumptions on the workload:

1. **Tenant T<sub>i</sub> provides the relative deadline D<sub>ij</sub>** 
It isn’t practical for a tenant to understand their computation’s execution time on the edge given the hardware’s inaccessi-bility and potentially heterogeneous edge hardware.
Given this, we assume no knowledge about average or worst-case computation times.

2. **Controlled utilization**
research focuses on predictable scheduling, and not on admission control. 
Load balancers and/or workload shapers often sit before computation nodes to control utilization and provide such functionality.



