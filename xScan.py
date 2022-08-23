import subprocess
import re
import time
import argparse
from datetime import datetime
from os import system

datatime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')


def banner():
    banner = '''
                _________                     
___  __________/   _____/ ____ _____    ____  
\  \/  /\_  __ \_____  \_/ ___\\__  \  /    \ 
 >    <  |  | \/        \  \___ / __ \|   |  \\
/__/\_ \ |__| /_______  /\___  >____  /___|  /
      \/              \/     \/     \/     \/ 
                        -- givemefivw
    '''
    print(banner)



def xscan(file):
    system(r"start cmd /k " + "xray.exe" + r" webscan --listen 127.0.0.1:7799 --html-output ./report_{}.html".format(datatime))
    time.sleep(5)
    target = open(file, 'r', encoding='utf-8')
    lines = target.readlines()
    pattern = re.compile(r'^(https|http)://')
    for line in lines:
        try:
            if not pattern.match(line.strip()):
                url = "http://" + line.strip()
            else:
                url = line.strip()
            system("rad.exe" + " " + "-t " + url + " -http-proxy 127.0.0.1:7799")
        except Exception as e:
            pass
    target.close()

def main():
    parser = argparse.ArgumentParser(description='xrScan help Info')
    parser.add_argument('-f','--file',help='scan targets from file',default='')
    args = parser.parse_args()

    if args.file:
        file = args.file
        xscan(file)
            


if __name__ == '__main__':
    banner()
    main()