# Linux EKF experiments

**Stage one:**

Single application, chain length equals one. (Basically what you have right now.) We can increase the number of clients to push the utilization higher. 

Detailed settings:

1. Flow number: needs to be adjusted
2. Rate: a static value should be sufficient, but we need it to calculate system utilization.
3. The result of the parameters are less important and can be set as a static value.

Results:

1. Tail and average latency of all clients.
2. Standard deviation of latencies. 
3. Throughput.

**Stage two:**

Single application, chain length greater than one. We need to set the Linux ip table to make it act as a firewall which means the chain structure would be like firewall -> ekf -> firewall. I will provide more information about Linux ip table and other nfs we need for longer chains.

Settings and results can remain unchanged.

Expected results:

1. Longer chain means more overhead, so I expect a lower throughput and higher average (and tail) latency.
2. The bottleneck will coming earlier than stage one which means the latency will sharply go up earlier than stage one.

**Stage three**

This is the final experiment we might want to have. In this experiments we will have multiple different applications such ekf, armnn and Mqtt all operating on the same server. More application means different execution times, which will in return make it harder for all applications especially that with small execution times meet their deadlines.

But for ekf tests, it should remains the same. What remains to solve is to have all three Linux compare cases been started at the same time and write scripts 

