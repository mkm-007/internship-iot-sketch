from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .bridge import LedCommand


@dataclass
class Esp8266Sim:
    pins: dict = field(default_factory=dict)
    log: List[str] = field(default_factory=list)

    def digital_write(self, cmd: LedCommand) -> None:
        self.pins[cmd.pin] = cmd.state
        self.log.append(f"GPIO{cmd.pin}={cmd.state}")
