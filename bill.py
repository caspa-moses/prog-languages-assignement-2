    #       MOSES ODENY
        # SCT211-0099/2022
            # QUESTION 2

bill = int(input("enter the total bill amount: "))
totalpeople = int(input("enter the total number of people: "))
tippercent = float(10/100)

amountperperson =float( bill/totalpeople )
tip = int(tippercent*bill)

print("the amount each person should pay is", amountperperson,)
print("the tip paid is",tip) 
