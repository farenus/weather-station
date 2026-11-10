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


def measurement():
    return tuple(sensor.read_compensated_data())
