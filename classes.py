class Library:
    def __init__(self):
        self.Books = ['Book1','Book2','Book3','Book4','Book5','Book6','Book7','Book8', 'Book9', 'Book10', 'Book11', 'Book12', 'Book13']

    def ListAvailableBooks(self):
        print ('Currently available books are:')
        print (self.Books)


Library1 = Library()
Library1.ListAvailableBooks()

def Enquiry(lis1):
    if not lis1:
        return 1
    else:
        return 0

returningBook = ''

def CheckIfBookIsAvailable (Book):
    if Library1.Books.count(Book) == 0:
        return 0
    else:
        return 1


class Customer:
    BorrowedBooks = []

    def BorrowBook(self):
        BorrowedBook = input('Which Book Do You want to Borrow:')
        if CheckIfBookIsAvailable(BorrowedBook):
            print ('You have borrowed ' + BorrowedBook)
            Library1.Books.remove(BorrowedBook)
            Customer.BorrowedBooks.append(BorrowedBook)
        else:
            print ('No Such Book Was Found Please Check The List of Available books to choose one that is available or check if you have already borrowed it or not')
    def ListBorrowedBooks(self):
        print ('Borrowed Books Are:')
        print (Customer.BorrowedBooks)
    def ReturnBooks(self):
        if Enquiry(Customer.BorrowedBooks):
            pass
        else:
            returningBook = ''
            returningBook = input('Which Book Do You Want to Return:')
        Customer.BorrowedBooks.remove(returningBook)
        Library1.Books.append(returningBook)
        print ('You have returned ' + returningBook)


Customer1 = Customer()

def UserInputSystem():
    QuitProgram = False
    while QuitProgram == False:
        UserInput = input(
            'Type Borrow to Borrow a book or Return to Return a book or List to see all available books or ListB to see all Borrowed books Type anything else to terminate the program:  ')
        if UserInput == 'Borrow':
            Customer1.BorrowBook()

        elif UserInput == 'List':
            Library1.ListAvailableBooks()

        elif UserInput == 'Return':
            Customer1.ReturnBooks()

        elif UserInput == 'ListB':
            Customer1.ListBorrowedBooks()

        else:
            QuitProgram = True
    else:
        exit()