#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time

def simulate_bus_traffic(num_packets=100):
    for _ in range(num_packets):
        # 15% packets are malicious
        if random.random() < 0.15:
            pkt = [time.time(), random.randint(0, 255), random.uniform(80, 120)]
            print(f"ATTACK PACKET: {pkt}")
        else:
            pkt = [time.time(), random.randint(0, 255), random.uniform(40, 60)]
            print(f"NORMAL PACKET: {pkt}")
        time.sleep(0.1)

if __name__ == "__main__":
    simulate_bus_traffic()

