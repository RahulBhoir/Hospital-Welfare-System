class Appointmnet:
    def __init__(self):
        self.user_name = ""
        self.dname = " "
        self.mobile = " "

    def enter_details(self):

        self.user_name = input("patient username: ")
        self.mobile = input("mobile number: ")
        self.dname = input("doctor name: ")     # entering doctor name

    def validate_details(self):

        # validation for doctor name
        if self.dname.isalpha():
            print()
        else:
            print("invalid doc name")
            exit()

        # validation for patient name
        if self.user_name.isalpha():
            print()
        else:
            print("invalid patient name")
            exit()

        # validation for mobile number of the patient
        if self.mobile.isdigit() and len(self.mobile) == 10:
            print()
        else:
            print("invalid mobile number")
            exit()
        print("success")

    def add_appointment(self):

        f= open("patient.txt", "a")
        f.write("\n")
        f.write("Patient name:")
        f.write(self.user_name)
        f.write("\t")
        f.write("Mobile number:")
        f.write(self.mobile)
        f.write("\t")
        f.write("doctor name:")
        f.write(self.dname)
        f.write("\t")
        f.close()


app = Appointmnet()
app.enter_details()
app.validate_details()
app.add_appointment()