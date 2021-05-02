## FT991a operating manual: http://www.hfelectronics.nl/docs/Manuals/FT-991A_Manual.pdf
## CAT commands manual: https://www.yaesu.com/downloadFile.cfm?FileID=13370&FileCatID=158&FileName=FT%2D991A%5FCAT%5FOM%5FENG%5F1711%2DD.pdf&FileContentType=application%2Fpdf
## TODO: Add try except blocks around send commands
## TODO: Add custom exceptions for each command function

from rsutils import send_rig_cmd, rslog, strip_prefix, strip_menu_return #project import

#Yaesu F991a globals 
#TODO: Maybe move to a config file
VFO_A = "A"
VFO_B = "B"
VALID_VFO = [VFO_A, VFO_B]
VFO_FREQ_MIN_HZ = 30000         #.03Mhz
VFO_FREQ_MAX_HZ = 470000000     #470MHz
AF_GAIN_MIN = 0
AF_GAIN_MAX = 254
CAT_RATES = {
    0: 4800,
    1: 9600,   
    2: 19200,  
    3: 38400,  
}

## SWAP VFOS - TODO: combine into one functions?
# {"catcmd": "AB", "desc": "VFO-A TO VFO-B"}
def atob():
    cmd = "AB"
    out = send_rig_cmd(cmd)    

# {"catcmd": "BA", "desc": "VFO-B TO VFO-A"},
def btoa():
    cmd = "BA"
    send_rig_cmd(cmd)  

## Antenna tuner control
# {"catcmd": "AC", "desc": "ANTENNA TUNER CONTROL"}
def get_at():
    cmd =   "AC"
    out = send_rig_cmd(cmd)
    if(out == "AC001"):
        return True
    elif(out == "AC000"):
        return False
    
def set_at(at_state):
    cmd = ""
    if at_state == True:
        cmd = "AC001"
    elif at_state == False:
        cmd = "AC000"
    else:
        rslog("Invalid command for set_at(). Options are True or False (on/off)")
    out = send_rig_cmd(cmd)
    return out

def start_at():
    #To be tested. No dummy load for the rig :-(
    cmd = "AC002"
    out = send_rig_cmd(cmd)
    return out

## AF Gain controls
# {"catcmd": "AG", "desc": "AF GAIN"}
def get_afgain():
    cmd = "AG0"
    out = send_rig_cmd(cmd)
    #strip command prefix and convert to int
    out = out[3:]
    out = int(out)
    return(out)

# Sets  the  receiver  audio  volume  level.
def set_afgain(gain):
    #check arg input between 0 - 254
    if(gain >= AF_GAIN_MIN and gain <= AF_GAIN_MAX):    
        #convert to 3 digits and string
        gain = ('{0:03d}'.format(gain))
        gain = str(gain)
        cmd = "AG0" + str(gain)
        out = send_rig_cmd(cmd)
        return True 
    else:
        rslog("set_afgain() value not in range")
        return False

# "400":   {"catcmd": "AI", "desc": "AUTO INFORMATION"},
# "500":   {"catcmd": "AM", "desc": "VFO-A TO MEMORY CHANNEL"},
# "700":   {"catcmd": "BC", "desc": "AUTO NOTCH"},
# "800":   {"catcmd": "BD", "desc": "BAND DOWN"},
# "900" :  {"catcmd": "BI", "desc": "BREAK-IN"},
# "1000" : {"catcmd": "BP", "desc": "MANUAL NOTCH"},
# "1100" : {"catcmd": "BS", "desc": "BAND SELECT"},
# "1200" : {"catcmd": "BU", "desc": "BAND UP"},
# "1300" : {"catcmd": "BY", "desc": "BUSY"},
# "1400" : {"catcmd": "CH", "desc": "CHANNEL UP/DOWN"},
# "1500" : {"catcmd": "CN", "desc": "CTCSS/DCS NUMBER"},
# "1600" : {"catcmd": "CO", "desc": "CONTOUR"},
# "1700" : {"catcmd": "CS", "desc": "CW SPOT"},
# "1800" : {"catcmd": "CT", "desc": "CTCSS"},
# "1900" : {"catcmd": "DA", "desc": "DIMMER"},
# "2000" : {"catcmd": "DN", "desc": "DOWN"},
# "2100" : {"catcmd": "DT", "desc": "DATE AND TIME"},
# "2200" : {"catcmd": "ED", "desc": "ENCORDER DOWN"},
# "2300" : {"catcmd": "EK", "desc": "ENT KEY"},
# "2400" : {"catcmd": "EU", "desc": "ENCORDER UP"},

