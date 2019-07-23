import sys
import os
import git
from git import Repo
import subprocess

if int(len(sys.argv)) > 1:
		updateCommand=sys.argv[1]
else:
	updateCommand="python main.py"
os.system("rmdir /s /Q updates")
os.system("mkdir updates")
Repo.clone_from("https://github.com/parashargawande/RemoteContro.git", "updates")
os.system("move /Y updates\* .")

proc = subprocess.Popen('start cmd /k %s' % updateCommand, shell=True)
os.system("del updating.py")
