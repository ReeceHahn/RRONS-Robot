import board
import digitalio
import time

switch_C = digitalio.DigitalInOut(board.GP9)
switch_C.direction = digitalio.Direction.INPUT
switch_C.pull = digitalio.Pull.UP

def value():
    return switch_C.value
