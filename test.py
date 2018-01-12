import sys
import os

dir_name = "default_name"
repo_name = "default_comment"

def syntaxErr():
	print("""Bad use of script.
Proper syntax:
./script_name -d dir_name -r repo_name""")
	exit()

if len(sys.argv) != 5:
	syntaxErr()

if sys.argv[1] == "-d" and \
	sys.argv[3] == "-r" or \
	sys.argv[1] == "-r" and \
	sys.argv[3] == "-d":
	if sys.argv[1] == "-d":
		dir_name = sys.argv[2]
		repo_name = sys.argv[4]
	else:
		dir_name = sys.argv[4]
		repo_name = sys.argv[2]
else:
	syntaxErr()


print(dir_name)
print(repo_name)
os.system("mkdir %s; cd %s; touch README.md; echo \"%s\" > README.md" % (dir_name,dir_name,repo_name))
os.system("cd %s; git init; git add README.md; git commit -m \"Init commit\"; hub create -d \"%s\"; git push origin master" % (dir_name,repo_name))

