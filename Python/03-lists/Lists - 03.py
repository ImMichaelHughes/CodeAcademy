# What is a List?

heights = [61, 70, 67, 64, 65]
broken_heights = [65, 71, 59, 62]

# What can a List contain?

ints_and_strings = [1, 2, 3, "four", "five", "6"]
sam_height_and_testscore = ['Sam', 67, 85.5, True]

# Empty Lists

my_empty_list = []

# List Methods

example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
print(example_list)

#Using Remove
example_list.remove(5)
print(example_list)

# Growing a List: Append

orders = ["daisies", "periwinkle"]
orders.append("tulips")
orders.append("roses")
print(orders)

# Growing a List: Plus (+)

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]
# Create new orders here:
new_orders = ["lilac", "iris"]
orders_combined = orders + new_orders
print(orders_combined)
broken_prices = [5, 3, 4, 5, 4, 4]
print(broken_prices)

# Accessing List Elements

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
employee_four = employees[3]
print(employee_four)
print(employees[6])

# Accessing List Elements: Negative Index

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(last_element, index5_element)

# Modifying List Elements

garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
print(garden_waitlist)
garden_waitlist[1] = "Calla"
print(garden_waitlist)
garden_waitlist[-1] = "Alex"
print(garden_waitlist)

# Shrinking a List: Remove

order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)
new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)
new_store_order_list.remove("Mango")
print(new_store_order_list)
# new_store_order_list.remove("Onions")

# Two-Dimensional (2D) Lists

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]
heights.append(["Vik", 68])
print(heights)
ages = [["Aaron", 15], ["Dhruti", 16]]
print(ages)

# Accessing 2D Lists

class_name_test = [["Jenny", 90], ["Alexus",	85.5], ["Sam",	83], ["Ellie", 101.5]]
print(class_name_test)
sams_score = class_name_test[2][1]
print(sams_score)
ellies_score = class_name_test[-1][-1]
print(ellies_score)

# Modifying 2D Lists

incoming_class = [["Kenny",	"American",	9], ["Tanya", "Russian", 9], ["Madison", "Indian", 7]]
print(incoming_class)
incoming_class[2][2] = 8
print(incoming_class)
incoming_class[-3][-3] = "Ken"
print(incoming_class)

# Review

first_names = ["Ainsley", "Ben", "Chani", "Depak"]
#print(first_names)
preferred_size = ["Small", "Large", "Medium"]
#print(preferred_size)
preferred_size.append("Medium")
#print(preferred_size)
expedited_shipping = [True, False, True, False]
#print(expedited_shipping)
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False,], ["Chani", "Medium", True], ["Depak", "Medium", False]]
#print(customer_data)
customer_data[2][2] = False
#print(customer_data)
customer_data[1].remove(False)
#print(customer_data)
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)