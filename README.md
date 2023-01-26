# learning

### Assume the current directory is where we want the new repository to be created
### Create the new repository

git init

### Add a remote for and fetch the old repo
git remote add -f old_a <OldA repo URL>

### Merge the files from old_a/master into new/master
git merge old_a/master

### Commit

git commit -m "Message"

---

git init

git remote add -f learning-matlab https://github.com/corey-richardson/learning-matlab

git merge learning-matlab/master

git remote add -f learning-python https://github.com/corey-richardson/learning-python

git merge learning-python/master

git remote add -f learning-c https://github.com/corey-richardson/learning-c

git merge learning-c/master

git remote add -f learning-cpp https://github.com/corey-richardson/learning-cpp

git merge learning-cpp/master

git remote add -f learning-c-sharp https://github.com/corey-richardson/learning-c-sharp

git merge learning-c-sharp/master

git commit -m "Merged all learning repos into one central"