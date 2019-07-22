import git
from git import Repo

def main():
	os.system("rmdir /s /Q updates")
	os.system("mkdir updates")
	Repo.clone_from("https://github.com/parashargawande/RemoteControl.git", "updates")
	os.system("move /Y updates\* .")
if __name__ == "__main__":
	main()