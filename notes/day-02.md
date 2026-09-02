# Day 2 - Linux Files, Permissions and Shell Confidence

## What I Learned

Linux is widely used in DevOps because servers, containers and CI/CD systems often run on Linux.

Today I learned how to move around the Linux filesystem, create files and folders, copy files, rename files and remove files.

I also learned that Linux permissions control who can read, write or execute a file.

## Linux Permissions

The three main permissions are:

- r = read
- w = write
- x = execute

Permissions can apply to the file owner, group and other users.

For example, `chmod 700 backup.sh` gives the owner read, write and execute permission while giving no permissions to the group or other users.

## Pipes

The pipe symbol `|` sends the output of one command into another command.

For example:

`ls -lah practice | grep input`

lists the practice directory and then searches the result for the word `input`.

## Exit Codes

Linux commands return exit codes.

An exit code of `0` normally means the command succeeded.

A non-zero exit code normally means something went wrong.

This is useful in automation because scripts and CI/CD systems can use exit codes to decide whether to continue or stop.

## Backup Script

I created a Bash script that copies `practice/input/report.txt` into the `practice/backup` directory.

The script adds a timestamp to every backup filename so that running the script again does not overwrite the previous backup.

## Mistake and Fix

I tested what would happen if the source file was missing.

The backup script returned an error because `practice/input/report.txt` could not be found.

The script returned exit code `1`.

I restored the correct file name and ran the script again.

The backup succeeded and returned exit code `0`.
