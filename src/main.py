import time

import measurement
import wifi

wifi.connect()

while True:
    print(measurement.get())
    time.sleep(5)
