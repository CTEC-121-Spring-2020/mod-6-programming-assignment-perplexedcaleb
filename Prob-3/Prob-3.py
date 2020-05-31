# Module 7
#   Programming Assignment 10
#     Prob-3.py

# Caleb Howard

def main():
   # do not change the while loop definition below
    sum = 0
    while True:
        userNumber = float(input("Please type in a number to add. Enter a negative number to quit program. "))
        if userNumber >= 0:
            sum = sum + userNumber
        else:
            break
    print("The total of the numbers entered is", sum)

main()    