import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from iot_sketch import Esp8266Sim, parse_assistant_phrase


def test_on_off():
    on = parse_assistant_phrase("turn on the LED")
    off = parse_assistant_phrase("turn off the LED")
    assert on and on.state == 1
    assert off and off.state == 0


def test_sim():
    mcu = Esp8266Sim()
    mcu.digital_write(parse_assistant_phrase("enable led"))
    assert mcu.pins[2] == 1
