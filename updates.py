import os
import git
from git import Repo
import subprocess

def main():
	os.system("rmdir /s /Q updates")
	os.system("mkdir updates")
	Repo.clone_from("https://github.com/parashargawande/RemoteControl.git", "updates")
	os.system("move /Y updates\* .")
	updateCommand="python main.py"
	proc = subprocess.Popen('start cmd /k %s' % updateCommand, shell=True)
	os.system("del updating.py")
	exit()
if __name__ == "__main__":
	main()
