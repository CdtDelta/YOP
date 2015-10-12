# This is a simple math script to help practice multiplication
#
# Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html
import random

def math_question(low, high):
    first_no = random.randrange(low, high)
    second_no = random.randrange(low, high)
    product = int(first_no) * int(second_no)
    answer = raw_input("What is {} times {}? ".format(first_no, second_no))
    if int(answer) == product:
        print "Great job, you answered correctly!"
        return
    else:
        print "Sorry that's not the correct answer, but give it another try!"
        return
    
print "Welcome to the multiplcation testing program!\n"
low_number = raw_input("What is the lowest number you want to use? ")
high_number = raw_input("What is the highest number you want to use? ")
count = raw_input("How many problems do you want to do? ")

ready = raw_input("Are you ready to begin? (Y/N) ")

count = int(count)

if ready.lower() == "y":
    while count > 0:
        math_question(int(low_number), int(high_number))
        count -= 1
        continue
else:
    print "Ok, but be sure to try again soon!"
    exit()
        
print "Thanks for playing!"   