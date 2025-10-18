from Book import Book


if __name__ == "__main__":
    print("This is Smart Library.")

Book_Crime_and_Punishment = Book("Crime and Punishment", "Fyodor Dostoevsky", "978-0140449136", "Fiction", 10)

ISBN = Book_Crime_and_Punishment.get_ISBN()
print("ISBN:", ISBN)

current_stock = Book_Crime_and_Punishment.get_stock()
print("Current Stock:", current_stock)

print("Changing Stock...")
Book_Crime_and_Punishment.set_stock(15)
print("New Stock Is:", Book_Crime_and_Punishment.get_stock())

print("General Information of the Book:")
print(Book_Crime_and_Punishment)