# {"catcmd": "EX", "desc": "MENU"}
## Menu item cmd format EX12312345678

#menu item 031 CAT RATE
def get_catrate():
    cmd = "EX031"
    out = send_rig_cmd(cmd)
    out = strip_prefix(out)
    out = strip_menu_return(out)
    out = CAT_RATES[int(out)]
    
    return out
    
#def set_catrate():
#    return False


## Get and set VFO frequencies
# {"catcmd": "FA", "desc": "FREQUENCY VFO-A"}
# {"catcmd": "FB", "desc": "FREQUENCY VFO-B"}
def get_vfo(vfo, format="hz"):
    vfo = vfo.upper()

    if(vfo in VALID_VFO):
        cmd = "F" + vfo
        out = send_rig_cmd(cmd)

        if(format == "hz"):
            out = out[2:]
            out = int(out)
            return out
        elif(format == "string"):
            out = out[2:]
            #make a nice string
            mhz = str(int(out[0:3]))
            khz = "{}".format(out[3:6])
            hz = "{}".format(out[6:9])
            freqstring = mhz + "." + khz + hz + "MHz"
            return freqstring
        elif(format == "raw"):
            return out
    else:
        rslog("Not a valid VFO for get_vfo()")
        return False

#Set VFO frequency in Hz
def set_vfo(vfo, freq_hz):
    vfo = vfo.upper()
    if(freq_hz >= VFO_FREQ_MIN_HZ and freq_hz <= VFO_FREQ_MAX_HZ):
        if(vfo in VALID_VFO):
            freq_padded = "{:0>9d}".format(freq_hz)
            cmd = "F" + vfo
            cmd = cmd + str(freq_padded)
            out = send_rig_cmd(cmd)
            
            #No output from radio
            return True
        else:
            rslog("Not a valid VFO for get_vfo()")
            return False
    else:
        rslog("Invalid frequency range for set_vfo() " + str(FREQ_MIN_HZ) + " - " + str(FREQ_MAX_HZ))

# "2800" : {"catcmd": "FS", "desc": "FAST STEP"},
# "2900" : {"catcmd": "FT", "desc": "FUNCTION TX"},
# "3000" : {"catcmd": "GT", "desc": "AGC FUNCTION"},

## Radio ID
# Usage: get_id(format) where format=num returns int with ID, 
# format="name" returns name string, format="raw" returns raw CAT cmd return (minus the ;)
# {"catcmd": "ID", "desc": "IDENTIFICATION"}
def get_id(format="name"):
    cmd = "ID"
    out = send_rig_cmd(cmd)
    
    if(format == "num"):
        #strip command prefix
        out = out[3:]           #TODO: use rsutils strip_prefix      
        out = int(out)          #TODO: move this value to a config file
        return out
    elif(format == "name"):
        return "FT-991A"        #TODO: move this value to a config file
    elif(format == "raw"):
        return out

