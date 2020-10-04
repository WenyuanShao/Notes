# Linux single chain test.

1. Goto client machine and run `git pull` under Linux_ben

   Create a arp.sh file in home as:

   ```
   #!/bin/bash
   sudo ifconfig enp59s0f0 10.10.1.1
   sudo ifconfig enp59s0f0 netmask 255.255.255.0
   sudo arp -s 10.10.1.2 f8:f2:1e:11:42:08
   ```

   Then run arp.sh

2. Goto server machine and run `./arp.sh`

   Then run `dhclient -v` and `scp -r wenyuan@[server_ipaddr]:~/Linux_ben .` (Replace the existing one).

   Then reboot client (avoid any dhcp related affect to the result)

   Run `./arp.sh` again. 

   **TEST:** you can test whether client and server connected correctly by
   On server side: `ping 10.10.1.1`

   On client side: `ping 10.10.1.2`

   No drop or timeouts means correct.

3. On server side start server: 

   Go to micro_ben dir and start the server by `./run_server [tot_core] [core_num]` in this case `./run_server 48 6`

4. On client side: 

   Go to Linux_client/Linux_expr/ start clients by  `python bino_test.py --nb_nodes 50 --nb_hi 10`

   Use `python data_aggragate logs/` to get the parsed result and fill in this [form](https://docs.google.com/spreadsheets/d/1kYjBN4baGQhIMVxm-uOobD4_mLcDQu60JVrAX5Gh5d0/edit#gid=0). To save you time, just last 3 tests which with`nb_hi` equals 10, 20, 30 are enough.

   You can ignore the error messages starts with "RTT" when you parse the log files. 

   You can also use `python parse.py [hi_nb] [tot]` to get detailed information.

5. You may need to install numpy to be able to run the parser script. Use this command

   `sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose`

6. Remember use `htop` to get some ideas about roughly what's the utilization of the server while running the test. Is it full loaded or not. 

## real test

This is what we want in the paper.

+ Server: total core: 48, core_num: 16
+ Client: number of nodes: 600, nb_hi: 360, 240, 120 ...
+ Fill in this [form](https://docs.google.com/spreadsheets/d/1kYjBN4baGQhIMVxm-uOobD4_mLcDQu60JVrAX5Gh5d0/edit#gid=1013723605).
