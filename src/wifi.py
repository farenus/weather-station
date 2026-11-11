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
    ip, netmask, gateway, dns = nic.ifconfig()
    print(
        f"ip: {ip}",
        f"netmask: {netmask}",
        f"gateway: {gateway}",
        f"dns: {dns}",
        sep="\n",
    )
    return nic
