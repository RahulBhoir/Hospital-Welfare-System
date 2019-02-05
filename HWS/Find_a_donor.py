class Find_Donor:
    def donor(self):
        print("Find a Donor")

        # opening file to read data
        f = open("organ.txt", "r")

        # for reading lines from the file
        f1 = f.readlines()

        # for displaying data
        for x in f1:
            print(x)