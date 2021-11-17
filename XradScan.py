#!/usr/bin/python
# Author: @Givemefivw
# Descrip: Xray&rad联动扫描
import time
import os
import re
import argparse
import sys
from typing import Pattern

def banner():
	banner = '''
____  ___                  .___
\   \/  /___________     __| _/
 \     /\_  __ \__  \   / __ | 
 /     \ |  | \// __ \_/ /_/ | 
/___/\  \|__|  (____  /\____ | 
      \_/           \/      \/ 
	
		@Givemefivw
	'''
	print(banner)


def xrad(url):
	try:
		outime = '%date:~0,4%%date:~5,2%%date:~8,2%0%time:~1,1%%time:~3,2%%time:~6,2%'
		run_xray = os.system('start cmd /k xray.exe webscan --listen 127.0.0.1:7799 --html-output ./result/Xrad-{}.html'.format(outime))
		time.sleep(5)
		if url.find('http') == -1:
			url = 'http://' + url + '/'
		else:
			url = url
		run_rad = os.system('start cmd /k rad.exe -t {} -http-proxy 127.0.0.1:7799'.format(url))
	except Exception as e:
		pass
	except KeyboardInterrupt:
		sys.exit()

def main():
	parser = argparse.ArgumentParser(description='Xrad Scan Help')
	parser.add_argument('-u','--url',help=' Please set the target url',default='')
	args = parser.parse_args()

	if args.url:
		url = args.url
		xrad(url)
if __name__ == '__main__':
	banner()
	main()