import doctest
from typing import Union


class Rectangle:
    def __init__(self, length: Union[int, float], width: Union[int, float], color: str):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param length: Длина фигуры
        :param width: Ширина фигуры
        :param color: Цвет фигуры

        Примеры:
        >>> rectangle = Rectangle(10, 5, "red") # инициализация экземпляра класса
        """
        self.color = None

        if not isinstance(length, (int, float)):
            raise TypeError("Длина фигуры должна быть int или float")
        if length <= 0:
            raise ValueError("Длина прямоугольника должна быть положительным числом")

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина прямоугольника должна быть int или float")
        if width <= 0:
            raise ValueError("Ширина прямоугольника должна быть положительным числом")

        self.length = length
        self.width = width
        self.init_color(color)

    def calculate_area(self):
        """
        Функция, которая вычисляет площадь прямоугольника
        :return: Площадь прямоугольника

        Примеры:
        >>> rectangle = Rectangle(50, 10, "red")
        >>> rectangle.calculate_area()
        """
        ...

    def calculate_perimeter(self):
        """
        Функция, которая вычисляет периметр прямоугольника
        :return: Периметр прямоугольника

        Примеры:
        >>> rectangle = Rectangle(50, 10, "red")
        >>> rectangle.calculate_perimeter()
        """
        ...

    def init_color(self, color: str):
        if not isinstance(color, str):
            raise TypeError("Цвет прямоугольника должен быть str")

        self.color = color


class Employee:
    def __init__(self, name: str, position: str, salary: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Сотрудник"

        :param name: Имя сотрудника
        :param position: Должность сотрудника
        :param salary: Зарплата сотрудника, $

        Примеры:
        >>> employee = Employee("John", 'Builder', 500) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя сотрудника должно быть str")

        if not isinstance(position, str):
            raise TypeError("Должность сотрудника должна быть str")

        if not isinstance(salary, (int, float)):
            raise TypeError("Зарплата сотрудника должна быть int или float")
        if salary <= 0:
            raise ValueError("Зарплата не может быть меньше 0 или отрицательная")

        self.name = name
        self.position = position
        self.salary = salary

    def is_working(self):
        """
        Функция которая проверяет, работает ли сотрудник (Если есть должность и есть зарплата, то он работает)

        :return: Работает ли сотрудник

        Примеры:
        >>> employee = Employee("John", 'Builder', 500)
        >>> employee.is_working()
        """
        ...

    def get_raise(self, bonus_salary: Union[int, float]) -> None:
        """
            Повышение уровня заработной платы.
            :param bonus_salary: Размер прибавки к зарплате

            :raise ValueError: Если количество добавляемой жидкости меньше или равно 0, то вызываем ошибку

             Примеры:
            >>> employee = Employee("John", 'Builder', 500)
            >>> employee.get_raise(200)
            """
        if not isinstance(bonus_salary, (int, float)):
            raise TypeError("Прибавка к зарплате должна быть int или float")
        if bonus_salary <= 0:
            raise ValueError("Прибавка к зарплате должна быть больше 0")
        ...


class Vehicle:
    def __init__(self, company: str, model: str, year: int, engine_status: str):
        """
                Создание и подготовка к работе объекта "Транспортное средство"

                :param company: Название производителя
                :param model: Модель автомобиля
                :param year: Год выпуска автомобиля
                :param engine_status: Статус работы двигателя (включен или выключен), задается "On" или "Off"

                Примеры:
                >>> car = Vehicle("Ford", "Focus", 2012, "On") # инициализация экземпляра класса
                """
        if not isinstance(company, str):
            raise TypeError("Компания должна быть str")

        if not isinstance(model, str):
            raise TypeError("Модель должна быть str")

        if not isinstance(year, int):
            raise TypeError("Год должен быть целым числом")
        if not (1950 <= year <= 2024):
            raise ValueError("Год выпуска должен быть в диапазоне от 1950 года до 2024 года")

        if not isinstance(engine_status, str):
            raise ValueError("Статус двигателя должен быть str")
        if (engine_status != "On") and (engine_status != "Off"):
            raise ValueError("Двигатель должен быть либо запущен (On), либо выключен (Off)")

        self.company = company
        self.model = model
        self.year = year
        self.engine_status = engine_status

    def start_engine(self):
        """"
               Функция включает двигатель, если тот был выключен,
               в случае успеха выводится сообщение (двигатель включен).
               :raise ValueError: вызывает ошибку, если двигатель был выключен при вызове метода
               Примеры:
               >>> car = Vehicle("Ford", "Focus", 2012, "Off")
               >>> car.start_engine()
               """
        ...

    def stop_engine(self):
        """"
               Функция выключает двигатель, если тот был включен,
               в случае успеха выводится сообщение (двигатель включен).
               :raise ValueError: вызывает ошибку, если двигатель был включен при вызове метода
               Примеры:
               >>> car = Vehicle("Ford", "Focus", 2012, "On")
               >>> car.stop_engine()
               """
        ...


if __name__ == "__main__":
    pass
    doctest.testmod()
