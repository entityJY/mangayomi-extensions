import os

print("User: git fetch --all")
os.system("git fetch --all")
print("User: git checkout -b updated_extensions upstream/main")
os.system("git checkout -b updated_extensions upstream/main")

print("Single Commit (y/n)")
if input() == "y":
    print("Enter commit id")
    commit = input()
    print("git cherry-pick " + commit)
    os.system("git cherry-pick " + commit)
else:
    print("Enter first commit")
    first_commit = input()
    print("Enter second commit")
    second_commit = input()
    print("User: git cherry-pick " + first_commit + "^.." + second_commit)
    os.system("git cherry-pick " + first_commit + "^.." + second_commit)

print("User: git push -u origin updated_extensions")
os.system("git push -u origin updated_extensions")

print("Enter title")
title = input()
print("Enter body")
body = input()
print("User: gh pr create --head updated_extensions -t \"" + title + "\" -b \"" + body + "\"")
os.system("gh pr create --head updated_extensions -t \"" + title + "\" -b \"" + body + "\" -w")