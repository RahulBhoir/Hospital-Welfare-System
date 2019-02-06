class Organ_Donation:
    def __init__(self):
        print("Organ Donation Form")
        print(10 * "=", "Donor Form", 10 * "=")

    def enter_details(self):
        # enter first name
        self.fname = input("First Name:-")

        # enter last name
        self.lname = input("Last Name:-")

        # enter mobile number
        self.mobile = input("Mobile No:-")


        # enter organ to donate
        self.organ = input("Organ to donate:" )


        # enter gender
        self.gender = input("Gender (M/F):")

    def validate(self):

        # validation for correct data
        if (self.fname.isalpha()) == True:
            print()
        else:
            print("invalid entry")
            exit()

        # validation for correct data
        if (self.lname.isalpha()) == True:
            print()
        else:
            print("invalid last name")
            exit()

        # validation for correct data
        if (self.mobile.isdigit()):
            print()
        else:
            print("invalid entry")
            exit()

        # validation for correct data
        if (self.organ.isalpha()):
            print()
        else:
            print("invalid entry")
            exit()

        # validation for correct data
        if (self.gender == "M" or self.gender == "m" or self.gender == "f" or self.gender == "F"):
            print()
        else:
            print("invalid entry")
            exit()

    def add_user(self):         #add donor

        # storing input data if every input data is valid
        f = open("organ.txt", "a")
        f.write("\n")
        f.write("Donor Name:")
        f.write(self.fname)
        f.write(" ")
        f.write(self.lname)
        f.write("\t")
        f.write("mobile no:")
        f.write(self.mobile)
        f.write("\t")
        f.write("Gender:")
        f.write(self.gender.upper())
        f.write("\t")
        f.write("Organ:")
        f.write(self.organ)
        f.write("\t")
        f.close()

        # display message if data entry is successful
        print(" Thank You for Saving a Life")

od = Organ_Donation()
