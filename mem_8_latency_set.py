import numpy as np
import matplotlib.pyplot as plt

#Data
rate = [25,50,75,100,125,150,175,200,225,250]
#cos = [0.156,0.154,0.127,0.153,0.159,0.725,36.042,38.989,38.842,38.909,38.881,38.823,39.057]
#cos = [0.156,0.154,0.127,0.153,0.159,0.725,36.042,np.inf,np.inf,np.inf,np.inf,np.inf,np.inf]
rate_cos = [25,50,75,100,110,115,116,120,125,150]
cos = [0.156,0.154,0.127,0.153,0.159,0.725,36.042,41,41,41]
rate_janus = [25,50,75,100,125,150,151,152,153,154,155,160]
Janus = [0.154,0.144,0.121,0.100,0.123,0.635,27.707,28.429,28.452,41,41,41]
rate_separate = [25,50,53,55,60,75,100,125,150]
separate = [0.374,0.384,0.707,41,41,41,41,41,41]
#shared = [0.374,1.207,38.291,108.806,90.93,77.098,67.153,60.791,55.171,50.229]
#single = [0.31,1.034,1.02,0.993,2.882,72.558,64.047,56.345,50.822,46.952]
rate_shared = [25,30,31,33,35,40,50,75,100,125,150]
shared = [0.31,1.078,2.329,17.128,41,41,41,41,41,41,41]

#finite_cos = np.array(cos)
#finite_cos[np.isinf(finite_cos)] = np.nanmax(finite_cos[np.isfinite(finite_cos)])
#print(finite_cos)

fig, ax = plt.subplots(figsize=(6, 4))

# Use hatch patterns for each bar group
#ax.plot(rate_shared, shared, linestyle='-', label='Shared', linewidth=2)
#ax.plot(rate_single, single, linestyle='--', label='Separate', linewidth=2)
#ax.plot(rate_janus, Janus, linestyle=':', label='Janus', linewidth=2)
#ax.plot(rate_cos, cos, linestyle='-.', label='Composite', linewidth=2)

ax.plot(rate_shared, shared, marker="D", linestyle = '-.',label='Linux Shared Memcached', linewidth=2)
ax.plot(rate_separate, separate, marker="^", linestyle = '--', label='Linux Separate Memcached', linewidth=2)
ax.plot(rate_janus, Janus, marker="s", linestyle= '-', label='Janus', linewidth=2)
ax.plot(rate_cos, cos, marker='o', linestyle=':',label='Composite', linewidth=2)

# Title & Subtitle
ax.set_ylabel('99%tile Latency (ms)', fontsize=14)
ax.set_xlabel('Client sending rate (1K packets per client per second)', fontsize=14)

ax.set_xticks([50,100,150])
#ax.set_xticklabels([50,100,150,200,250], fontsize=12)
plt.xticks(fontsize=12)

plt.ylim(0,4)
ax.set_yticks(np.linspace(0, 4, num=5))
plt.yticks(fontsize=12)
ax.grid(axis='y', linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

# Create legend & Show graphic
plt.tight_layout()
plt.subplots_adjust(top=0.84)
ax.legend(loc='upper center',fontsize=11,frameon=True,framealpha=0,ncol=2,bbox_to_anchor=(0.5, 1.2))
#ax.legend(loc='upper center',fontsize=11,ncol=4,bbox_to_anchor=(0.5, 1.15))
plt.savefig('mem_8_latency_set.pdf',bbox_inches='tight')
#plt.show()
