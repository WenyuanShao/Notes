# outline 

##Introduction

+ Contribution
  + system infrastructure for deadline aware computation
  + scalable EDF scheduling algorithm
  + Schedule NFs instead of packets

## related work

## system design

+ System overview
  + The infrastructures for deadline aware scheduling
+ Deadline aware scheduling
  + Translate deadline of packets to deadline of NFs
  + Every Nfs in the chain share the same deadline instead of having different deadlines
+ Bounded tardiness 
  + The notion of offset (delta) and how it will affect the system's schedulability. 

## evaluation

+ Evaluation setup.
  + Two server, 48 cores each.
  + Workload.

+ Micro-benchmark
  + Ultilization benchmark (by having different spin time and rate)
    + two kinds of lines for different spin time;
    + 3 lines each for EOS configure using edf, Linux, EOS configure using fprr;
    + X-axis: packet rate
    + Y-axis: tail latency
  + edf algorithm microbenchmark
    + X-axis: number of threads
    + Y-axis: scheduling latency (time taken for making a scheduling decision)
  + Offset (delta might be better) benchmark 
    + X-axis: offset changing from 0 to packet rate
    + Y-axis: tai latency
+ Real case application
  + MQTT broker
    + Firewall-> MQTT-> firewall; multiple MQTT instances per core; one topic per broker; two clients subscribe to one client.
      + Linux compare case: use ip_table as firewall each MQTT instances running in a separate process.
    + X-axis: flow number
    + Y-axis: tail lantency
    + Three lines for EOS (edf), linux, EOS(fprr)
  + Multi-type nfs
    + Have different types of NF per core. Each type has different WCET, which will result interferences to each other.
      + Linux compare case: have memcached and armnn instance on the same core. The goal is to see the tail latency of memcached which will surely be impacted by armnn.
    + Chain length one is enough.
    + X-axis: number of armnn instances (flows) per core.  --> more armnn instance harder to schedule memcached instances. 
    + Y-axis: tail latency of memcached instance.  
    + Three lines for EOS (edf), linux, EOS (fprr)