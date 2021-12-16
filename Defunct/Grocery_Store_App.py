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

class Grocery_Item:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = float(item_price)

class ShoppingList:
    def __init__(self, title, address):
        self.title = title
        self.address = address
        self.grocery_items = []

    def add_grocery_item(self, grocery_item):
        self.grocery_items.append(grocery_item)
    


while True:
    print("\n")
    print("************************************************")
    print("\n")
    print("Press 1 to add a shopping list")
    print("Press 2 to view all shopping lists")
    print("Press 3 to add to an existing list")
    print("Type 'quit' to exit")
    print("\n")
    print("************************************************")
    print("\n")

    choice = input("Enter a selection: ")
    
    if choice == "1":
        title = input("Enter the name of the store: ")
        address = input("Input the address of the store: ")
        # Now we add this instance of the shopping list to shoppinglists
        shopping_list = ShoppingList(title, address)
        shopping_lists.append(shopping_list)

    elif choice == "2":
        # Iterate through the shoppinglists array and print all instances of shoppinglist
        for index in range (len(shopping_lists)):
            # python must know what to print
            shopping_list = shopping_lists[index]
            # Add plus 1 to our print index statement otherwise it'll print starting at 0
            print(f"{index + 1}. {shopping_list.title}")

            for index in range (len(shopping_list.grocery_items)):
                print(f"{index + 1}. {shopping_list.grocery_items[index].item_name}")

    elif choice == "3":
        for index in range(len(shopping_lists)):
            shopping_list = shopping_lists[index]
            print(f"{index + 1}. {shopping_list.title}")
        grocery_store_index = int(input("Input the number of the grocery store list you wish to add to: "))
        shopping_list = shopping_lists[grocery_store_index - 1]
        item_name = input("Input the name of the item: ")
        item_price = float(input("Input the price of the item $.$$: "))
        grocery_item = Grocery_Item(item_name, item_price)
        shopping_list.add_grocery_item(grocery_item)
        # print(shopping_list.grocery_items)

    elif choice == "quit":
        break
    



# unit tests test our clases, NEVER WAIT FOR USER INPUT
# CREATE A SEPERATE FILE GROCERY_TEST_PY and write all opur tests

# remove items
# don't add same items
# delete a list