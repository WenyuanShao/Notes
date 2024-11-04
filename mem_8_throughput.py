import numpy as np
import matplotlib.pyplot as plt

#Data
rate = [25,50,75,100,125,150,175,200,225,250]
shared_memcached = [1.685592,2.209204,2.164801,2.067841,1.976733,1.947107,1.942640,1.946988,1.942594,1.943053]
separate_memcached = [1.685323,3.428034,4.584384,4.641337,4.554204,4.611238,4.556382,4.538523,4.637747,4.659758]
cos = [1.685587,3.434304,5.182925,6.994016,8.105674,8.127538,8.129643,8.139585,8.158418,8.119010]
Janus = [1.685542,3.433994,5.182668,6.994796,8.680770,10.492593,10.708696,10.738576,10.741923,10.672641]

fig, ax = plt.subplots(figsize=(6, 4))

# Use hatch patterns for each bar group
ax.plot(rate, shared_memcached, marker="D", linestyle='-.', label='Linux Shared Memcached', linewidth=2)
ax.plot(rate, separate_memcached, marker="^", linestyle='--', label='Linux Separate Memcached', linewidth=2)
ax.plot(rate, Janus, marker="s", label='Janus', linestyle='-', linewidth=2)
ax.plot(rate, cos, marker='o', label='Composite', linestyle=':', linewidth=2)

# Title & Subtitle
ax.set_ylabel('Goodput (million requests)', fontsize=14)
ax.set_xlabel('Client sending rate (1K packets per client per second)', fontsize=14)

#ax.set_xticklabels([50, 100, 150, 200, 250], fontsize=12)
plt.xticks(fontsize=12)

plt.ylim(0,12)
ax.set_yticks(np.linspace(0, 12, num=5))
plt.yticks(fontsize=12)
ax.grid(axis='y', linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

# Create legend & Show graphic
#ax.legend(fontsize=11, frameon=True, framealpha=0)
plt.tight_layout()
plt.subplots_adjust(top=0.84)
ax.legend(loc='upper center',fontsize=11,frameon=True,framealpha=0,ncol=2,bbox_to_anchor=(0.5, 1.2))
plt.savefig('mem_8_throughput.pdf')
#plt.show()
