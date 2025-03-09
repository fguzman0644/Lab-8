#Fernando Guzman
#03/09/25

##Function that takes a year as a parameter and returns True if the year is a
##leap year, False if it is otherwise.

inputYear = int(input("Please enter a year: "))

def leapYearChecker(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(leapYearChecker(inputYear))
