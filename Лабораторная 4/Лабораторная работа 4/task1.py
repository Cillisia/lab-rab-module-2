if __name__ == "__main__":
    # Write your solution here
    class Vehicle:
        """
        Базовый класс автомобиля.
        """

        def __init__(self, brand: str, model: str, year: int):
            self.brand = brand
            self.model = model
            self.year = year

        def __str__(self) -> str:
            return f"{self.brand} {self.model} ({self.year})"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r})"

        def start_engine(self) -> str:
            """
            Заводит двигатель.
            """
            return f"{self.brand} {self.model} - двигатель запущен"

        def stop_engine(self) -> str:
            """
            Останавливает двигатель.
            """
            return f"{self.brand} {self.model} - двигатель остановлен"

        def make_sound(self) -> str:
            """
            Производит звук (сигналит).
            """
            return "Beep!"


    class Car(Vehicle):
        """
        Дочерний класс, представляющий легковой автомобиль.
        """

        def __init__(self, brand: str, model: str, year: int, color: str):
            super().__init__(brand, model, year)
            self.color = color

        def __str__(self) -> str:
            return f"{super().__str__()}, Цвет: {self.color}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, color={self.color!r})"

        def make_sound(self) -> str:
            """
            Производит звук (сигналит).
            Данный метод перегружает исходный метод, тк каждый класс автомобилей издает свой звук.
            """
            return "Beep-Boop!"




    class Truck(Vehicle):
        """
        Дочерний класс, представляющий грузовой автомобиль.
        """

        def __init__(self, brand: str, model: str, year: int, max_load: float):
            super().__init__(brand, model, year)
            self._max_load = max_load

        def __str__(self) -> str:
            return f"{super().__str__()}, Максимальная нагрузка: {self._max_load} т"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, max_load={self.max_load!r})"

        @property
        def max_load(self):
            return self._max_load

        @max_load.setter
        def max_load(self, max_load: float):
            """
            Атрибут "макимальная нагрузка" сделан закрытым, чтобы его случайно не изменили извне,
            так как это заводская характеристика грузовика.
            """
            self._max_load = max_load
            
        def load_cargo(self, cargo: float) -> str:
            """
            Загружает груз.
            """
            return f"{self.brand} {self.model} - загружен груз весом {cargo} т"

        def unload_cargo(self) -> str:
            """
            Разгружает груз.
            """
            return f"{self.brand} {self.model} - груз разгружен"

        def make_sound(self) -> str:
            """
            Производит звук (сигналит).
            Данный метод перегружает исходный метод, тк каждый класс автомобилей издает свой звук.
            """
            return "Too-Tooooo!"



    pass
