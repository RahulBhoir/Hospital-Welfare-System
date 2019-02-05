""""
Module Name: Find_a_donor.py
Description: This file allow user to get organ donor when required.
Last Edited by: Rahul Bhoir
Date:21/10/2018
"""
def donor():
    print("Find a Donor")

    # opening file to read data
    f = open("organ.txt", "r")

    #for reading lines from the file
    f1 = f.readlines()

    # for displaying data
    for x in f1:
        print(x)
