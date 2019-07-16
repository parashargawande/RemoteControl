import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os,json
import signal,time
import subprocess
import getpass


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
	
def main():
	print("hello main")
	addToStartUp("main.py")
if __name__ == "__main__":
	main()
