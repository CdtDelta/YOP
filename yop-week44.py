# This is yet another math script, this time focusing on division
# And yes, I meant to name the functions that way
#
#
# Tom Yarrish
# Version 1.0
#
# Licensed under the GPL
# http://www.gnu.org/copyleft/gpl.html

import random

def devide(x, y):
    answer = x / y
    return answer

def multeply(x,y):
    answer = x * y
    return answer

print "Welcome to the division testing program!"
low_num = raw_input("What's the lowest number you want to use?" )
hi_num = raw_input("What's the highest number you want to use?" )
count = raw_input("How many problems do you want? ")

count = int(count)
low_num = int(low_num)
hi_num = int(hi_num)

while count > 0:
    x = random.randrange(low_num, hi_num)
    y = random.randrange(low_num, hi_num)
    product = multeply(x, y)
    answer = devide(product, y)
    guess = raw_input("What is {} divided by {}? ".format(product, y))
    if answer == int(guess):
        print "That's correct!  Good job!"
    else:
        print "Sorry that's not the right answer..."
    count -= 1
    