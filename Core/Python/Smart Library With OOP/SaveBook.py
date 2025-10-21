from Book import Book

class SaveBook(Book):

    def __init__(self, title="", author="", ISBN="", category="", stock=0):
        super().__init__(title, author, ISBN, category, stock)

    def save_book_info(self):

        self.books = []
        how_many = 0
        print("How Many Books Do You Want to Save?")
        how_many = int(input())

        for i in range(how_many):

            print(f"Book {i+1}, Please Enter Book Information to Save:")
            self.title = input("Title: ")
            self.author = input("Author: ")
            self.__ISBN = input("ISBN: ")
            self.category = input("Category: ")
            self.__stock = int(input("Stock: "))

            book = SaveBook(self.title, self.author, self.__ISBN, self.category, self.__stock)
            self.books.append(book)

    def display_saved_books(self):
        for i in self.books:
            print("Saved Book:", i) # __str__ method will be called here

        print("Books Saved Successfully.")

