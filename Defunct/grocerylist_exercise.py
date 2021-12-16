# we will submit this as a link to our repository 
# Grocery App
# Complete & Submit the Exercise

# Description
# You are responsible for creating an app that manages groceries. Your groceries are characterized by Shopping Lists which can contain grocery items. Here are the features you need to implement:
#     You need to ask the user for the input.
#     A user should be able to create a shopping list.
#         A shopping list consists of a title and address.
#             Example = Fiesta, Walmart, Sams Club, Cosco, Randalls etc
#     A user should be able to add multiple shoppings lists
#     Give user an option to display the list
#     A user should be able to add a grocery items to a particular shopping list. A grocery item consists of a title, price, quantity.
#         Example Milk, Cookies, Paper, Napkins, Soda, Chips etc
# Fiesta
# Milk, Soda, Fish
# Walmart
# Paper, Napkins, Plate, Chips
# Sams Club
# Chicken, Beef, Eggs, Sugar, Salt, Pepper, Honey



shopping_lists = [] 

class GroceryItem: 
    def __init__(self, name): 
        self.name = name 

class ShoppingList: 
  def __init__(self, name, address): 
    self.name = name 
    self.address = address 
    self.grocery_items = [] 
  
  def add_grocery_item(self, item):
    self.grocery_items.append(item)
    

def display_all_shopping_lists(): 
    for index in range(0, len(shopping_lists)):
      shopping_list = shopping_lists[index]
      print(f"{index +1}. {shopping_list.name}") # the dot is for dispay purposes 1. walmart, 2 fiesta., 3 aldi. etc


print("1. Add a shopping list")
print("2. add item to an existing shopping list")
print("3. display shopping lists")
print("q to quit")

choice = input("Enter choice: ")

if choice == "1": 
  display_all_shopping_lists() 
  name = input("Enter name of shopping list: ")
  address = input("Enter shopping list address: ")
  shopping_list = ShoppingList(name, address)
  shopping_lists.append(shopping_list)
elif choice ==  "2":
    item = input("Enter the item: ")
    choice.add_grocery_item(item)
elif choice == "3": 
  display_all_shopping_lists() 