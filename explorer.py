#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep
import random
import sys

gyro = ev3.GyroSensor()
gyro.mode = 'GYRO-ANG'
us   = ev3.UltrasonicSensor()
ir   = ev3.InfraredSensor('in4')
ir4 = True #geeft aan of de IR-sensor op poort 4 aangesloten is.
try:
    us.mode = 'US-DIST-CM'
    ir.mode = 'IR-PROX'
except Exception:
    ir   = ev3.InfraredSensor('in3')
    ir4 = False
    us.mode = 'US-DIST-CM'
    ir.mode = 'IR-PROX'

motorleft = ev3.LargeMotor('outB')
motorright = ev3.LargeMotor('outC')
motorir = ev3.MediumMotor('outA')

step = 10

def debug_print(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)

def irvalue():
    if ir4:
        return ir.value()
    else:
        return us.value()

def scan():
    motorir.run_to_rel_pos(position_sp=-180, speed_sp=200, stop_action="hold")
    motorir.wait_while('running')
    dist_max = irvalue()
    angle = -180
    angle_max = [angle]
    for _ in range(360//step):
        motorir.run_to_rel_pos(position_sp=step)
        motorir.wait_while('running')
        dist = irvalue()
        angle += step
        # debug_print(dist,angle)
        if dist > dist_max:
            dist_max = dist
            angle_max = [angle]
        elif dist == dist_max:
            angle_max.append(angle)
    motorir.run_to_rel_pos(position_sp=-180)
    motorir.wait_while('running')
    return (dist_max,angle_max)

def analyse_scan(angles):
    return random.choice(angles)

def drive(speed):
    motorleft.run_forever(speed_sp=speed)
    motorright.run_forever(speed_sp=speed)

def stop():
    motorleft.stop()
    motorright.stop()

def reset_gyro():
    gyro.mode = 'GYRO-RATE'
    gyro.mode = 'GYRO-ANG'

def turn(angle):
    reset_gyro()
    if angle < 0:
        motorleft.run_forever(speed_sp=-200)
        motorright.run_forever(speed_sp=200)
    else:
        motorleft.run_forever(speed_sp=200)
        motorright.run_forever(speed_sp=-200)
    # debug_print(gyro.value())
    while gyro.value() < angle - 2 or gyro.value() > angle + 2:
        sleep(0.01)
        # debug_print(gyro.value())
    stop()
    # debug_print(gyro.value())

while True:
    drive(500)
    while ir.value() > 50 and us.value() > 25:
        # debug_print(ir.value(),us.value())
        sleep(.05)
    # debug_print(ir.value(),us.value())
    stop()
    dist, angles = scan()
    # debug_print(dist,angles)
    angle = analyse_scan(angles)
    turn(angle)