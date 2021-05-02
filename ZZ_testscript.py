## VFO swap
def doswaptests():
    from yaesu991a import atob, btoa

    print("Testing atob() - swapping VFO-A to VFO-B")
    atob()

    #test btoa()
    print("Testing atob() - swapping VFO-B to VFO-A")
    btoa()

## Antenna tuner control
def doattests():
    print("**** Testing Antenna tuner control - including if/elif/else flow control to create a toggle")
    from yaesu991a import get_at, set_at, start_at
    
    if(get_at() == True):
        print("Antenna tuner is on. Turning it off.")
        set_at(False)
    elif(get_at() == False):
        print("Antenna tuner is off. Turning it on")
        set_at(True)
    else:
        print("Must have been an error or something. Shouldn't get here")

    ## Start antenna tuner
    #start_at

##AF gain
def doafgaintests():
    from yaesu991a import get_afgain, set_afgain
    
    print("**** Testing AF gain")
    print("Testing AF gain getter")
    print(get_afgain())

    print("Testing AF gain setter to 255. Should fail")
    print(set_afgain(255))

    print("Testing AF gain setter to 254")
    set_afgain(254)
    print("Set to: " + str(get_afgain()))

    print("Testing AF gain setter to 0")
    set_afgain(0)
    print("Set to: " + str(get_afgain()))
   
    print("Testing AF gain setter to 50")
    set_afgain(50)
    print("Set to: " + str(get_afgain()))

## Radio ID/name  
def doidtest():
    from yaesu991a import get_id

    print("**** Testing Radio ID")
    print(get_id("num"))
    print(get_id("name"))
    print(get_id("raw"))
    print(get_id())

#Set VFO in Hz
def dovfotests():
    from yaesu991a import get_vfo, set_vfo

    TEST_VFO = "A"
    TEST_FREQ = 3000000

    print("VFO " + TEST_VFO + " default (Hz): " + str(get_vfo(TEST_VFO)))
    print("VFO " + TEST_VFO + " string: " + str(get_vfo(TEST_VFO, "string")))
    print("VFO " + TEST_VFO + " Hz: " + str(get_vfo(TEST_VFO, "hz")))
    print("VFO "+ TEST_VFO + " raw: " + str(get_vfo(TEST_VFO, "raw")))

    print("Set " + TEST_VFO + " to " + str(TEST_FREQ) + ": " + str(set_vfo(TEST_VFO, TEST_FREQ)))

def doinfotests():
    from yaesu991a import get_info

    print(get_info())

def docatratemenutests():
    print("**** Running catrate menu tests")
    from yaesu991a import get_catrate

    print("CAT baud rate is: " + str(get_catrate()))


## Run test sets
#doinfotests()
#doswaptests()
#dovfotests()
#doattests()
#doafgaintests()
#doidtest()
docatratemenutests()


