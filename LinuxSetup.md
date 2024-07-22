## This is a note of the Linux memcached server setup.

+ `https://github.com/WenyuanShao/janus_non_block_bench_client/blob/main/multi_server.py` This allows starting multiple memcached servers.
However, in this experiment I am using one memcached server running on 16 cores.
+ Stop irqbalance `sudo systemctl stop irqbalance` and check irqbalance status `sudo systemctl status irqbalance`.
+ Manually set smp_affinity 
```
#!/bin/bash
# Set the CPU mask to use all 16 cores (0-15)
CPU_MASK="0000ffff"  # 16 cores

# Loop through IRQ numbers 128 to 143
for IRQ in $(seq 128 143); do
    echo "Setting smp_affinity for IRQ $IRQ to $CPU_MASK"
    echo $CPU_MASK > /proc/irq/$IRQ/smp_affinity || echo "Failed to set smp_affinity for IRQ $IRQ"
done

echo "smp_affinity settings applied for IRQs 128 to 143."
```
+ Manually set RPS
```
#!/bin/bash

# Network interface
INTERFACE="eth0"

# Set the CPU mask to use all 16 cores (0-15)
CPU_MASK="ffff"  # 16 cores

# Find the number of receive queues for the interface
NUM_QUEUES=$(ls -d /sys/class/net/$INTERFACE/queues/rx-* | wc -l)

# Set RPS for each receive queue
for QUEUE in $(seq 0 $(($NUM_QUEUES - 1))); do
    echo "Setting RPS for $INTERFACE queue rx-$QUEUE to $CPU_MASK"
    echo $CPU_MASK > /sys/class/net/$INTERFACE/queues/rx-$QUEUE/rps_cpus || echo "Failed to set RPS for $INTERFACE queue rx-$QUEUE"
done

# Set the number of flow entries
echo 32768 > /proc/sys/net/core/rps_sock_flow_entries

echo "RPS settings applied for $INTERFACE."
```
+ Testing using `htop` to see if all cores are fully utilized.
