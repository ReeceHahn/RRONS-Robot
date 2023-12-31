import board
import digitalio
import busio
import adafruit_tca9548a
import adafruit_vl6180x

#Create an I2C Bus
i2c = busio.I2C(board.GP1, board.GP0)

#Create a Multiplexer Object
mux = adafruit_tca9548a.TCA9548A(i2c)

#Create VL6180X sensor objects for each channel
sensor1 = adafruit_vl6180x.VL6180X(mux[0]) #Left Sensor
sensor2 = adafruit_vl6180x.VL6180X(mux[1]) #Middle Sensor
sensor3 = adafruit_vl6180x.VL6180X(mux[2]) #Right Sensor

#Return the reading on the left sensor
def left_distance():
    return sensor1.range

#Return the reading on the middle sensor
def front_distance():
    return sensor2.range

#Return the reading on the right sensor
def right_distance():
    return sensor3.range
