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


library = ["Harry Potter", "The Hobbit", "Pride and Prejudice"]

while True:
    print("\n1. Add Book")
    print("2. Check Book")
    print("3. Remove Book")
    print("4. Show Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        if book in library:
            print("Book already exists.")
        else:
            library.append(book)
            print("Book added.")

    elif choice == "2":
        book = input("Enter book name to check: ")
        if book in library:
            print("Book is available.")
        else:
            print("Book not found.")

    elif choice == "3":
        book = input("Enter book name to remove: ")
        if book in library:
            library.remove(book)
            print("Book removed.")
        else:
            print("Book not found.")

    elif choice == "4":
        print("Books in library:")
        for b in library:
            print("-", b)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")