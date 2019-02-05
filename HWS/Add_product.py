class Add_Product:
    def __init__(self):
        print("ADD PRODUCT")

    def product_details(self):

        self.product_name = input("enter the product name:")
        self.units = int(input("enter the units:"))

    def validate_product(self):

        if self.product_name.isalnum():
            pass
        else :
            print("enter valid data")
            exit()

        if self.units >0:
            self.units = str(self.units)
        else :
            print("enter positive number")

    def add_product(self):

        f = open("product.txt","a")

        f.write("\n")
        f.write("product:")
        f.write(self.product_name)
        f.write("\t")
        f.write("units:")
        f.write(self.units)

        f.close()


ap = Add_Product()
ap.product_details()
ap.validate_product()
ap.add_product()


