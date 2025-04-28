class Books:
    def __init__(self, title, author, published_year,available_copies):
        self.title = title
        self.author = author
        self.published_year = published_year
        self.available_copies = available_copies
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPublished Year: {self.published_year}\nAvailable Copies: {self.available_copies}"    
book=[]
def add_book(title,author,published_year,available_copies):
    book.append(Books(title,author,published_year,available_copies))
    print("Book has been added")
def display_books():
    for i in book:
        print(i)
def borrow_book(title):
    for i in book:
        if i.title==title:
            if i.available_copies>0:
                i.available_copies-=1
                print("Book has been borrowed")
            else:
                print("Book is not available")
def return_book(title):
    for i in book:    
        if i.title==title:
            i.available_copies+=1
            print("Book has been returned")
while True:
    print("1.Add Book")
    print("2.Display Books")
    print("3.Borrow Book")
    print("4.Return Book")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        title=input("Enter title:")
        author=input("Enter author:")        
        published_year=int(input("Enter published year:"))        
        available_copies=int(input("Enter available copies:"))        
        add_book(title,author,published_year,available_copies)
    elif choice==2: 
        display_books()    
    elif choice==3:
        title=input("Enter title:")        
        borrow_book(title)
    elif choice==4:                              
        title=input("Enter title:")        
        return_book(title)
    elif choice==5:                              
        break       
    else:
        print("Invalid choice")                                          