import re  # importing this package for using match funtion for validation of email id
class Register:


    def user_details(self):
        # print Registration on the Screen
        print("Registration")

        self.fname = input("First name")    # enter first name
        self.lname = input("Last name")     # enter last name
        self.mobile = input("Mobile No:-")  # enter mobile number
        self.mail = input("E-mail:-")  # enter e-mail
        self.uname = input("Username:-")  # enter username
        self.password = input("Password:-")  # enter password
        self.cpassword = input("Password:-")  # enter  confirm password

    def validate_details(self):

        # validation for first name
        if self.fname.isalpha():
            print()
        else:
            print("invalid entry")
            exit()

        # validation for last name
        if self.lname.isalpha():
            print()
        else:
            print("invalid entry")
            exit()

        # validation for mobile number
        if self.mobile.isdigit() and len(self.mobile) == 10:
            print()
        else:
            print("invalid entry")
            exit()

        # validation for email id
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.mail)
        if (match == None):
            print("invalid mail address")
            exit()
        else:
            print()

        # validation for user name
        if self.uname.isalnum():
            print()
        else:
            print("invalid username")
            exit()

        # validation for password
        if self.password == self.cpassword:
            print()
        else:
            print(" password not match")
            exit()
        print("success")

    def store_detail(self):
        # storing input data if every input data is correct

            f = open("user_details.txt", "a") #opening a file named  user_details.txt
            f.write("\n")
            f.write(self.fname)
            f.write("\t")
            f.write(self.lname)
            f.write("\t")
            f.write(self.mobile)
            f.write("\t")
            f.write(self.mail)
            f.write("\t")
            f.write(self.uname)
            f.write("\t")
            f.write(self.password)
            f.close()
            print("Registration successful")  # display message if data entry is successful
            print()
            print()



# function calls
r = Register()
