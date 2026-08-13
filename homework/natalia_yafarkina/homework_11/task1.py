class Book:
    page_material = 'бумага'
    is_presence_text = True

    def __init__(self, book_title, author, number_pages, isbn, is_reserved):
        self.book_title = book_title
        self.author = author
        self.number_pages = number_pages
        self.isbn = isbn
        self.is_reserved = is_reserved


class StudyBook(Book):
    is_tasks = True

    def __init__(self, book_title, author, number_pages, isbn, is_reserved, subject, degree_class):
        super().__init__(book_title, author, number_pages, isbn, is_reserved)
        self.subject = subject
        self.degree_class = degree_class


book_1 = Book('Мастер и Маргарита', 'Михаил Булгаков', 480, '978-5-699-12014-7', False)
book_2 = Book('Преступление и наказание', 'Федор Достоевский', 608, '978-5-389-04917-8', False)
book_3 = Book('Три товарища', 'Эрих Мария Ремарк', 480, '978-5-17-062836-0', False)
book_4 = Book('Маленький принц', 'Антуан де Сент-Экзюпери', 112, '978-5-699-92305-2', False)
book_5 = Book('Отцы и дети', 'Иван Тургенев', 288, '978-5-389-04479-1', False)
book_1.is_reserved = True
book_3.is_reserved = True

if book_1.is_reserved:
    print(f'Название: {book_1.book_title}, Автор: {book_1.author}, страниц: {book_1.number_pages}, зарезервирована')
else:
    print(f'Название: {book_1.book_title}, Автор: {book_1.author}, страниц: {book_1.number_pages}')

if book_2.is_reserved:
    print(f'Название: {book_2.book_title}, Автор: {book_2.author}, страниц: {book_2.number_pages}, зарезервирована')
else:
    print(f'Название: {book_2.book_title}, Автор: {book_2.author}, страниц: {book_2.number_pages}')

if book_3.is_reserved:
    print(f'Название: {book_3.book_title}, Автор: {book_3.author}, страниц: {book_3.number_pages}, зарезервирована')
else:
    print(f'Название: {book_3.book_title}, Автор: {book_3.author}, страниц: {book_3.number_pages}')

if book_4.is_reserved:
    print(f'Название: {book_4.book_title}, Автор: {book_4.author}, страниц: {book_4.number_pages}, зарезервирована')
else:
    print(f'Название: {book_4.book_title}, Автор: {book_4.author}, страниц: {book_4.number_pages}')

if book_5.is_reserved:
    print(f'Название: {book_5.book_title}, Автор: {book_5.author}, страниц: {book_5.number_pages}, зарезервирована')
else:
    print(f'Название: {book_5.book_title}, Автор: {book_5.author}, страниц: {book_5.number_pages}')

study_book_1 = StudyBook('геометрия', 'Михаил Иванов', 250, '978-5-699-12014-1', False, 'геометрия', 7)
study_book_2 = StudyBook('физика', 'Александр Перышкин', 250, '978-5-699-12014-2', False, 'физика', 7)
study_book_3 = StudyBook('алгебра', 'Михаил Иванов', 250, '978-5-699-12014-3', False, 'алгебра', 7)
study_book_1.is_reserved = True
study_book_3.is_reserved = True

if study_book_1.is_reserved:
    print(f'Название: {study_book_1.book_title}, Автор: {study_book_1.author}, страниц: {study_book_1.number_pages},'
          f' предмет: {study_book_1.subject}, класс: {study_book_1.degree_class}, зарезервирована')
else:
    print(f'Название: {study_book_1.book_title}, Автор: {study_book_1.author}, страниц: {study_book_1.number_pages},'
          f' предмет: {study_book_1.subject}, класс: {study_book_1.degree_class}')

if study_book_2.is_reserved:
    print(f'Название: {study_book_2.book_title}, Автор: {study_book_2.author}, страниц: {study_book_2.number_pages},'
          f' предмет: {study_book_2.subject}, класс: {study_book_2.degree_class}, зарезервирована')
else:
    print(f'Название: {study_book_2.book_title}, Автор: {study_book_2.author}, страниц: {study_book_2.number_pages},'
          f' предмет: {study_book_2.subject}, класс: {study_book_2.degree_class}')

if study_book_3.is_reserved:
    print(f'Название: {study_book_3.book_title}, Автор: {study_book_3.author}, страниц: {study_book_3.number_pages},'
          f' предмет: {study_book_3.subject}, класс: {study_book_3.degree_class}, зарезервирована')
else:
    print(f'Название: {study_book_3.book_title}, Автор: {study_book_3.author}, страниц: {study_book_3.number_pages},'
          f' предмет: {study_book_3.subject}, класс: {study_book_3.degree_class}')
