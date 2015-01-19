# This is a script to generate a random number
# and then convert it to binary and hex values
#
# Version 1.0
# Tom Yarrish

import random

# This function is going to generate a random number from 1-255, and then
# return the decimal,along with the corresponding binary and hexidecimal value
def random_number_generator():
    ran_decimal = random.randint(1, 255)
    return (ran_decimal, bin(ran_decimal), hex(ran_decimal))


numbers_start = 0
numbers_end = 40

# We're going to open a file to write the output too and then run the
# random number generator function
with open("random_list.txt", "w") as ran_file:
    ran_file.write("Decimal\t\t\tBinary\t\t\tHexadecimal\n")
    while numbers_start < numbers_end:
        results = random_number_generator()
        ran_file.write("{}\t\t\t{}\t\t\t{}\n".format(*results))
        numbers += 1
    