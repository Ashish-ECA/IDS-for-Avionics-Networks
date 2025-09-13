#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from sklearn.ensemble import IsolationForest
import random
import time

# Simulated avionics packet structure (timestamp, message_id, data_value)
def generate_normal_packet():
    return [time.time(), random.randint(0, 255), random.normalvariate(50, 5)]

def generate_attack_packet():
    # Simulate spoofing or abnormal data spikes
    return [time.time(), random.randint(0, 255), random.normalvariate(100, 30)]

class AvionicsIDS:
    def __init__(self):
        # Isolation Forest to detect anomalies in 3D feature space
        self.model = IsolationForest(contamination=0.05)
        self.training_data = []

    def collect_training_data(self, num_samples=100):
        for _ in range(num_samples):
            pkt = generate_normal_packet()
            self.training_data.append(pkt)
        self.model.fit(self.training_data)
        print("Training completed.")

    def predict(self, packet):
        pred = self.model.predict([packet])
        return pred[0]  # 1 for normal, -1 for anomaly

def main():
    ids = AvionicsIDS()
    ids.collect_training_data()

    for _ in range(50):
        # Randomly generate normal or attack packets
        if random.random() < 0.1:  # 10% chance of attack packet
            pkt = generate_attack_packet()
        else:
            pkt = generate_normal_packet()

        prediction = ids.predict(pkt)
        status = "Anomaly Detected!" if prediction == -1 else "Normal"
        print(f"Packet: {pkt}, Status: {status}")

        time.sleep(0.5)

if __name__ == "__main__":
    main()

