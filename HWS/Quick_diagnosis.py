""""
Module Name: Quick_diagnosis.py
Description: This file allow the user to get treatment information
Last Edited by: Rahul Bhoir
Date:21/10/2018
"""
def quick_diagnosis():
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    # to search the treatment

    # enter the data
    query = input("Enter Diagnosis: ")

    # search for the data entered by the user
    for j in search(query, tld="co.in", num=10, stop=1, pause=2):

        #print links available for that diagnosis
        print(j)