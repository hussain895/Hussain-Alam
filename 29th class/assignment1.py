inventory = {
    "Laptop": 10,
    "Smartphone": 25,
    "Tablet": 15,
    "Headphones": 30,
    "Smartwatch": 20
}

inventory["Smartphone"] += 10
inventory["Headphones"] += 5

item, qty = inventory.popitem()
print("Sold Last Item:", item, "Quantity:", qty)

print("Camera stock:", inventory.get("Camera", "Out of Stock"))

print("Inventory now:", inventory)
