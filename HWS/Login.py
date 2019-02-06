""""
Module Name: Login.py
Description: This file allow the user to login to access the system.
Last Edited by: Rahul Bhoir
Date:06/02/2019
"""


def login():
    print("Login page \n")

    # enter the username
    user_name = input("Username:-")

    # enter the password
    password = input("Password:-")

    # username validation
    def wordcount(filename, word, passwd):

        try:
            # opening the file to read data
            file = open(filename, "r")

            read = file.readlines()

            # closing the file
            file.close()

            for word in word:
                lower = word.lower()        # convert string into lower-case
                count1 = 0
                for sentance in read:
                    line = sentance.split()

                    for each in line:
                        line2 = each.lower()
                        line2 = line2.strip("!@#$%^&*()-*")

                        if lower == line2:
                            count1 += 1
                                                                                                        #print(lower,":", count1)
        except FileExistsError:
            print("error")

    # password validation
        try:
            # opening the file for reading data
            file = open(filename, "r")

            # reading line from the file
            read_password = file.readlines()

            # closing the file
            file.close()

            for word in passwd:
                passwd1 = word.lower()
                pss_count = 0
                for a in read_password:

                    # spliting the words on the line by space
                    line = a.split()

                    for each in line:
                        passwd2 = each.lower()
                        passwd2 = passwd2.strip("!@#$%^&*()-*")

                        if passwd1 == passwd2:
                            pss_count += 1
                                                                                                    # print(lower,":", count2)
        except FileExistsError:
            print("error")

        if count1 == 1 and pss_count == 1:
            print("welcome", user_name)
        else:
            print("try again")

    wordcount("user_details.txt", [user_name], [password])
