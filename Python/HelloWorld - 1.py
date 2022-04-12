# I have wanted to leard how to code since I was a teenager and have decided that I will kick start my adult learning through Code Academy.

# Lesson 1 - Welcome

my_name = "Michael"
print("Hello and welcome " + my_name + "!")

# Lesson 2 - Comments

# This is a short comment on my first program.

# Lesson 3 - print

print("Hello World!")

# Lesson 4 - Strings

print("Michael")
print('Michael')

# Lesson 5 - Variables

# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!
meal = "A chicken sandwhich"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner
meal = "Pot roast"
# Printing out dinner
print("Dinner:")
print(meal)

# Lesson 6 - Errors

print("This message has mismatched quote marks!")
print("Abracadabra")

# Lesson 7 - Numbers

# Define the release and runtime integer variables below:
release_year = 2020
runtime = 140
# Define the rating_out_of_10 float variable below:
rating_out_of_10 = 7.8

# Lesson 8 - Caculations

print(25 * 68 + 13 / 28)

# Lesson 9 - Changing Numbers

quilt_width = 8
quilt_length = 8

squares = quilt_width * quilt_length
print(squares)

# Lesson 10 - Exponents

# Calculation of squares for:
# 6x6 quilt
quilt_width = 6
quilt_length = 6
squares = quilt_width * quilt_length
#print("A 6 x 6 quilt requires", 6 ** 2, 'squares.')
print(6 ** 2)
# 7x7 quilt
quilt_width = 7
quilt_length = 7
squares = quilt_width * quilt_length
#print("A 7 x 7 quilt requires", 7 ** 2, 'squares.')
print(7 ** 2)
# 8x8 quilt
quilt_width = 8
quilt_length = 8
squares = quilt_width * quilt_length
#print("A 8 x 8 quilt requires", 8 ** 2, 'squares.')
print(8 ** 2)
# How many squares for 6 people to have 6 quilts each that are 6x6?
quilt_width = 6
quilt_length = 6
squares = quilt_width * quilt_length
number_of_quilts = 6
# total_squares = squares_in_quilt * number_of_quilts

print(squares ** 2)

# Lesson 11 - Modulo

my_team = 27 % 4
print(my_team)

# Lesson 12 - Concatenation

string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = (string1 + string2 + string3 + string4 + string5 + string6)

print(message)

# Lesson 13 - Plus Equals

total_price = 0
new_sneakers = 50.00
total_price += new_sneakers
nice_sweater = 39.00
total_price += nice_sweater
fun_books = 20.00
total_price += fun_books

# Update total_price here:

print("The total price is", total_price)

# Lesson 14 - Muti-line Strings

# Assign the string here
to_you = """
Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
"""

print(to_you)

# Lesson 15 - Review

my_age = 100
half_my_age = 100 / 2
greeting = "Hello, my name is "
name = "Michael "
greeting_with_name = greeting + name + "I am " + str(my_age) + " which is double " + str(half_my_age)

print(greeting_with_name)