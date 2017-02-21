# lk

Command line tool for sharing commands and scripts.

**Table of Contents:**

- [Install](#install)
- [Hello world](#hello-world)
- [Create new shell command](#create-new-shell-command)
- [Push command to repository](#push-command-to-repository)
- [Share your command](#share-your-command)
- [List commands](#list-commands)

## Install

pip install git+git://github.com/eyalev/lk.git#egg=lk

## Hello World

### First Run

````
$ lk hello-world

| Command not found locally.
|
| Cloning remote repo: https://github.com/lk-commands/default
| to local path: YOUR_LOCAL_APP_DATA_PATH
|
| Command found in cloned repo at: YOUR_CLONED_REPO_PATH
|
| Adding 'hello-world' to list of local commands.
|
| Command output:

Hello World


````

### Next Runs

````
$ lk hello-world
Hello World
````

## Create New Shell Command

````
$ lk create-shell-command hello-me

| Enter shell command:

echo 'Hello me'

| Command successfully added

````

### Run Command


````
$ lk hello-me
Hello me
````

## Push Command to Repository


````
$ lk push hello-me

| Configuring commands repository
| Create one if needed. Example: https://github.com/your-user-name/lk-commands
| Enter repository URL:

https://github.com/your-user-name/lk-commands

| Pusing command 'hello-me' to repo: https://github.com/your-user-name/lk-commands
|
| Command pushed successfuly.

````

## Share Your Command

Other users can run your lk-command like this:

### First Run

````
$ lk hello-me --repo=https://github.com/your-user-name/lk-commands

# Fetching remote repo: https://github.com/your-user-name/lk-commands

# Found command 'hello-me' in local repo: https://github.com/your-user-name/lk-commands

# Adding 'hello-me' to list of local commands.

# Command contents:
--------------------------------------
echo 'Hello me'
--------------------------------------

# Running command:

Hello me

````

### Next Runs

````
$ lk hello-me
Hello me
````

## List Commands

````
$ lk list

hello-world       # https://github.com/lk-commands/default
hello-me          # https://github.com/your-user-name/lk-commands
...
...
...


````


## Create New Command

The `add-command` command will create a new command python file. 
There, you can add python code for execution.

Example:

````
$ lk add-command command1

| Adding command: command1
| Command location: PATH_TO_COMMAND

````

Now you can edit the file.

Open it with your favorite editor and add custom code.

Example:

````

print('command1 output')

````
