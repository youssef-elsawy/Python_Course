class Book:
    def __init__(self,title:str, author:str, isbn:str, checked_out:bool):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.checked_out=checked_out
    def check_out(self):
        if self.checked_out ==False:
            print("book successfully checked out")
            self.checked_out=True
        else: print("book is already checked out")
    def check_in(self):
        if self.checked_out ==True:
            print("book successfully checked in")
            self.checked_out=False
        else: print("book is already checked in")  
    def display_info(self):
        print(f"Title: {self.title} Author: {self.author} isbn: {self.isbn} Status: {"Available" if self.checked_out==False else "Not Available"}")

class Customer:
    def __init__(self,name:str, customer_id:str):
        self.name=name
        self.customer_id=customer_id
        
        self.checked_out_books=[]
    def check_out_book(self, book_instance):
        if book_instance.checked_out==False:
            self.checked_out_books.append(book_instance)
            print(f"customer with name: {self.name} and ID: {self.customer_id} got the book: {book_instance.title}")
            book_instance.checked_out=True
        else: print("book is already checked out")
    def display_info(self):
        print(f"customer with name: {self.name} and ID: {self.customer_id} has the following books:")  
        for book in self.checked_out_books:
            print(f"- {book.title}") 

class Library(Customer):
    def __init__(self):
        self.books = []
        self.customers = []

    def add_book(self,book_instance):
        self.books.append(book_instance)
    
    def add_customer(self,customer_instance):
        self.customers.append(customer_instance)
    
    def display_books(self):
        for i in self.books:
            print(i.title)
    
    def display_customers(self):
        for j in self.customers:
            print(j.name)
    
    #             check_in_book(customer_id, isbn): Checks in a book from a customer.
    def check_out_book(self,customer_id, isbn):
        for book in self.books:
            if book.isbn==isbn:
                self.check_out_book(book)

#########################################################################################
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565",True)
book2 = Book("1984", "George Orwell", "9780451524935",False)
customer1 = Customer("Alice Smith", "C001")
customer2 = Customer("Bob Johnson", "C002")
customer1.check_out_book(book1)
customer1.check_out_book(book2)
customer2.check_out_book(book2)
customer1.display_info()
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_customer(customer1)
library.add_customer(customer2)
library.display_books()
library.display_customers()
library.check_out_book("C001", "9780743273565")