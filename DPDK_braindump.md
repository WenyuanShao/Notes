# What I know about dpdk

### How to compile and run composite+dpdk
1. Add the following environmental variable in ~/.bashrc
```
export COS_HOME="~/composite-dir"
export EXT_CFLAGS="-nostdlib -nostdinc -fno-pic -fno-pie -D_GLOBAL_OFFSET_TABLE -D_GNU_SOURCE -mno-sse -mno-sse2 -mno-mmx -mno-3dnow -mno-avx"

```
Then you can compile composite using `./cos init` and `./cos build` to compile. Lib dpdk depends on musl-libc, so it is possible that you need to run `./cos init` twice.

2. We force a link between dpdk and device [here](https://github.com/gwsystems/dpdk/blob/b524a0e4c80161a606332bb339a8838589f0450f/lib/librte_eal/common/eal_common_pci.c#L313-L341).


### Current state of the code and problem unsolved
1. Currently, I have inserted code in llbooter to do initiate and test. 

2. I've tried to using -netdev to configure qemu using a e1000 network card and connect to the tap network create in the host machine. 
Here's some reference might be helpful: [1](https://brezular.com/2011/06/19/bridging-qemu-image-to-the-real-network-using-tap-interface/); [2](https://wiki.qemu.org/Documentation/Networking); [3](https://gist.github.com/extremecoders-re/e8fd8a67a515fee0c873dcafc81d811c)

3. I've also able to dump packets qemu can see. Use wireshark to open the dump.data

4. Currently, no packets can be received and sent by composite with dpdk. And the dump.data result is also empty.

### Compoiste APIs used in DPDK and dependencies of DPDK
1. DPDK use some composite provided APIs check [this](https://github.com/WenyuanShao/eos/blob/fwp/src/components/implementation/no_interface/fwp_manager/ninf.c).

2. One possible problem could be PCI has been mapped to wrong physical address. The mapping API is in ninf.c

3. DPDK depend on component and posix library.

### Some other stuff about DPDK
1. The debug print can be used in DPDK is `RTE_LOG`, you can use it as `RTE_LOG(ERR, EAL "...", ...);` 

2. You can set the level of LOG [here](https://github.com/gwsystems/dpdk/blob/e348f018f52409b927866c940b47e29993801b20/lib/librte_eal/linuxapp/eal/eal.c#L792). I recommend using `RTE_LOG_DEBUG` paired with `RTE_LOG(ERR, EAL, ...)`

3. Some directories which are important. dpdk/lib/eal/common, dpdk/lib/eal/linux, dpdk/driver/net/e1000/em_rxtx.c, etc.
