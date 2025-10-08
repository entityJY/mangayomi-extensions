import os

os.system("git fetch --all")
os.system("git checkout -b updated_extensions upstream/master")

print("Single Commit (y/n)")
if input() == "y":
    print("Enter commit id")
    commit = input()
    os.system("git cherry-pick " + commit)
else:
    print("Enter first commit")
    first_commit = input()
    print("Enter second commit")
    second_commit = input()
    os.system("git cherry-pick " + first_commit + "^.." + second_commit)

os.system("git push -u origin updated_extensions")

print("Enter title")
title = input()
print("Enter body")
body = input()
os.system("gh pr create --head updated_extensions -t \"" + title + "\" -b \"" + body + "\"")