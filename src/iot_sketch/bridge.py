from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class LedCommand:
    pin: int
    state: int  # 1 on, 0 off
    phrase: str


def parse_assistant_phrase(phrase: str, pin: int = 2) -> LedCommand | None:
    t = re.sub(r"\s+", " ", phrase.strip().lower())
    if "led" not in t and "light" not in t:
        return None
    if any(k in t for k in ("turn on", "switch on", "enable", "on")) and "off" not in t:
        return LedCommand(pin=pin, state=1, phrase=phrase)
    if any(k in t for k in ("turn off", "switch off", "disable", "off")):
        return LedCommand(pin=pin, state=0, phrase=phrase)
    return None
