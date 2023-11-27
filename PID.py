import motors
import time

#Initial PWM Input Values
left_pwm = 0.35
right_pwm = 0.35

#Global Variables
optimal_distance = 35
integral = 0
maxintegral = 0.05
previous_error = 0
previous_time = time.monotonic()

#PID Constants
kp = 0.00005
ki = 0.0005
kd = 0.005

def Calculate_PID(leftdistance):
    global left_pwm, right_pwm, integral, previous_error, previous_time

    error = leftdistance - optimal_distance
    dt = time.monotonic() - previous_time

    proportional = kp * error
    integral += (ki * error) / dt if dt != 0 else ki * error
    derivative = (kd * (error - previous_error)) / dt if dt!= 0 else (kd * (error - previous_error)

    if integral > maxintegral:
        integral = maxintegral
    elif integral < -maxintegral:
        integral = -maxintegral

    pwm_change = proportional + integral + derivative

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
    previous_time = time.monotonic()
