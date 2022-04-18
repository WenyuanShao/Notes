This paper is focusing on a multi-tenant infrastructure in which each tenant provides multiple stages of computation.
Consider for tenant $T_i$, it provides multiple network Applications {A_1, A_2, ...}. 
The network application $A_{ij}$ consists of k stages of computation {$S^1_{ij}$, $S^2_{ij}$,... ,$S^k_{ij}$}.
Client c is continuously sending packets to the edge cloud requesting the application $A_{ij}$.
For simplicity, in this paper, we ignore any kind of packet losses happen on the client side or during the transaction from the client to the edge cloud.
Additionally, the edge cloud should provide isolated execution for each client since multiple clients can send requests asking for the same network application.
Packet $P_n$ is the nth packet from client c requesting application $A_{ij}$.

