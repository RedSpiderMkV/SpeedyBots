from microbit import *

def main():
    memory = {"left": 0, "right": 0}
    
    left_count = 0
    right_count = 0
    
    display.scroll('Go', wait=0, loop=1)
    while 1:
        if left_detect():
            left_count += 1
            motors(-0.2, 0.3)
        elif right_detect():
            right_count += 1
            motors(0.3, -0.2)
        else:
            right_count = left_count = 0
            
            if right_count > 2 and left_count > 2:
                motors(1.0, 1.0)
            else:
                motors(0.4, 0.4)
            
        if memory["left"] > 4 and memory["right"] > 4:
            motors(0.1,0.1)
            right_count = left_count = 0
            

def left_detect():
    return pin1.read_analog() > 255

def right_detect():
    return pin2.read_analog() > 255

def motors(l,r):
    left_motor(l)
    right_motor(r)

def left_motor(s):
    _motor(s,pin12,pin8,0)

def right_motor(s):
    _motor(s,pin16,pin0,1)

_p=[0,0]
def _motor(s,p0,p1,i):
    m = 0
    _p[i]+=abs(s)
    if _p[i]>1:
        m=1
        _p[i]-=1
    _pin(p0,(s>0)&m)
    _pin(p1,(s<0)&m)

def _pin(p, v):
    p.write_digital(v)

main()