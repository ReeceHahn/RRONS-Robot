import time
import board
import rotaryio

#Create RotaryIO objects for both encoders
encoder1 = rotaryio.IncrementalEncoder(board.GP12, board.GP11)
encoder2 = rotaryio.IncrementalEncoder(board.GP20, board.GP21)

#Global Variables
prev_time1 = 0
prev_time2 = 0

prev_position1 = encoder1.position
prev_position2 = encoder2.position

#Function to get the RPS value for encoder 1
def left_rps():
    global prev_time1, prev_position1
    revolutions = (encoder1.position - prev_position1) / 300
    rps = revolutions / (time.monotonic() - prev_time1)
    prev_time1 = time.monotonic()
    prev_position1 = encoder1.position
    return abs(rps)

#Function to get the RPS value for encoder 2
def right_rps():
    global prev_time2, prev_position2
    revolutions = (encoder2.position - prev_position2) / 300
    rps = revolutions / (time.monotonic() - prev_time2)
    prev_time2 = time.monotonic()
    prev_position2 = encoder2.position
    return abs(rps)
