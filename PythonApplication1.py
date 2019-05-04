
food_tuple = ("apple","Fries", "Pizza", "Chips", "Taco")

new_list = list(food_tuple)

new_item = input("Enter a new food item that you like!: ")
new_list.append(new_item)

new_food_tuple = tuple(new_list)

#Checking if tuple
try:
	check_tuple = input("List and Tuple switched!! Now try entering a new item: ")
	new_food_tuple[2] = check_tuple
except TypeError:  #I want this still to run to check if its back to a tuple, so I didn't use else.
	print("Checked, it's back to a Tuple")

#printing tuple to screen
print("\nHere's your list of Foods")
for i in new_food_tuple:
	print("* " + i)
