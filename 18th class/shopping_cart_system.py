cart = []

while True:
    print("\n1. Add item\n2. Remove item\n3. View cart\n4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        item = input("Enter item to add: ")
        cart.append(item)

    elif choice == '2':
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
        else:
            print("Item not found.")

    elif choice == '3':
        print("Your cart contains:", cart)

    elif choice == '4':
        break

    else:
        print("Invalid choice!")


sorted_cart = sorted(cart, key=str.lower)
print("\nFinal sorted cart items:", sorted_cart)

count = {}
for item in cart:
    count[item] = count.get(item, 0) + 1

print("Item counts:", count)

total_items = sum(count.values())
print("Total items in cart:", total_items)







