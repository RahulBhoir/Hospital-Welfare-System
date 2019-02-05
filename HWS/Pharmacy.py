""""
Module Name: Pharmacy.py
Description: This file allow the user to login to access the system.
Last Edited by: Rahul Bhoir
Date:21/10/2018
"""
def buy_product():
    print("Search Product")

    pname =input("enter product name:-")        #enter product name


    def product_search(filename, listwords):

        try:

            # opening file to read data
            file = open(filename, "r")

            #read lines from file
            read = file.readlines()

            #close file
            file.close()

            for word in listwords:
                lower = word.lower()
                count1 = 0

                for sentance in read:

                    # spliting the words on the line by space
                    line = sentance.split()

                    for each in line:
                        line2 = each.lower()
                        line2 = line2.strip("!@#$%^&*()-*")

                        if lower == line2:
                            count1 += 1
            print(count1,"units of ",listwords, "available")
            b = input("Buy (Y/N)?")
            if b=="Y" or b=="y":
                uname = input("username:")
                units = int(input("how many units to buy: "))
                address = input("adrress:")
                mobile = input("Mobile no:")
                count1 = count1 - units
                print("Customer Name:",uname,"\n","Product Name:",pname,"\n","Mobile No:",mobile,"\n","Delivery Address:",address,"\n")
                print("Delivery will be done in 3-5 hours")
        except FileExistsError:
            print("error")
    product_search("product.txt",[pname])