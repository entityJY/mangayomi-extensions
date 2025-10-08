import os

print("User: git fetch --all")
os.system("git fetch --all")

print("Reset extension branch? (y/n)")
if input() == "y":
    print("User: git push -d origin updated_extensions")
    os.system("git push -d origin updated_extensions")
    print("User: git branch -D updated_extensions")
    os.system("git branch -D updated_extensions")
    print("User: git checkout -b updated_extensions upstream/main")
    os.system("git checkout -b updated_extensions upstream/main")
else:
    print("User: git switch updated_extensions")
    os.system("git switch updated_extensions")

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

print("User: gh pr create --head updated_extensions -w")
os.system("gh pr create --head updated_extensions -w")