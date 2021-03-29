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

args = parser.parse_args()

logging.debug("rs-raw.py args: " + str(args))

if args.file:
	#send commands line by line from file
	with open(args.file) as file:
		for cmd in file:
			cmd = cmd.rstrip()
			#log and send
			logging.debug("Sending " + str(cmd))
			out = rsutils.send_rig_cmd(cmd)

			#print raw command and raw output
			print(str(cmd) + " --> " + str(out))
			

elif args.commands:
	for cmd in args.commands:
		
		#log and send
		logging.debug("Sending " + str(cmd))
		out = rsutils.send_rig_cmd(cmd)

		#print raw command and raw output
		print(str(cmd) + " --> " + str(out))

else:
    logging.error("rs-raw.py invoked with no args")

