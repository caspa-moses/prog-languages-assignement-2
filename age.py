        #     MOSES ODENY
        #   SCT211-0099/2022
        #     QUESTION ONE

name = input("enter your name:" )
birthyear = int(input("enter your year of birth:" ))
birthmonth = int(input("enter your birth month number:" ))
birthdate = int(input("enter your date of birth:" ))
currentyear = int(input("enter the current year:" ))
month = int(input("enter the current month number :" ))
currentdate = int(input("enter the current date:" ))

yearage = int(currentyear - birthyear)
monthage = int(month - birthmonth)
daysage = int(currentdate)

print("my name is ",name,"and my age is",  yearage, "years", monthage, "months",daysage, "days")
