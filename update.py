#!/usr/bin/python3.6

import os
import subprocess
import sys
import time

def main():
    print ('Starting...')
    cfdir = os.path.abspath(os.path.dirname(__file__))  
    print (os.getcwd())
    if cfdir != os.getcwd():
        os.chdir(cfdir)
    if not os.path.isdir('.git'):
        raise EnvironmentError("This isn't a Git repository.")
    try:
        subprocess.check_call('git --version', shell=True, stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        raise EnvironmentError("Couldn't use Git on the CLI. You will need to run 'git pull' yourself.")
    print("Passed Git checks...")
    print("Attempting to update the bot using Git...")
    try:
        subprocess.check_call('git pull', shell=True)
    except subprocess.CalledProcessError:
        raise OSError("Could not update the bot. You will need to run 'git pull' yourself.")
    print("Attempting to update dependencies...")
    try:
        subprocess.call([sys.executable, '-m', 'pip', 'install', '-U', '-r', 'requirements.txt'], shell=True)
    except subprocess.CalledProcessError:
        raise OSError("Could not update dependencies. You will need to run '{0} -m pip install -U -r requirements.txt' yourself.".format(sys.executable))



if __name__ == '__main__':
    count = 1
    while True:
        main()
        print ('Starting Discord Bot')
        try:
            subprocess.call([sys.executable, 'chatbotbeta.py'], shell=False)
        except:
            print ('gg')
        print ('Waiting... '+str(count))
        count += 1
        time.sleep(3)
        print (str(os.getpid())+' Restarting...')