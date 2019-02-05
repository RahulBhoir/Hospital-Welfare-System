
class Quick_diagnosis:
    def __init__(self):
        print("QUICK DIAGNOSIS")

    def quick_diagnosis(self):
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")

        # to search the treatment

        # enter the data
        query = input("Enter Diagnosis: ")

        # search for the data entered by the user
        for j in search(query, tld="co.in", num=10, stop=1, pause=2):
            # print links available for that diagnosis
            print(j)

qd = Quick_diagnosis()
qd.quick_diagnosis()