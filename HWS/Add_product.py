""""
Module Name: Add_product.py
Description: This file will help admin to add new product to the product database.
Last Edited by: Rahul Bhoir
Date:21/10/2018
"""
def product():
    print("Add Product")

    # enter medicine name
    med = input("medicine name:")


    #Storing input data into the file
    if med.isalnum():
        # opening the file to write data in it
        f = open("product.txt", "a")

        # entering the medicine data to the file
        f.write(med)
        f.write("\n")

        # closing the file
        f.close()

        # display message when data entry is done successfully
        print("database updated")
    else:
        # display message when their is any error
        print("invalid entry")
        exit()