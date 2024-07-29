class Book:
    page_material = 'paper'
    text_existing = True

    def __init__(self, title, author, pages, isbn, flag_reservation=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.flag_reservation = flag_reservation


class SchoolBook(Book):

    def __init__(self, title, author, pages, isbn, flag_reservation, subject, grade, exercise_flag=False):
        super().__init__(title, author, pages, isbn, flag_reservation)
        self.subject = subject
        self.grade = grade
        self.exercise_flag = exercise_flag


library = [Book('Love of Life', 'Jack London', 64, '978-1-55547-685-3'),
           Book('The Mysterious Stranger', 'Mark Twain', 96, '978-0-486-27020-7'),
           Book('Jonathan Livingston Seagull', 'Richard Bach', 144, '978-0-7432-5387-9', True),
           Book('Stranger to the Ground', 'Richard Bach', 192, '978-0-440-20327-4'),
           Book('The Word Processor of the Gods', 'Stephen King', 20, '978-0-452-25879-8')]

school_library = [SchoolBook(
    'Principles of Mathematics', 'Marian Small', 552, '978-0176675022', False, 'Math', 10, True),
    SchoolBook('Realms, Regions, and Concepts', 'Harm J. de Blij', 544, '978-0470382585', False, 'Geography', 9),
    SchoolBook('Science in Action', 'Irwin Publishing', 720, '978-0774123030', True, 'Science', 11, True)]

print('Library:')
for book in library:
    reservation_status = ', this book is reserved' if book.flag_reservation else ''

    print(f'Book title: {book.title}, Author: {book.author}, pages: {book.pages}, material: {book.page_material}'
          f'{reservation_status}')

print('\nSchool library:')
for school_book in school_library:
    reservation_status = ', this book is reserved' if school_book.flag_reservation else ''
    exercise_status = ', this book has exercises' if school_book.exercise_flag else ''

    print(f'Book title: {school_book.title}, Author: {school_book.author}, pages: {school_book.pages}, '
          f'subject: {school_book.subject}, grade: {school_book.grade}'
          f'{exercise_status}{reservation_status}')
