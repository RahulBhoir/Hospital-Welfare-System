""""
Module Name: check_appointment.py
Description: This file allow actor to check the appointments for the doctors.
Last Edited by: Rahul Bhoir
Date:21/10/2018
"""
def check():
    print("Appointment Details:")

    # opening file to read data
    f = open("patient.txt", "r")

    #for reading line from the file
    f1 = f.readlines()

    # for displaying data
    for x in f1:
        print(x)