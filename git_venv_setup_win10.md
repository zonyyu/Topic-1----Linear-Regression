# Setting up Git and Virtual Environments on Windows

## Setting up Git

1. Go to [https://git-scm.com/download/win](https://git-scm.com/download/win) to download `git` for windows
2. To test if `git` is installed, open an instance of **Windows PowerShell** and type the following:
```ps
\> git --version
```
You should see something like this:
```
git version 2.32.0.windows.1
```

## Setting up Virtual Environments

1. Open an instance of **Windows PowerShell** in **Administrator** mode and type the following:
```ps
\> set-executionpolicy remotesigned
```
2. Type in ```A``` for "Yes to all"
3. Now run the virtual env script.