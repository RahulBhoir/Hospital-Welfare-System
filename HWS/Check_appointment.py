class Check_Appoitnment:

    def appoint_details(self):
        print("Appointment Details:")

        # opening file to read data
        f = open("patient.txt", "r")

        # for reading line from the file
        f1 = f.readlines()

        # for displaying data
        for x in f1:
            print(x)

ca = Check_Appoitnment()
ca.appoint_details()