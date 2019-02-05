class Login:
    def __init__(self,):
        self.user_name = " "
        self.password  = " "
        self.un_count = 0
        self.pss_count = 0
        self.filename = "user_details.txt"

    def enter_details(self):
        print("Login page \n")

        # enter the username
        self.user_name = input("Username:-")

        # enter the password
        self.password = input("Password:-")

    #username validation
    def wordcount(self,):

        print(self.filename)

        try:
            # opening the file to read data
            file = open("user_details.txt", "r")

            read = file.readlines()

            #closing the file
            file.close()

            for word in self.user_name:
                un = word.lower() #convert string into lower-case
                self.un_count = 0
                print("##1")

                for i in read:
                    line = i.split()
                    print("##2")

                    for each in line:
                        line2 = each.lower()
                        line2 = line2.strip("!@#$%^&*()-*")
                        print("##3")

                        if un == line2:
                            self.un_count += 1
                            print(self.un_count)
                                                                                                        #print(lower,":", un_count)
        except FileExistsError:
            print("error")

    # password validation
        try:
            #opening the file for reading data
            file = open("user_details.txt", "r")

            #reading line from the file
            read_password = file.readlines()

            #closing the file
            file.close()

            for word in self.password:
                passwd1 = word.lower()
                self.pss_count = 0
                for a in read_password:

                    #spliting the words on the line by space
                    line = a.split()

                    for each in line:
                        passwd2 = each.lower()
                        passwd2 = passwd2.strip("!@#$%^&*()-*")

                        if passwd1  == passwd2:
                            self.pss_count += 1
                            print(self.pss_count)
                                                                                                    #print(lower,":", count2)
        except FileExistsError:
            print("error")
        print("success")
        print(self.pss_count)
        print(self.un_count)

    def display_msg(self):
        if (self.un_count == 1 and self.pss_count == 1):
            print("welcome",self.user_name)
            #exit()
        else:
            print("try again")
            #exit()

l = Login()
l.enter_details()
l.wordcount()
l.display_msg()

