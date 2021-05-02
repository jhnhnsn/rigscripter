import serial
from datetime import datetime
import json
import logging
from os import listdir, path

#Get config file location
script_dir = path.dirname(path.abspath(__file__))
RS_CONFIG_FILE = path.join(script_dir, 'rs_config.json')

#read global config file
def read_rs_config_file():
    #read config json
    with open(RS_CONFIG_FILE) as file:
        rs_config = json.load(file)
    return rs_config


#get logfle name from global config and start logging
logging.basicConfig(filename=read_rs_config_file()["logfile"], level=logging.DEBUG)

#logging format
def rslog(logstring):
    timestamp = str(datetime.now().strftime("%m-%d-%Y_%H-%M-%S-%f"))
    logging.debug(timestamp + " : " + logstring)

#read config file and send back a configured serial object
def get_serial():
    
    #RIG_SERIAL_CONFIG_FILE = './rig_serialconfig.json'
    config = read_rs_config_file()
    RIG_SERIAL_CONFIG_FILE = config["rig_serial_config_file"]

    #read config json
    with open(RIG_SERIAL_CONFIG_FILE) as file:
        rig_conf_json = json.load(file)

    # configure the serial connections (the parameters differs on the device you are connecting to)
    ser = serial.Serial(
        port        =   rig_conf_json["port"],
        baudrate    =   int(rig_conf_json["baudrate"]),
        parity      =   rig_conf_json["parity"],
        stopbits    =   int(rig_conf_json["stopbits"]),
        bytesize    =   int(rig_conf_json["bytesize"]),
        timeout     =   float(rig_conf_json["timeout"])
    )

    #return the serial port
    return ser


#Format a simple string and convert command to binary eg add ; at the end for sending to rig
def cmdstr_to_cmdbin(cmd):
    #check if it's a string
    if type(cmd) == str:
        #check that the last character is a ;, if not add one
        if cmd[-1] != ';':
            cmd = cmd + ';'
        #convert to binary ascii
        cmd = bytes(cmd, encoding="ascii")
        return cmd

    else:
        return "Not a string"


#convert a binary command to string for output or saving
#not sure if this is necessary
def cmdbin_to_cmdstr(cmd):
    #check if it's binary
    if type(cmd) == bytes:
        cmd = cmd.decode('ascii')
        cmd = cmd.rstrip(';')
        return cmd
    else:
        return "Not binary"


#send a command to the rig return the raw response
#assumes commands are all strings now
def send_rig_cmd(cmd):
    rslog("Sending --> " + str(cmd))
    ser = get_serial()
    cmd = cmdstr_to_cmdbin(cmd)
    ser.write(cmd)
    out = ser.readline()
    out = cmdbin_to_cmdstr(out)
    rslog("Received --> " + out)
    if(out == "?"):
        #TODO: turn this into an exception
        rslog("Got an error - rig returned: " + out)
        return False
        ser.close()
    else:
        return out
        ser.close()
    ser.close()

def strip_prefix(cmd):
    out = cmd[2:]
    return out

def strip_menu_return(cmd):
    out = cmd[3:]
    return out

