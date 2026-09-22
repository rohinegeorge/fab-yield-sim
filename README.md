# Silicon Fab Yield & Stochastic Logistics Engine

A Python-based discrete-event simulation engine designed to model semiconductor wafer transit across cleanroom process nodes, evaluate particle defect rates, and optimize overall batch yield.

## Overview
- **Process Stages:** Photolithography, Etching, Chemical Vapor Deposition (CVD), Ion Implantation, Chemical-Mechanical Planarization (CMP).
- **Yield Model:** Poisson distribution modeling based on cleanroom defect probability parameters.
- **Output:** Automated pass/fail classification based on an 85% die-yield quality threshold.

## Quick Start
```bash
python3 main.py
```
