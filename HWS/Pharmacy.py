class Pharmacy:
    def __init__(self):
        print("ONLINE STORE")

    def search_product(self):
        self.product = input("Product name:")

    def check_product(self):
        try:

            # opening file to read data
            file = open("product.txt", "r")

            #read lines from file
            read = file.readlines()

            #close file
            file.close()

            for word in self.product:
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
            print(count1,"units of ",self.product, "available")
            b = input("Buy (Y/N)?")
            if b=="Y" or b=="y":
                self.uname = input("username:")
                self.units = int(input("how many units to buy: "))
                self.address = input("adrress:")
                self.mobile = input("Mobile no:")
                self.count1 = self.count1 - self.units
                print("Customer Name:",self.uname,"\n","Product Name:",self.product,"\n","Mobile No:",self.mobile,"\n","Delivery Address:",self.address,"\n")
                print("Delivery will be done in 2-3 hours")
        except FileExistsError:
            print("error")

p = Pharmacy()
p.search_product()
p.check_product()

