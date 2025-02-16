if __name__ == "__main__":
    class ElectronicDevice:


        def __init__(self, brand: str, model: str, battery_capacity: int) -> None:
            """Базовый класс для представления электронных устройств.

            Атрибуты:
                brand (str): Бренд устройства
                model (str): Модель устройства
                battery_capacity (int): Максимальная емкость аккумулятора (mAh)
                _current_battery (int): Текущий заряд аккумулятора (инкапсулирован)
            """

            self.brand = brand
            self.model = model
            self.battery_capacity = battery_capacity
            self._current_battery = battery_capacity  # Инкапсуляция для контроля заряда

        def __str__(self) -> str:
            return f"{self.brand} {self.model} ({self._current_battery}/{self.battery_capacity}mAh)"

        def __repr__(self) -> str:
            return f"ElectronicDevice({self.brand}, {self.model}, {self.battery_capacity})"

        def charge(self, amount: int) -> None:
            """Заряжает устройство на указанное количество mAh"""
            self._current_battery = min(self._current_battery + amount, self.battery_capacity)

        def get_remaining_battery(self) -> float:
            """Возвращает процент оставшегося заряда

            Примеры:
            >>> device = ElectronicDevice("Brand", "Model", 3000)
            >>> device.get_remaining_battery()
            100.0
            """
            return (self._current_battery / self.battery_capacity) * 100


    class Smartphone(ElectronicDevice):
        """
        Класс смартфона с расширенной функциональностью.

            :param screen_size: Диагональ экрана в дюймах

            Наследует:
                :class:`ElectronicDevice`
        """

        def __init__(self, brand: str, model: str, battery_capacity: int, screen_size: float) -> None:
            super().__init__(brand, model, battery_capacity)
            self.screen_size = screen_size

        def __str__(self) -> str:
            base_str = super().__str__()
            return f"{base_str} | Screen: {self.screen_size}\""

        def make_call(self, duration: int) -> None:
            """
            Совершает звонок с расходом батареи

            :param duration: Длительность звонка в минутах
            :raise ValueError: Если длительность меньше или равна 0

            Примеры:
            >>> phone = Smartphone("Xiaomi", "Xiaomi 14", 3500, 6.3)
            >>> phone.make_call(5)
            """
            self._current_battery -= duration * 10  # 10 mAh в минуту


    class Laptop(ElectronicDevice):
        """
        Класс ноутбука с расширенной функциональностью.

        :param ram_size: Объем оперативной памяти (GB)

        Наследует:
            :class:`ElectronicDevice`
        """

        def __init__(self, brand: str, model: str, battery_capacity: int, ram_size: int) -> None:
            super().__init__(brand, model, battery_capacity)
            self.ram_size = ram_size

        def __repr__(self) -> str:
            return f"Laptop({self.brand}, {self.model}, {self.battery_capacity}, {self.ram_size}GB)"

        def perform_computation(self, intensity: int) -> None:
            """
            Выполняет ресурсоемкие вычисления

            :param intensity: Уровень интенсивности вычислений (1-10)
            :raise ValueError: Если интенсивность вне диапазона 1-10

            Примеры:
            >>> laptop = Laptop("Dell", "XPS 15", 8000, 32)
            >>> laptop.perform_computation(7)
            """
            self._current_battery -= intensity * self.ram_size * 5  # Индивидуальная логика расхода
    pass
