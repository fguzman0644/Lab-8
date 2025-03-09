#Fernando Guzman
#03/09/25

##Function that takes a list and prints if the value 5 is in that list

def listChecker(my_list):
    if 5 in my_list:
        print("The value 5 is in the list.")
    else:
        print("The value 5 is not in the list.")

list1 = [1, 9, 13, 5, 7]
list2 = [1, 3, 4, 6, 15]

listChecker(list1)
listChecker(list2)
