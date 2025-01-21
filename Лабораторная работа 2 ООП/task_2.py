BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param id_: Уникальный идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book(1, "test_name", 300) # инициализация экземпляра класса
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Метод для получения строкового представления книги
        :return: Строковое представление книги

        Примеры:
        >>> book = Book(1, "test_name", 300)
        >>> str(book)
        'Книга "test_name"'
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Метод для получения подробного представления книги
        :return: Строковое представление экземпляра класса Book

        Примеры:
        >>> book = Book(1, "test_name", 300)
        >>> repr(book)
        "Book(id_=1, name='test_name', pages=300)"
        """
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'

class Library:
    def __init__(self, books=None):
        """
        Создание и подготовка к работе объекта "Библиотека"
        :param books: Список объектов Book (по умолчанию пустой список)

        Примеры:
        >>> library = Library() # создание пустой библиотеки
        >>> book = Book(1, "test_name", 300)
        >>> library = Library([book]) # библиотека с одной книгой
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Определение следующего доступного идентификатора книги
        :return: Следующий доступный идентификатор книги

        Примеры:
        >>> library = Library()
        >>> library.get_next_book_id()
        1
        >>> book = Book(1, "test_name", 300)
        >>> library = Library([book])
        >>> library.get_next_book_id()
        2
        """
        if not self.books:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id__):
        """
        Поиск индекса книги в библиотеке по её ID
        :param id__: Идентификатор книги
        :return: Индекс книги в списке books
        :raises ValueError: Если книги с указанным ID нет в библиотеке

        Примеры:
        >>> book = Book(1, "test_name", 300)
        >>> library = Library([book])
        >>> library.get_index_by_book_id(1)
        0
        >>> library.get_index_by_book_id(2)
        Traceback (most recent call last):
        ...
        ValueError: Книги с запрашиваемым ID не существует
        """
        for i, book in enumerate(self.books):
            if id__ == book.id_:
                return i
        raise ValueError("Книги с запрашиваемым ID не существует")

if __name__ == '__main__':
    empty_library = Library()  # создание пустой библиотеки
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # создание библиотеки с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
