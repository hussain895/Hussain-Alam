# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# total = 0

# for i in range(1, 4):
#     while True:
#         price = input(f"Enter price of item {i}: ")
#         try:
#             price = float(price)
#             if price < 0:
#                 print("Price can't be negative. Try again.")
#             else:
#                 total += price
#                 break
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# print(f"\nTotal before discount: ${total:.2f}")

# discount = input("Do you have a membership card for 10% off? (yes/no): ").lower()

# if discount == "yes":
#     total *= 0.9
#     print("10% discount applied!")

# print(f"Final total: ${total:.2f}")
# print("Thank you for shopping!")


# library = ["Harry Potter", "The Hobbit", "Pride and Prejudice"]

# while True:
#     print("\n1. Add Book")
#     print("2. Check Book")
#     print("3. Remove Book")
#     print("4. Show Books")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         book = input("Enter book name: ")
#         if book in library:
#             print("Book already exists.")
#         else:
#             library.append(book)
#             print("Book added.")

#     elif choice == "2":
#         book = input("Enter book name to check: ")
#         if book in library:
#             print("Book is available.")
#         else:
#             print("Book not found.")

#     elif choice == "3":
#         book = input("Enter book name to remove: ")
#         if book in library:
#             library.remove(book)
#             print("Book removed.")
#         else:
#             print("Book not found.")

#     elif choice == "4":
#         print("Books in library:")
#         for b in library:
#             print("-", b)

#     elif choice == "5":
#         print("Goodbye!")
#         break

#     else:
#         print("Invalid choice! Try again.")


# Employee data: names and their ratings


# employees = {
#     "Alice": 5,
#     "Bob": 4,
#     "Charlie": 3,
#     "David": 2,
#     "Eve": 5
# }

# # Function to determine bonus based on rating
# def calculate_bonus(rating):
#     if rating == 5:
#         return 1000
#     elif rating == 4:
#         return 750
#     elif rating == 3:
#         return 500
#     else:
#         return 0

# # Loop through each employee and print their details
# for name, rating in employees.items():
#     bonus = calculate_bonus(rating)
#     print(f"Employee: {name}, Rating: {rating}, Bonus: ${bonus}")



# Initialize an empty dictionary to store the inventory




inventory = {}

print("Welcome to the Store Inventory System!")
print("Enter items and their quantities. Type 'done' when finished.\n")

# Use a while loop to keep asking for input
while True:
    item_name = input("Enter item name (or type 'done' to finish): ").strip()
    
    # Check if user wants to stop
    if item_name.lower() == "done":
        break
    
    # Get the quantity and make sure it's a valid number
    quantity = input(f"Enter quantity for '{item_name}': ")
    
    # Check if input is a number
    if not quantity.isdigit():
        print("❌ Please enter a valid number for quantity.\n")
        continue

    quantity = int(quantity)
    
    # Add item to the inventory (if already exists, add to existing quantity)
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    
    print(f"✅ Added {quantity} of '{item_name}' to inventory.\n")

# Display final inventory list
print("\n🧾 Final Inventory List:")
print("-" * 30)
for item, qty in inventory.items():
    print(f"{item:<15} : {qty:>5}")
print("-" * 30)
print("Inventory recording complete!")