#{"catcmd": "IF", "desc": "INFORMATION"}
def get_info():
    cmd = "IF"
    out = send_rig_cmd(cmd)
    raw = out #save the raw response for later
    ret = {}
    
    #strip command prefix
    out = out[2:]

    #3 chars current memory channel
    ret["active_mem"] = out[0:3]
    ret["vfoa_freq"] = int(out[3:12])
    ret["clar_offset"] = int(out[12:17])
    ret["rx_clar_on"] = bool(out[17:18])  #0 = OFF, 1 = ON
    ret["tx_clar_on"] = bool(out[18:19])  #0 = OFF, 1 = ON

    op_mode = out[19:20]
    if(op_mode == "1"):
        ret["op_mode"] = "LSB"
    elif(op_mode == "2"): 
        ret["op_mode"] = "USB"
    elif(op_mode == "3"):
        ret["op_mode"] = "CW"
    elif(op_mode == "4"):
        ret["op_mode"] = "FM"
    elif(op_mode == "5"):
        ret["op_mode"] = "AM"
    elif(op_mode == "6"):
        ret["op_mode"] = "RTTY-LSB"
    elif(op_mode == "7"):
        ret["op_mode"] = "CW-R"
    elif(op_mode == "8"):
        ret["op_mode"] = "DATA-LSB"
    elif(op_mode == "9"):
        ret["op_mode"] = "RTTY-USB"
    elif(op_mode == "A"):
        ret["op_mode"] = "DATA-FM"
    elif(op_mode == "B"):
        ret["op_mode"] = "FM-N"
    elif(op_mode == "C"):
        ret["op_mode"] = "DATA-USB"
    elif(op_mode == "D"):
        ret["op_mode"] = "AM-N"
    elif(op_mode == "E"):
        ret["op_mode"] = "C4FM"
    else:
        ret["op_mode"] = "Error?"

    mem_mode = out[20:21] #TODO: find a better name for this
    if(mem_mode == "0"):
        ret["mem_mode"] = "VFO"
    elif(mem_mode == "1"):
        ret["mem_mode"] = "Memory"
    elif(mem_mode == "2"):
        ret["mem_mode"] = "Memory Tune"
    elif(mem_mode == "3"):
        ret["mem_mode"] = "Quick Memory Bank (QMB)"
    else:
        ret["mem_mode"] = "Error?"
    
    code_type = out[21:22]
    if(code_type == "0"):
        ret["code_type"] = "CTCSS OFF"
    elif(code_type == "1"):
        ret["code_type"] = "CTCSS ENC/DEC"
    elif(code_type == "2"):
        ret["code_type"] = "CTCSS ENC"
    elif(code_type == "3"):
        ret["code_type"] = "DCS ENC/DEC"
    elif(code_type == "4"):
        ret["code_type"] = "DCS ENC"
    else:
        ret["code_type"] = "Error?"

    simplex = out[24:25]
    if(simplex == "0"):
        ret["simplex"] = "Simplex"
    elif(simplex == "1"):
        ret["simplex"] = "Plus Shift"
    elif(simplex == "2"):
        ret["simplex"] = "Minus Shift"
    else:
        ret["simplex"] = "Error?"

    ret["raw_output"] = raw
    
    return ret

# {"catcmd": "IS", "desc": "IF-SHIFT"}
def get_ifshift():
    return False

def set_ifshift():
    return False

