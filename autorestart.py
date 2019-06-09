import os
import subprocess
import sys
import time


if __name__ == '__main__':
    count = 1
    while True:
        print ('Starting Discord Bot')
        try:
            subprocess.call([sys.executable, 'afat_r.py'], shell=False)
        except:
            print ('gg')
        print ('Waiting... '+str(count))
        count += 1
        time.sleep(1)
        print (str(os.getpid())+' Restarting...')