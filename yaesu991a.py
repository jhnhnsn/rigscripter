## FT991a operating manual
## CAT commands manual: https://www.yaesu.com/downloadFile.cfm?FileID=13370&FileCatID=158&FileName=FT%2D991A%5FCAT%5FOM%5FENG%5F1711%2DD.pdf&FileContentType=application%2Fpdf

import rsutils #project import

## SWAP VFOS
# {"catcmd": "AB", "desc": "VFO-A TO VFO-B"},
def atob():
    cmd = "AB"
    out = rsutils.send_rig_cmd(cmd)    
    print(str(out))

# {"catcmd": "BA", "desc": "VFO-B TO VFO-A"},
def btoa():
    cmd = "BA"
    rsutils.send_rig_cmd(cmd)  

## ANTENNA TUNER CONTROL
# {"catcmd": "AC", "desc": "ANTENNA TUNER CONTROL"},
def atstate():
    cmd =   "AC"
    out = rsutils.send_rig_cmd(cmd)
    if(out == "AC001"):
        return True
    elif(out == "AC000"):
        return False
    
def atcontrol(state):
    if state == "on":
        cmd = "AC001"
    elif state == "off":
        cmd = "AC000"
    out = rsutils.send_rig_cmd(cmd)

def atstart():
    #To be tested
    cmd = "AC002"
    out = rsutils.send_rig_cmd(cmd)
  

# "300":   {"catcmd": "AG", "desc": "AF GAIN"},
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
# "2500" : {"catcmd": "EX", "desc": "MENU"},
# "2600" : {"catcmd": "FA", "desc": "FREQUENCY VFO-A"},
# "2700" : {"catcmd": "FB", "desc": "FREQUENCY VFO-B"},
# "2800" : {"catcmd": "FS", "desc": "FAST STEP"},
# "2900" : {"catcmd": "FT", "desc": "FUNCTION TX"},
# "3000" : {"catcmd": "GT", "desc": "AGC FUNCTION"},
# "3100" : {"catcmd": "ID", "desc": "IDENTIFICATION"},
# "3200" : {"catcmd": "IF", "desc": "INFORMATION"},
# "3300" : {"catcmd": "IS", "desc": "IF-SHIFT"},
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
