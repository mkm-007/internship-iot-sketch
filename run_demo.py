#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from iot_sketch import Esp8266Sim, parse_assistant_phrase

PHRASES = [
    "Hey Google, turn on the LED",
    "Hey Google, turn off the light",
    "What's the weather",
]


def main():
    mcu = Esp8266Sim()
    print("ESP8266 voice→LED internship sketch (simulated)")
    for p in PHRASES:
        cmd = parse_assistant_phrase(p)
        print(f"\nphrase: {p}")
        if not cmd:
            print("  (no LED command)")
            continue
        mcu.digital_write(cmd)
        print(f"  -> {mcu.log[-1]} pins={mcu.pins}")


if __name__ == "__main__":
    main()
