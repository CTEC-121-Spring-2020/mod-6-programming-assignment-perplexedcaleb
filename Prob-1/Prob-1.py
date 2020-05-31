# Module 7
#   Programming Assignment 10
#     Prob-1.py

# Caleb Howard

def main():
    sum = 0
    userNumber = float(input("Please type in a number to add. Enter a negative number to quit program. "))
    while userNumber >= 0:
        sum = sum + userNumber
        userNumber = float(input("Please type in a number to add. Enter a negative number to quit program. "))
    print("The total of the numbers entered is", sum)
    
main()    