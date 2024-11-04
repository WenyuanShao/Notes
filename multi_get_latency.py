import numpy as np
import matplotlib.pyplot as plt

#Data
multi_get = [1,2,3,4,5]
cos = [0.127,0.153,99,99,99]
Janus = [0.121,0.139,0.159,0.192,60.004]
shared = [0.248,0.642,3.237,99,99]
single = [0.630,99,99,99,99]


fig, ax = plt.subplots(figsize=(6, 4))

# Use hatch patterns for each bar group
#ax.plot(rate_shared, shared, linestyle='-', label='Shared', linewidth=2)
#ax.plot(rate_single, single, linestyle='--', label='Separate', linewidth=2)
#ax.plot(rate_janus, Janus, linestyle=':', label='Janus', linewidth=2)
#ax.plot(rate_cos, cos, linestyle='-.', label='Composite', linewidth=2)

ax.plot(multi_get, shared, marker="D", linestyle = '-.',label='Linux Shared Memcached-15K', linewidth=2)
ax.plot(multi_get, single, marker="^", linestyle = '--', label='Linux Separate Memcached-15K', linewidth=2)
ax.plot(multi_get, Janus, marker="s", linestyle= '-', label='Janus-75K', linewidth=2)
ax.plot(multi_get, cos, marker='o', linestyle=':',label='Composite-75K', linewidth=2)

# Title & Subtitle
ax.set_ylabel('99%tile Latency (ms)', fontsize=14)
ax.set_xlabel('Memcached Operations Per Client Request', fontsize=14)

#ax.set_xticklabels([50,100,150,200,250], fontsize=12)
plt.xticks(fontsize=12)
ax.set_xticks(np.linspace(1, 5, num=5))

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
plt.savefig('multi_get_latency.pdf',bbox_inches='tight')
#plt.show()
