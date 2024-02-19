"""Demonstrate basic list syntax"""

# Initialize an empty list

grocery_list: list[str] = list() # List constructor
grocery_list: list[str] = [] # Literal constructor

grocery_list.append("bananas") # Append will add to very end of list

# print(grocery_list)



# Initialize an already populated list
grocery_list2: list[str] = ["bananas", "bread", "pasta"] # Literal constructor

grocery_list2.append("new bananas") # Append will add to very end of list

print("Old grocery list: ")
print(grocery_list2)

grocery_list2[0] = "old bananas" # Modifying by index

print("Updated grocery list: ")
print(grocery_list2)

