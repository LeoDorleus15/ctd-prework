# This script asks the user for their age, then prints a personalized
# message telling them whether they're a minor or an adult.

name = "Leopold"          
min_adult_age = 18         

age_input = input("What is your age? ")   
age = int(age_input)                       

if age >= min_adult_age:
    print(name + ", at age " + str(age) + " you are considered an adult.")
else:
    print(name + ", at age " + str(age) + " you are still a minor.")
