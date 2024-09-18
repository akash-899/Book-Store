# entity: Book,user,library

# functionalities: adding user,adding book,borrow,return

class Book:

    def __init__(self,cat,id,name,quantity) -> None:
        self.id = id
        self.name = name
        self.cat = cat
        self.quantity = quantity

class User:

    def __init__(self,id,name,password) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.borrowedBooks = []

class Library:

    def __init__(self,owner,name) -> None:
        self.owner = owner
        self.name = name
        self.books = []
        self.users = []
        self.returnedBooks = []


    def addBook(self,cat,id,name,quantity):
        book = Book(cat,id,name,quantity)
        self.books.append(book)
        print(f"\n\t{name} Book added successfully ! ")


    def addUser(self,id,name,password):
        user = User(id,name,password)
        self.users.append(user)
        return user
    
    def showUsers(self):
        if len(self.users) == 0:
            print("\n\tNo users available.")
            return
        print("\n\tUsers List: ")
        for user in self.users:
            print(f"\tID: {user.id}, Name: {user.name}")

    def showBooks(self):
        if len(self.books) == 0:
            print("\n\tNo books available.")
            return
        print("\n\tBooks List: ")
        for book in self.books:
            print(f"\tID: {book.id}, Name: {book.name}, Category: {book.cat}, Quantity: {book.quantity}")
    
    def borrowBook(self,user,id):

        for book in self.books:
            if book.id == id:
                if book in user.borrowedBooks:
                    print("\n\tAlready Borrowed ! ")
                    return
                elif book.quantity < 1:
                    print("\n\tNo available copies ! ")
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quantity -= 1
                    print(f"\n\t{book.name}  borrowed successfully ! ")
                    return
        

        print(f"\n\tBook not found ! ")
    
    def returnBook(self, user, id):
        for book in user.borrowedBooks:
            if book.id == id:
                user.borrowedBooks.remove(book)
                book.quantity += 1
                self.returnedBooks.append(book)
                print(f"\n\t{book.name} returned successfully!")
                return
        print(f"\n\tBook not found in your borrowed list!")

    def showBorrowedBooks(self, user):
        if len(user.borrowedBooks) == 0:
            print("\n\tNo books borrowed.")
        else:
            print("\n\tBorrowed Books List: ")
            for book in user.borrowedBooks:
                print(f"\tID: {book.id}, Name: {book.name}")

    def showReturnedBooks(self):
        if len(self.returnedBooks) == 0:
            print("\n\tNo returned books.")
        else:
            print("\n\tReturned Books List: ")
            for book in self.returnedBooks:
                print(f"\tID: {book.id}, Name: {book.name}")
                 



pl = Library("NEO","PHITRON LIBRARY")
admin = pl.addUser(1,'admin','admin')
rahim = pl.addUser(2,'rahim','1234')
pybook = pl.addBook('Sci-Fi',15,'Dune',5)


run = True
currentUser = admin

while run:

    if currentUser == None:
         print(f"\n\tNo logged in user ! ")

         option = input("Login ? Registration (L/R): ")

         if option == 'R':
             id = int(input("\tEnter id: "))
             name = input("\tEnter Name: ")
             password = input("\tEnter password: ")

             user = pl.addUser(id,name,password)
             currentUser = user

         elif option == 'L':
             id = int(input("\tEnter id: "))
             password = input("\tEnter password: ")

             match = False
             for user in pl.users:
                 if user.id == id and user.password == password:
                     currentUser = user
                     match = True
                     break
             
             if match == False:
                 print(f"\n\tNo user found ! ")

    else:

        if currentUser.name == 'admin':

            print("options: \n")

            print("1 : Add Book")
            print("2 : Show Users")  
            print("3 : Show Books")
            print("4 : Logout")

            ch = int(input("\nEnter option: "))

            if ch == 1:
                cat = input("\tEnter cat: ")
                id = int(input("\tEnter id: "))
                name = input("\tEnter Name: ")
                quantity = int(input("\tEnter quantity: "))

                pl.addBook(cat,id,name,quantity)
            elif ch == 2:
                pl.showUsers()

            elif ch == 3:
                pl.showBooks()

            elif ch == 4:
                currentUser = None

        else:
             print("options: \n")

             print("1 : Borrow Book")
             print("2 : Return Book")  
             print("3 : Show Books")
             print("4 : Show Borrowed Books")
             print("5 : Show Returned Books")
             print("6 : Logout")

             ch = int(input("\nEnter option: "))   

             if ch == 1:
                 id = int(input("\tEnter id: "))
                 pl.borrowBook(currentUser,id)
             elif ch == 2:
                id = int(input("\tEnter id: "))
                pl.returnBook(currentUser, id)
             elif ch == 3:
                 pl.showBooks()
             elif ch == 4:
                pl.showBorrowedBooks(currentUser)

             elif ch == 5:
                pl.showReturnedBooks()

             elif ch == 6:
                currentUser = None

             
        

                 

        
        
                      




