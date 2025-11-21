"""
In this assignment, you will create a Python script to practice basic file operations using the os module. Your script will organize files into newly created directories based on their file types.

Objectives
Create a new directory.
Create subdirectories and organize files into them.
Understand and apply basic file operations in Python.
 

Instructions
Create a new Python script named file_organizer.py.
Use the os.mkdir() function to create a new directory named MyFiles.
Inside MyFiles, create three subdirectories named Docs, Images, and Videos using the same mkdir() function.
"""

import os

def main():

    # Create a new directory
    os.mkdir("MyFiles")

    # Create subdirectories 
    os.mkdir("MyFiles/Docs")
    os.mkdir("MyFiles/Images")
    os.mkdir("MyFiles/Videos")

main()    