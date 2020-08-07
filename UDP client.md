# UDP client

### Packet composition:

[This fcuntion](https://github.com/WenyuanShao/facebook-memcached-old/blob/f7d04d94721fb947735f88ef835f44a55bc9b92c/test/mcblaster/main.c#L961) will compose a memcached packet. So what we need to do are:

1. Look into the request type and remove if necessary.
2. Replace this function with what we need for ekf.
3. Remove most of the memcached result parse (start from [here](https://github.com/WenyuanShao/facebook-memcached-old/blob/f7d04d94721fb947735f88ef835f44a55bc9b92c/test/mcblaster/main.c#L1012)) after receive the reply from the server.

### Options used:

1. -t: number of thread started. Set to 1 since we've used a script to start multiple client each bind to a different ip address and port.
2. -k: number of keys, need to be removed, is used for memcached.
3. -z: key value size, need to be removed
4. -u: udp port
5. -f: client udp port
6. -r: rate limit. **we've added this parameter to limit the number of packets sent every second.**
7. -d: run for how long. 

You can find detailed usages of this client [here](https://github.com/WenyuanShao/facebook-memcached-old/blob/f7d04d94721fb947735f88ef835f44a55bc9b92c/test/mcblaster/main.c#L1290).

