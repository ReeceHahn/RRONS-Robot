import motors

#Initial PWM Input Values
left_pwm = 0.45
right_pwm = 0.45

#Global Variables
integral = 0
previous_error = 0

#PID Constants
kp = 0.00008
kd = 0.006

def left_PID(leftdistance, optimal_distance):
    global left_pwm, right_pwm, previous_error
    
    error = leftdistance - optimal_distance
    
    proportional = kp * error
    derivative = kd * (error - previous_error)
    
    pwm_change = proportional + derivative
    
    left_pwm -= pwm_change
    right_pwm += pwm_change

    #simple boundary check to stop the code crashing
    if left_pwm < 0:
        left_pwm = 0
    elif left_pwm > 1:
        left_pwm = 1
    if right_pwm < 0:
        right_pwm = 0
    elif right_pwm > 1:
        right_pwm = 1
    
    motors.speed(left_pwm, right_pwm)
    
    previous_error = error
    
def right_PID(rightdistance, optimal_distance):
    global left_pwm, right_pwm, previous_error
    
    error = rightdistance - optimal_distance
    
    proportional = kp * error
    derivative = kd * (error - previous_error)
    
    pwm_change = proportional + derivative
    
    left_pwm += pwm_change
    right_pwm -= pwm_change

    #simple boundary check to stop the code crashing
    if left_pwm < 0:
        left_pwm = 0
    elif left_pwm > 1:
        left_pwm = 1
    if right_pwm < 0:
        right_pwm = 0
    elif right_pwm > 1:
        right_pwm = 1
    
    motors.speed(left_pwm, right_pwm)
    
    previous_error = error
