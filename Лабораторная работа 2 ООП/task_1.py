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


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание объекта Book.
        :param id_: Уникальный идентификатор
        :param name: Название
        :param pages: Страницы

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


if __name__ == '__main__':

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
