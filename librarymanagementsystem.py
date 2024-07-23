class library():
    def __init__(self,name="nil"):
        self.name=name
        self.books=[]

    def add(self,book):
        self.books.append(book)
        print(f"Book {book} has been added to the library")
    def list_books(self):
        if not self.books:
            print("there is no books in the library")
        else:
            print("books in the library are:")
            for book in self.books:
                print(f"-{book}")
my_library=library("my local library")
my_library.add("harry potter part 1")
my_library.add("harry potter part 2")
my_library.add("harry potter part 3")
my_library.add("harry potter part 4")
print(my_library.list_books())