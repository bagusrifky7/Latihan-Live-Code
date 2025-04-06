print('                                                                 ')
print('Welcome to Zitae Library App!')
print('                                                                 ')
print('                                                                 ')
# Membuat class untuk buku yang diinput

class book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
    
    def __str__(self):
        return f'ISBN: {self.isbn}, {self.title} by {self.author}'

# Membuat class untuk perpustakaanya  
class libraries:
    def __init__(self):
        self.book_list = []
    
    # Fungsi untuk menambah buku ke katalog
    def adding_book(self, isbn, title, author):
        buku = book(isbn, title, author) #storing objek dalam list
        self.book_list.append(buku)

    def remove_book(self, isbn):
        try:
            if not self.book_list: #Jika tidak ada buku sama sekali di dalam katalog
                print('There\'s no books in the catalogue')
            else:
                for bks in self.book_list:
                    if bks.isbn == isbn:
                        print(f'Book {bks.title} with ISBN: {isbn} successfully been removed')
                        self.book_list.remove(bks)
                    else:
                        raise ValueError
                
        except ValueError: # Jika tidak ada buku dengan ISBN yang diinput
            print("There's no books with those ISBN number")
        
    # Digunakan untuk mencari buku berdasarkan penulis    
    def search_by_author(self, author):
        try:
            if not self.book_list: #Jika tidak ada buku di dalam katalog
                print('There\'s no books in the catalogue')

            else:
                for bks in self.book_list:
                    if bks.author.lower() == author.lower():
                        print(f'ISBN: {bks.isbn}, Title: {bks.title}')
                    
                    else: 
                        raise NameError
                        
        # Jika tidak ada buku dengan penulis yang diinput
        except NameError:
            print('There\'s no book with that title')
    
    # Digunakan untuk display katalog
    def display_book(self):
        if not self.book_list: # Jika tidak ada buku sama sekali di katalog
            print('There\'s no books added yet')
        else:
            for index, bks in enumerate(self.book_list):
                print(f'{index + 1}. {bks}')
    
    def running_app(self):
        while True:
            print('Menu:')
            print('1. Adding book to library')
            print('2. Remove book from library')
            print('3. Display books catalogue')
            print('4. Search book by author')
            print('5. Exit')
            print('                                                                  ')
            pilihan = input('Pilihan: ') # Input pilihan menu
            try:
                if pilihan == '1':
                    try:
                        isbn = int(input('Input ISBN numbers: '))
                        title = input('Input book title: ')
                        author = input('Input author of the book: ')
                        self.adding_book(isbn, title, author)
                        print(f'{title} by {author} with ISBN {isbn} successfully added')
                    
                    except ValueError:
                        print('Input invalid')

                elif pilihan == '2':
                    try:
                        isbn = int(input('Input book ISBN: '))
                        self.remove_book(isbn)
                    
                    except ValueError:
                        print('Please input numbers only')
                
                elif pilihan == '3':
                    self.display_book()
                
                elif pilihan == '4':
                    author = input('Author of the books: ')
                    self.search_by_author(author)
                
                elif pilihan == '5':
                    print('Thank you and have a nice day')
                    break

                else: # Jika input-an dari user salah
                    raise ValueError
            
            except ValueError:
                print('Error: Menu\'s not available')
            
            print('                                                                    ')

#Jalakan aplikasi
if __name__ == '__main__':
    app_perpus = libraries()
    app_perpus.running_app()
    