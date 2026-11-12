import time

import network

import api
import config
import measurement
import wifi

nic = wifi.connect()
print(
    f"ip: {nic.ifconfig()[0]}",
    f"dns: {nic.ifconfig()[3]}",
    sep="\n",
)

while True:
    try:
        wifi.connect()
        data = measurement.get()
        print(data)
        status = api.post(data)
        print(f"http status: {status}")
    except OSError as e:
        print(e)
    finally:
        network.WLAN(network.STA_IF).active(False)
    time.sleep(config.SEND_INTERVAL)
