import time

import api
import config
import measurement
import wifi

wifi.connect()

while True:
    try:
        status = api.post(measurement.get())
        print(f"http status: {status}")
    except OSError as e:
        print(e)
    time.sleep(config.SEND_INTERVAL)
