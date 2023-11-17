import board
import pulseio
import time

#Define pulsein objects to count encoder A pin pulses (B is ignored since we are not concerned about direction)
encoder1 = pulseio.PulseIn(board.GP12, maxlen=10000)
encoder2 = pulseio.PulseIn(board.GP20, maxlen=10000)

#Initialise previous time variables
encoder1_previous_time = time.monotonic()
encoder2_previous_time = time.monotonic()

#Define encoder pulses per revolution
pulses_per_revolution = 300 #This value was determined experimentally, I can't find the true value anywhere on the encoder website as there is no datasheet available to my knowledge

def calculate_rps(count, time_interval):
    if time_interval != 0:
        revolutions = count / pulses_per_revolution
        rps = revolutions / time_interval
        return rps
    else:
        return 0

def left_rps():
    global encoder1_previous_time
    
    #Pause pulse counter
    encoder1.pause()
    
    #Count the pulses
    encoder1_count = len(encoder1)
    
    #Calculate the time interval between the previous count
    current_time = time.monotonic()
    time_interval = current_time - encoder1_previous_time

    #Calculate RPS
    rps = calculate_rps(encoder1_count, time_interval)

    #Clear the pulse counter
    encoder1.clear()
    
    #Reset the previous time
    encoder1_previous_time = current_time
    
    #Resume the pulse counter
    encoder1.resume()
    
    return rps

def right_rps():
    global encoder2_previous_time
    
    #Pause pulse counter
    encoder2.pause()
    
    #Count the pulses
    encoder2_count = len(encoder2)
    
    #Calculate the time interval between the previous count
    current_time = time.monotonic()
    time_interval = current_time - encoder2_previous_time

    #Calculate RPS
    rps = calculate_rps(encoder2_count, time_interval)

    #Clear the pulse counter
    encoder2.clear()
    
    #Reset the previous time
    encoder2_previous_time = current_time
    
    #Resume the pulse counter
    encoder2.resume()
    
    return rps
