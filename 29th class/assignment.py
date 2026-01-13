books = {
    "The Great Gatsby": 15.99,
    "To Kill a Mockingbird": 12.49,
    "1984": 10.99,
    "Pride and Prejudice": 9.99,
    "Moby Dick": 8.99
}

books_backup = books.copy()

for title, price in books.items():
    print(title, ":", price)
print("\n")
print("Total value:", sum(books.values()))

sold_book = books.pop("1984")
print("Sold:", "1984 for", sold_book)
print("\n")

print("Updated inventory:\n", books)
