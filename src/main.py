import time

import network

import api
import config
import measurement
import wifi

while True:
    try:
        wifi.connect()
        status = api.post(measurement.get())
        print(f"http status: {status}")
    except OSError as e:
        print(e)
    finally:
        network.WLAN(network.STA_IF).active(False)
    time.sleep(config.SEND_INTERVAL)
