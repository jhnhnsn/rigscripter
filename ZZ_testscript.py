from yaesu991a import atob, btoa, atstate, atcontrol, atstart

## VFO Swap tests
#test atob()
print("Testing atob() - swapping VFO-A to VFO-B")
atob()

#test btoa()
print("Testing atob() - swapping VFO-B to VFO-A")
btoa()

## Antenna tuner control
print("Testing Antenna tuner control - including if/elif/else flow control to create a toggle")
if(atstate()):
    print("Antenna tuner is on. Turning it off.")
    atcontrol("off")
elif(atstate() == False):
    print("Antenna tuner is off. Turning it on")
    atcontrol("on")
else:
    print("Must have been an error or something. Shouldn't get here")
