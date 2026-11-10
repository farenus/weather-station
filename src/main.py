import bme280_float
import machine

i2c = machine.I2C(0, sda=machine.Pin(8), scl=machine.Pin(9), freq=400000)

sensor = bme280_float.BME280(i2c=i2c)


def measurement():
    return tuple(sensor.read_compensated_data())
