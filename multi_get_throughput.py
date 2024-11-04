import numpy as np
import matplotlib.pyplot as plt

#Data
multiget = [1,2,3,4,5]
shared_memcached = [10.49002,9.71136,6.81331,5.20769,4.31170]
separate_memcached = [10.49079,10.49031,10.48235,9.03532,6.87235]
cos = [51.82925,52.45708,50.30719,42.45900,36.82818]
Janus = [51.82668,51.37771,52.45734,52.45498,52.06318]

fig, ax = plt.subplots(figsize=(6, 4))

# Use hatch patterns for each bar group
ax.plot(multiget, shared_memcached, marker="D", linestyle='-.', label='Linux Shared Memcached-15K', linewidth=2)
ax.plot(multiget, separate_memcached, marker="^", linestyle='--', label='Linux Separate Memcached-15K', linewidth=2)
ax.plot(multiget, Janus, marker="s", label='Janus-75K', linestyle='-', linewidth=2)
ax.plot(multiget, cos, marker='o', label='Composite-75K', linestyle=':', linewidth=2)

# Title & Subtitle
ax.set_ylabel('Goodput (100K requests)', fontsize=14)
ax.set_xlabel('Memcached Operations Per Client Request', fontsize=14)

#ax.set_xticklabels([50, 100, 150, 200, 250], fontsize=12)
plt.xticks(fontsize=12)
ax.set_xticks(np.linspace(1, 5, num=5))

plt.ylim(0,60)
ax.set_yticks(np.linspace(0, 60, num=7))
plt.yticks(fontsize=12)
ax.grid(axis='y', linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

# Create legend & Show graphic
#ax.legend(fontsize=11, frameon=True, framealpha=0)
plt.tight_layout()
plt.subplots_adjust(top=0.84)
ax.legend(loc='upper center',fontsize=11,frameon=True,framealpha=0,ncol=2,bbox_to_anchor=(0.5, 1.2))
plt.savefig('multi_get_throughput.pdf')
#plt.show()
