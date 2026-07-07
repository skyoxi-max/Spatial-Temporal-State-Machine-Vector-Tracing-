# Architectural Co-Design and Spatial-Temporal State Machine Vector Tracing for Robust Traffic Violation Monitoring on Unstructured Urban Roads

[![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hardware Target](https://img.shields.io/badge/Hardware-Edge--Embedded%20(RPi5/Jetson)-orange)](https://www.raspberrypi.com/)

This repository hosts the official production-grade software implementation of our unified Edge-to-Cloud Hardware-Software Co-Design Framework. The project links an **Illumination-Aware YOLO (IA-YOLO)** object detection pipeline with an **Automated Spatial-Temporal Violation Detection (A-STVD) State Machine Vector Tracing** algorithm to regulate unconstrained, unstructured urban traffic corridors.

---

## 🛠️ Core Engineering Architecture

Our system addresses three primary constraints typical of edge computing deployments on unconstrained roadways:
1. **Spatio-Temporal Jitter Suppression:** Compresses raw frame-to-frame bounding box coordinate jitter from $\pm 8.2\text{ px}$ down to a stabilized $\pm 1.4\text{ px}$ boundary via a rolling filter kernel, avoiding premature edge threshold alerts.
2. **Deterministic Finite State Machine (DFSM):** Maps continuous vehicle trajectories as directed space-time vectors across structural regions of interest ($\Omega_{R1}$ and $\Omega_{R2}$), systematically isolating true wrong-way violations while dropping legal maneuvers.
3. **Resilient Telemetry Fallback:** Automatically bypasses standard TCP/IP stacks during localized network failure modes, switching to a connectionless physical-layer ESP-NOW broadcast protocol to maintain an operational packet recovery rate of $\sim 81\%$ inside the critical failure domain ($SNR \le 2\text{ dB}$).

---

## 💻 Repository Structure

```text
traffic_violation_monitoring/
│
├── README.md               # System Documentation & Empirical Benchmarks
├── config.py               # Structural Variables and Field Threshold boundaries
├── image_processing.py     # Luma Compensation and Jitter Filtering Modules
├── state_machine.py        # Robust State Machine Execution Engine & Historical Logs
├── telemetry.py            # Telemetry Invariance and Channel Degradation Simulation
└── main.py                 # Deep Multi-Node Analytical Benchmarking Runtime Core
Datasets :Traffic_Enforement
