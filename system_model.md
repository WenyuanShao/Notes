This paper is focusing on a multi-tenant infrastructure in which each tenant provides multiple stages of computation.
Consider for tenant T<sub>i</sub>, it provides multiple network Applications {A<sub>1</sub>, A<sub>2</sub>, ...}. 
The network application A<sub>ij</sub> consists of k stages of computation {S<sup>1</sup> <sub>ij</sub>, S<sup>2</sup> <sub>ij</sub>,... ,S<sup>k</sup> <sub>ij</sub>}.
Client c is continuously sending packets to the edge cloud requesting the application A<sub>ij</sub>.
For simplicity, in this paper, we ignore any kind of packet losses happen on the client side or during the transaction from the client to the edge cloud.
Additionally, the edge cloud should provide isolated execution for each client since multiple clients can send requests asking for the same network application.
Packet P<sub>n</sub> is the nth packet from client c requesting application A<sub>ij</sub>.