# "3400" : {"catcmd": "KM", "desc": "KEYER MEMORY"},
# "3500" : {"catcmd": "KP", "desc": "KEY PITCH"},
# "3600" : {"catcmd": "KR", "desc": "KEYER"},
# "3700" : {"catcmd": "KS", "desc": "KEY SPEED"},
# "3800" : {"catcmd": "KY", "desc": "CW KEYING"},
# "3900" : {"catcmd": "LK", "desc": "LOCK"},
# "4100" : {"catcmd": "LM", "desc": "LOAD MESSEGE"},
# "4200" : {"catcmd": "MA", "desc": "MEMORY CHANNEL TO VFO A"},
# "4300" : {"catcmd": "MC", "desc": "MEMORY CHANNEL"},
# "4400" : {"catcmd": "MD", "desc": "MODE"},
# "4500" : {"catcmd": "MG", "desc": "MIC GAIN"},
# "4600" : {"catcmd": "ML", "desc": "MONITOR LEVEL"},
# "4700" : {"catcmd": "MR", "desc": "MEMORY READ"},
# "4800" : {"catcmd": "MS", "desc": "METER SW"},
# "4900" : {"catcmd": "MT", "desc": "MEMORY CHANNEL WRITE/TAG"},
# "5100" : {"catcmd": "MW", "desc": "MEMORY WRITE"},
# "5200" : {"catcmd": "MX", "desc": "MOX SET"},
# "5300" : {"catcmd": "NA", "desc": "NARROW"},
# "5400" : {"catcmd": "NB", "desc": "NOISE BLANKER"},
# "5500" : {"catcmd": "NL", "desc": "NOISE BLANKER LEVEL"},
# "5600" : {"catcmd": "NR", "desc": "NOISE REDUCTION"},
# "5700" : {"catcmd": "OI", "desc": "OPPOSITE BAND INFORMATION"},
# "5800" : {"catcmd": "SO", "desc": "FFSET (Repeater Shift)"},
# "5900" : {"catcmd": "PA", "desc": "PRE-AMP (IPO)"},
# "6100" : {"catcmd": "PB", "desc": "PLAY BACK"},
# "6200" : {"catcmd": "PC", "desc": "POWER CONTROL"},
# "6300" : {"catcmd": "PL", "desc": "SPEECH PROCESSOR LEVEL"},
# "6400" : {"catcmd": "PR", "desc": "SPEECH PROCESSOR"},
# "6500" : {"catcmd": "PS", "desc": "POWER SWITCH"},
# "6600" : {"catcmd": "QI", "desc": "QMB STORE"},
# "6700" : {"catcmd": "QR", "desc": "QMB RECALL"},
# "6800" : {"catcmd": "QS", "desc": "QUICK SPLIT"},
# "6900" : {"catcmd": "RA", "desc": "RF ATTENUATOR"},
# "7100" : {"catcmd": "RC", "desc": "CLAR CLEAR"},
# "7200" : {"catcmd": "RD", "desc": "CLAR DOWN"},
# "7300" : {"catcmd": "RG", "desc": "RF GAIN"},
# "7400" : {"catcmd": "RI", "desc": "RADIO INFORMATION"},
# "7500" : {"catcmd": "RL", "desc": "NOISE REDUCTION LEVEL"},
# "7600" : {"catcmd": "RM", "desc": "READ METER"},
# "7700" : {"catcmd": "RS", "desc": "RADIO STATUS"},
# "7800" : {"catcmd": "RT", "desc": "CLAR"},
# "7900" : {"catcmd": "RU", "desc": "CLAR UP"},
# "8100" : {"catcmd": "SC", "desc": "SCAN"},
# "8200" : {"catcmd": "SD", "desc": "SEMI BREAK-IN DELAY TIME"},
# "8300" : {"catcmd": "SH", "desc": "WIDTH"},
# "8400" : {"catcmd": "SM", "desc": "S METER"},
# "8500" : {"catcmd": "SQ", "desc": "SQUELCH LEVEL"},
# "8600" : {"catcmd": "SV", "desc": "SWAP VFO"},
# "8700" : {"catcmd": "TS", "desc": "TXW"},
# "8800" : {"catcmd": "TX", "desc": "TX SET"},
# "8900" : {"catcmd": "UL", "desc": "UNLOCK"},
# "9100" : {"catcmd": "UP", "desc": "UP"},
# "9200" : {"catcmd": "VD", "desc": "VOX DELAY TIME"},
# "9300" : {"catcmd": "VG", "desc": "VOX GAIN"},
# "9400" : {"catcmd": "VM", "desc": "[V/M] KEY FUNCTION"},
# "9500" : {"catcmd": "VX", "desc": "VOX"},
# "9600" : {"catcmd": "XT", "desc": "TX CLAR"},
# "9700" : {"catcmd": "ZI", "desc": "ZERO IN"}
