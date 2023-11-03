        #     MOSES ODENY
        #  SCT211-0099/2022
            # QUESTION 4


givenyear = int(input("year to be checked = "))
daysinleapyear = int(input("days in a leap year = "))
daysingivenyear = int(input("the days in the given year = "))


def leapYear(daysingivenyear,daysinleapyear):
    if(daysingivenyear == daysinleapyear):
        print( givenyear, "is a leap year" )
    else:
        print( givenyear, "is not a leap year ")    

leapYear(daysingivenyear,daysinleapyear)

# if(daysingivenyear == daysinleapyear):
#     print("the given year is a leap year")
# else:
#     print("the given year is not a leap year ")    
