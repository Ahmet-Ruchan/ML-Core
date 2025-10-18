# First of all create a class name Book with the following attributes:
# Book: title, author, ISBN, category, stock

class Book:

    def __init__(self, title, author, ISBN, category, stock):
        self.title = title
        self.author = author
        self.__ISBN = ISBN # International Standard Book Number
        self.category = category
        self.__stock = stock

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.__ISBN}, Category: {self.category}, Stock: {self.__stock}"

    def get_stock(self):
        return self.__stock

    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            print("Stock Cannot Be Negative.")

    def get_ISBN(self):
        return self.__ISBN

    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN
