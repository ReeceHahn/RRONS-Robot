import board
import pulseio
import time

#Define pulsein objects to count encoder A pin pulses (B is ignored since we are not concerned about direction)
encoder1 = pulseio.PulseIn(board.GP12, maxlen=5000)
encoder2 = pulseio.PulseIn(board.GP20, maxlen=5000)

#Initialise count variables
encoder1_count = 0
encoder2_count = 0

#Initialise previous time variables
encoder1_previous_time = time.monotonic()
encoder2_previous_time = time.monotonic()

#Define encoder pulses per revolution
pulses_per_revolution = 150

# Function to calculate RPS from encoder counts
def calculate_rps(count, time_interval):
    if time_interval != 0:
        revolutions = count / pulses_per_revolution
        rps = revolutions / time_interval
        return rps
    else:
        return 0

def left_rps():
    global encoder1, encoder1_count, encoder1_previous_time
    
    current_time = time.monotonic()
    time_interval = current_time - encoder1_previous_time

    # Calculate RPS
    rps = calculate_rps(encoder1_count, time_interval)

    # Reset count
    encoder1_count = 0

    # Update the previous time
    encoder1_previous_time = current_time

    # Reset the pulsein object to start counting again
    encoder1.pause()
    encoder1.clear()
    encoder1.resume()

    # Sleep for a short duration to control the update rate
    time.sleep(0.1)

    # Count the pulses to update counts
    encoder1_count = len(encoder1)
    
    return rps

def right_rps():
    global encoder2, encoder2_count, encoder2_previous_time
    
    current_time = time.monotonic()
    time_interval = current_time - encoder2_previous_time

    # Calculate RPS
    rps = calculate_rps(encoder2_count, time_interval)

    # Reset count
    encoder2_count = 0

    # Update the previous time
    encoder2_previous_time = current_time

    # Reset the pulsein object to start counting again
    encoder2.pause()
    encoder2.clear()
    encoder2.resume()

    # Sleep for a short duration to control the update rate
    time.sleep(0.1)

    # Count the pulses to update counts
    encoder2_count = len(encoder2)
    
    return rps
