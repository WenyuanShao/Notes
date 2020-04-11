Assume that we have a IPC from component A->B.

# probabilistic security
+ Looked up for instructions related to bind some instruction together but found nothing useful.
+ No good solution yet.

# shared queue
+ a shared memory between kernel and user-level is necessary for the synchronization between kernel and user-level.

+ It is a per thread per component data structure:
	{
		int           operation;
		unsigned long ip;
		unsigned long sp;
		capid_t       cap;
	}
	If current sinv is returned, set operation to 0. Otherwise, on the caller side set operation to 1 and 2 on the callee side.
	
+ Multiple entries might needed for nested IPCs.

+ Kernel will check the in-flight user-level IPCs by look into the syn-structure of both caller and callee. The possible cases are as bellow:
	
	|Possible condition|resolve|
	
	|:------:|:------:|
	
	|Caller/callee writes messes into shared memory.|Illegal, kernel will detect the error and which component is faulting|
	
	|Caller starts the IPC while callee didn't receive.|legal, push into invstk|
	
	|Caller writes info in shared memory and get preempted before calling *wrpkru*|kernel will push it into invstk and deal with it next time calls into kernel.|
	
	|Callee received IPC while no records on caller side| Illegal, callee could fake a IPC record, caller                                                                                  could delete a IPC record.|
	
	|Caller starts an IPC but callee writes mess into shared memory|Illegal, kernel will detect the error and which component is faulting|
	
	|Caller and callee both have legal records|kernel needs to verify if this IPC is legal and current thread is in a in-flight IPC|
	
	|Caller and callee both have empty shared queue|there is no in-flight IPC, kernel should verify previous completed IPCs which distributed stored elsewhere.|

# call gate design
+ The correctness of the IPC is ensured by linker and loader.
+ will call the function to add entries into the syn-queue before IPC and set the complete in the entry after return.
+ If the call gate is compromised (by correctly guess the security_token), it will have the ability to call into the other component through the call gate. However, since we've defined limited entrance (stubs), it will broke the isolation but i doubt how severe the consequence could be.

# problems:
+ ~~If there's no pgtbl switch in user-level IPC using MPK, does this mean it maps part of callee into caller's address space?~~

   **the whole address space of callee needs to be mapped into caller's address space.**

+ ~~instead of using the call gate system provided, one compromised component can using its own **call gate** and try to gain read and write privilege of other components.~~ 

  **solved by having a binary inspection.**

+ ~~16 protection domains seems very limited to me. What if we have much more components and needs to IPC between each other.~~

  **if caller and callee aren't the  components in these 16 protection domains, it will still follow the normal IPC path.**

  **Some intelligent policies are need to determine which components are more frequently used and can be put into these protection domains.**
