# updated file
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os,json
import signal,time
import subprocess
import getpass
import time
import git
from git import Repo

global email
global NotificationFlag
global proc
proc=""
NotificationFlag=False

email="par@gmail"
# Fetch the service account key JSON file contents
cred = credentials.Certificate('firebase-adminsdk.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://automate-e9fec.firebaseio.com/'
})

def addToStartUp(filename):
	USER_NAME = getpass.getuser()
	bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
	os.system('copy "%s" "%s"' %(filename,bat_path) )

def updateSelf():
	updateCommand="echo updating the project"
	proc = subprocess.Popen('start cmd /k %s' % updateCommand, shell=True)

def Testing():
	proc = subprocess.Popen("start cmd", shell=True)
	time.sleep(5)
	pid=os.getpid()
	print(pid)
	try:
		subprocess.call(['taskkill', '/F', '/T', '/PID',  str(pid)])
	except:
		print("error")
def update():
	os.system("move updates.py updating.py")
	updateCommand="python updating.py"
	proc = subprocess.Popen('start cmd /k %s' % updateCommand, shell=True)
	exit()
	
def main():
	print("updated main.py started")
#	addToStartUp("main.py")
	a=int(input("update (1)?"))
	if a==1:
		update()
if __name__ == "__main__":
	main()

