import motors

#Initial PWM Input Values
left_pwm = 0.35
right_pwm = 0.35

#Global Variables
optimal_distance = 35
previous_error = 0

#PID Constants
kp = 0.00005
kd = 0.005

def Calculate_PID(leftdistance):
    global left_pwm, right_pwm, previous_error
    
    error = leftdistance - optimal_distance
    
    proportional = kp * error
    derivative = kd * (error - previous_error)
    
    pwm_change = proportional + derivative
    
    left_pwm -= pwm_change
    right_pwm += pwm_change
    
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
