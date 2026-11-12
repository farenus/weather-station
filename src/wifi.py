import time

import network

import config


def connect(timeout=15):
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    if nic.isconnected():
        return nic
    nic.connect(config.WLAN_SSID, config.WLAN_PASSWORD)
    start = time.ticks_ms()
    while not nic.isconnected():
        if time.ticks_diff(time.ticks_ms(), start) > timeout * 1000:
            nic.disconnect()
            raise RuntimeError("nie udało się połączyć z wifi")
        time.sleep(0.5)
    return nic
