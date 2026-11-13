import machine
import network

import api
import config
import measurement
import wifi

nic = wifi.connect()

if machine.reset_cause() != machine.DEEPSLEEP_RESET:
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
    machine.deepsleep(config.SEND_INTERVAL * 1000)
