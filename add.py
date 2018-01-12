import sys
import os

dir_name = "default_name"
commit = "Added project files"

if len(sys.argv) == 1:
	os.system("git add -A; git commit -m \"Update\"; git push origin master")
if len(sys.argv) == 2:
	dir_name = sys.argv[1]
if len(sys.argv) > 2:
	commit = sys.argv[2]

print(dir_name)
print(commit)
os.system("cd %s; git add -A; git commit -m \"%s\"; git push origin master" % (dir_name,commit))

