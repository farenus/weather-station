import time

import bme280_float
import machine

import config

i2c = machine.I2C(
    config.I2C_ID,
    sda=machine.Pin(config.PIN_SDA),
    scl=machine.Pin(config.PIN_SCL),
    freq=config.I2C_FREQ,
)

sensor = bme280_float.BME280(i2c=i2c)


def read_sensor():
    return tuple(sensor.read_compensated_data())


def read_measurement():
    temperature, pressure, humidity = read_sensor()
    return {
        "temperature": round(temperature, 2),
        "pressure": round(pressure / 100, 2),
        "humidity": round(humidity, 1),
    }


while True:
    print(read_measurement())
    time.sleep(5)
