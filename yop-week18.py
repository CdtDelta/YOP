# This script I wrote to help in determining the final grade for
# a class I teach.
#
#
# By Tom Yarrish
# Version 0.1


midterm_total = raw_input("Enter the Midterm grade: ")
final_total = raw_input("Enter the Final Grade: ")
lab_total = raw_input("Enter the Lab Total Grade: ")
homework_total = raw_input("Enter the Homework Total Grade: ")
participation_total = raw_input("Enter the Participation Grade: ")

midterm_calc = float(midterm_total) * 0.2
final_calc = float(final_total) * 0.2
lab_calc = float(lab_total) * 0.3
homework_calc = float(homework_total) * 0.2
participation_calc = float(participation_total) * 0.1

extra_credit = raw_input("Enter extra credit score (Enter if none): ")

if extra_credit:
    grade = (midterm_calc + final_calc + lab_calc + homework_calc + participation_calc) + int(extra_credit)
else:
    grade = midterm_calc + final_calc + lab_calc + homework_calc + participation_total

print "Grade is {}\n".format(int(grade))
