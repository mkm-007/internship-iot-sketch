# Internship IoT Sketch — ESP8266 voice LED

Portfolio rebuild from the **NSIC Embedded Systems & IoT internship** report/PPT: control an LED via Google Assistant–style voice → cloud/IFTTT-style webhook → ESP8266.

**Display title (locked):** ESP8266 Voice-Triggered LED  
> Skills signal on resume only (no NSIC Experience row). 2026 rebuild; current dates.

---

## Problem

Demo IoT stacks fail when the voice → cloud → MCU path is hand-wavy. This sketch makes the **control path** explicit and testable without requiring live Google / IFTTT credentials.

## Build

```
src/iot_sketch/
  bridge.py     parse assistant phrase → LED command
  firmware_sim.py   ESP8266-side handler simulation
run_demo.py
tests/
```

Flow: phrase → intent (`led_on` / `led_off`) → simulated NodeMCU digital write.

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python run_demo.py
```

## Honesty

Rebuilt from enrolled internship materials for portfolio proof. Not an employer product dump. Embedded C / ESP8266 remain **Skills** on the resume.
