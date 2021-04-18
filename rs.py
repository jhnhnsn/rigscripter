## **** TODO ACTUALLY TEST THIS ***

#Send raw command strings to rig and print out raw responses
#example commands for testing: 'FB147960000', 'FA146960000', 'FB', 'MT001'

import logging
import argparse
import rsutils #project import
import memorymanager #project import

#get logifle name from global config and start logging
logging.basicConfig(filename=rsutils.read_rs_config_file()["logfile"], level=logging.DEBUG)

#parse arguments
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-c', '--commands', nargs='+', help='Send a one or more raw command strings to the rig')
group.add_argument('-f', '--file', help="Send commands from a file. One raw command per line")
group.add_argument('-r', '--repl', action='store_true', help="Enter commands one at a time at the prompt. Type 'quit' to quit.")

args = parser.parse_args()

logging.debug("rs-raw.py args: " + str(args))

def logandsend(cmdtosend):
	#log and send
	logging.debug("Sending " + str(cmdtosend))
	out = rsutils.send_rig_cmd(cmdtosend)
	#print raw command and raw output
	return(str(cmdtosend) + " --> " + str(out))

if args.file:
	#send commands line by line from file
	with open(args.file) as file:
		for cmd in file:
			cmd = cmd.rstrip()
			res = logandsend(cmd)
			print(res)
			

elif args.commands:
	for cmd in args.commands:
		res = logandsend(cmd)
		print(res)

elif args.repl:
	print("In REPL mode. Type 'quit' to quit.")
	while 1:
		cmd = input("rs> ")
		if cmd == "quit":
			break
		else:
			res = logandsend(cmd)
			print(res)

else:
	print("No args. Try --help for help.")
	logging.error("rs-raw.py invoked with no args")
	


