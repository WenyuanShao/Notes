# Experiment setup

### Overview

For this experiment, we need to have a client and a server which are directly connected. The server needs to be booted into Composite. The client side needs to accomplish two jobs: 1. sending requests and benchmark the performance, 2. use minicom to get the serial output of server.

We use iDrac which is a separate power control firmware of Dell's server to reboot the server or boot it into Composite. iDrac has a different IP address and it has a web interface, you can access it using the IP address. 

### Detailed server information

+ Client info:
  + IP address: 161.253.78.154
  + iDrac address: 161.253.78.152
  + iDrac user name: root 
  + iDrac password: F99RNPW4KRNX
+ Server info:
  + IP address: 161.253.78.153
  + iDrac address: 161.253.78.151
  + iDrac user name: root 
  + iDrac password: HWHEPVAWMYFF
+ Client & server ssh:
  + Username: wenyuan
  + Password: wenyuan

### Reboot steps

1. Login iDrac
2. Ssh into client and open minicom use command "sudo minicom"
3. Open virtual console (needs to allow popup window in browser setup)
4. In the menu there's a "connect virtual device", click on it and upload Composite.iso to virtual CD.
5. In boot menu, choose warm reboot. (Usually it will take about 5 minutes)
6. You should see output on both virtual console (VGA output) and minicom (serial output)