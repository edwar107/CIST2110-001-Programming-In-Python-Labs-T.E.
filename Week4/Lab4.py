# Lab4
# Author: Terrisha Edwards

"""_summary_
This lab is designed to get you familiar with Python Boolean Expressions, Conditional Expressions, if-elif-else statements, and while / for loops.
"""

# 1. Write some code that asks the user for a number and prints out whether it is positive, negative, or zero.
# get user input (number) (int)
# if number is positive 
# print "positive"
# elif number is negative
# print "negative"
# else
# print "zero"
input_number = int(input("Enter a number: "))
if input_number > 0:
    print("positive")
elif input_number < 0:
    print("negative")
else: 
    print("zero")

# 2. Write some code that asks the user for a number and prints out whether it is even or odd.
get user input (number) (int)
# if number is even 
# print "even"
# else
# print "odd"
# explain modular division in english 
modular division is the remainder of a division problem
# 5 / 2 = 2 remainder 1
# 5 % 2 = 1 remainder 0
# 6 / 2 = 3 remainder 0
# 6 % 2 = 0
input_number = int(input("Enter a number"))
if input_number % 2 = 0:
    print("even") 
else:
    print("odd: ", remainder)


# 3. Write some code that asks the user for a number and prints out all the numbers from 1 to that number using a while loop.
# get user input (number) (int)
# set counter to 1
# while counter < number
# print counter
# increment counter
input_number = int(input("Enter a number: "))
counter = 1
While counter < input_number:
print(counter)
counter += 1 # same thing as counter = counter + 1 
print("done")


# 4. Use a for loop to ask a user for 5 numbers and print out the average of those 5 numbers.
# set sum to 0
# for i in range 5
# get user input (number) (int)
# print sum / 5
sum = 0
for i in range(5)
    input_number = int(input("Enter a number "))
    sum += input_number # same thing as sum = sum + input_number
average = sum / 5
print(average)

# 5. Write some code that prints out all the numbers from 1 to 10 that are divisible by 3 or 5.
# create a for loop that interates from 1 to 10
range 1 to 11 (11 is not included) so that we do not divide by 0 
# if the current number is divisible by 3 or 5
#   print the current number
for i in range(1, 11):
    if i % 3 = 0 or i % 5 = 0:
        print(i)
        elif i % 5 = 0 
        print(i)

# answer with continue statement
for i in range(1, 11):
    if i % 3 = 0 and i % 5 = 0:
        print(i)



# 6. Write some code that asks the user for a number and then prints out a countdown from that number to 1 using a while loop. After the countdown, print "Blast off!".
"Blast off!".
# get user input (number) (int)
# set counter to number 
# while counter > 1
#   print counter
#   decrement counter
# print "Blast off!"
input_number = int(input("Enter a number: "))
counter = input_number
while counter > 1:
    # lets add a sleep function to slow down the countdown
    import time # import the time module (we did not learn about import statements yet)
    time.sleep(1) # sleep for 1 seconf (we will talk about methodS and functions later)
    print(counter)
    counter-= 1 # same thing as counter = counter - 1
time.sleep(4)
print("Blast off!")
# 7. Write some code that asks the user for a number and then uses a for loop to iterate from 1 to that number. If the current number is divisible by 7, print 
"Lucky" and continue to the next iteration. If the current number is greater than 100, break the loop.

input_number = int(input("Enter a number: "))
for i in range(1, input_number + 1): 
# q: why do we need to add 1 to input_number?
# a: range is not inclusive of the last number
    if i % 7 = 0:
        print("Lucky")
        countinue
    if i > 100:
        break 
    print(i)