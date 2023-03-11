class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.age_in_months = age * 12

    def celebrate_birthday(self):
        self.age += 1
        self.age_in_months += 12

    def change_name(self, new_name):
        self.name = new_name


person = Person("Alice", 30)
print(person.age)  # outputs: 30
print(person.age_in_months)  # outputs: 360

person.celebrate_birthday()
print(person.age)  # outputs: 31
print(person.age_in_months)  # outputs: 372

person.change_name("Bob")
print(person.name)  # outputs: "Bob"


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class LibraryCatalog:
    def __init__(self, books=None):
        self.books = books or []

    def __str__(self):
        catalog_str = ""
        for book in self.books:
            catalog_str += f"{book.title} by {book.author}\n"
        return catalog_str

catalog = LibraryCatalog([Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565"),
                          Book("To Kill a Mockingbird", "Harper Lee", "9780446310789")])
print(catalog)
