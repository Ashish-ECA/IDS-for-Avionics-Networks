# Intrusion Detection System (IDS) for Avionics Networks

## Overview
This project develops a prototype Intrusion Detection System (IDS) designed to monitor and detect anomalies in avionics communication networks such as MIL-STD-1553 or CAN bus. The IDS aims to identify suspicious activities like spoofing, message replay, and flooding attacks using anomaly detection techniques powered by machine learning.

## Installation

Install required packages using:

pip install -r requirements.txt

## How to Run

### Simulate Attacks

Run this to simulate avionics attacks:

python simulate_attacks.py

### Run the IDS

Start the IDS to capture and analyze network traffic:

python ids.py

*Note: You might need admin/root privileges for packet sniffing.*

## Sample Output

IDS Prediction Output:

Packet: [1757914545.9572082, 98, 56.395989453279164], Status: Normal
Packet: [1757914545.9673202, 19, 48.359695887656336], Status: Normal
Packet: [1757914545.9776764, 218, 38.94254781555465], Status: Anomaly Detected!
Packet: [1757914545.9884856, 182, 56.13083109547495], Status: Normal
Packet: [1757914545.9980187, 168, 48.06514577171264], Status: Normal

Simulation Traffic Output:

ATTACK PACKET: [1757914546.0081234, 209, 82.92051817065511]
NORMAL PACKET: [1757914546.008142, 91, 58.332375178179355]
ATTACK PACKET: [1757914546.0081494, 86, 112.71925388838596]
NORMAL PACKET: [1757914546.0081596, 114, 43.762808722959754]
NORMAL PACKET: [1757914546.0081654, 211, 40.612787170467925]

## Features
- Real-time monitoring of avionics bus messages  
- Anomaly detection model trained to identify malicious traffic patterns  
- Simulation of common avionics attacks for validation  
- Data logging for forensic and analysis purposes  
- Visualization dashboard to observe traffic anomalies (optional)

## How to Run
1. Install dependencies:  
pip install scapy numpy scikit-learn matplotlib
2. Use provided scripts to simulate avionics bus traffic and inject attack scenarios.  
3. Run the IDS script to capture traffic and detect anomalies in real-time.  
4. Monitor console outputs or plots showing detected suspicious activities.

## File Structure
- `ids.py` — Main IDS script capturing and analyzing bus traffic  
- `simulate_attacks.py` — Scripts to simulate spoofing, replay, and flooding attacks  
- `models/` — Pretrained ML models for anomaly detection  
- `logs/` — Captured traffic and alerts  
- `README.md` — Project documentation and usage instructions

## Methodology
- Capture avionics network packets using packet sniffing tools.  
- Extract feature vectors representing message timing, frequency, and content.  
- Train machine learning models (e.g., Isolation Forest, One-Class SVM) on normal traffic to identify anomalies.  
- Flag suspicious packets and trigger alerts for investigation.

## Future Work
- Extend IDS capabilities to support more avionics protocols (e.g., ARINC 429).  
- Integrate with hardware-based real-time monitoring systems.  
- Develop automated mitigation by actively filtering malicious traffic.

## References
- Aviation Today, “Cybersecurity in the Skies,” 2024  
- Research papers on anomaly detection in MIL-STD-1553 and CAN bus networks  
- Open-source IDS frameworks adapted for avionics

## Contact
ashishprajit308@gmail.com
