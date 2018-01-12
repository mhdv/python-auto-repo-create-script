import sys
import os

dir_name = "default_name"
commit = "Added project files"

if len(sys.argv) == 1:
	os.system("git add -A; git commit -m \"Update\"; git push origin master")

dir_name = sys.argv[2]
if len(sys.argv) > 2:
	commit = sys.argv[3]

print(dir_name)
print(commit)
os.system("cd %s; git add -A; git commit -m \"%s\"; git push origin master" % (dir_name,commit))

