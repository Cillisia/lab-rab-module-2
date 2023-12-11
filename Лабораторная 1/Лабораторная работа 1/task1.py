# TODO Написать 3 класса с документацией и аннотацией типов
class Student:
    def __init__(self, age: int, course: int):
        """
        Конструктор класса Table.

        :param age: Возраст студента.
        :param course: Курс обучения.
        """
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целыым числом")
        if age <= 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.age = age

        if not isinstance(course, int):
            raise TypeError("Курс должен быть целыым числом")
        if course <= 0 and course >= 7:
            raise ValueError("Такого курса быть не может")
        self.course = course
    def expel_from_university(self):
        """
        Метод для отчисления студента.
        :return: None
        """
        ...
    def upgrade_course(self):
        """
        Метод для перевода студента на следующий курс.
        :return: None
        """
        ...


class Table:
    def __init__(self, material: str, color: str):
        """
        Конструктор класса Table.

        :param material: Материал стола.
        :param color: Цвет стола.
        """
        self.material = material
        self.color = color

    def change_color(self, new_color: str) -> None:
        """
        Метод для изменения цвета стола.

        :param new_color: Новый цвет стола.
        :return: None
        >>>table.change_color("белый")
        """
        ...
    def cut_legs(self, num_of_legs:int) -> None :
        if num_of_legs <= 0:
            raise ValueError("Невозможное количество ножек")
        """
        Метод для уменьшения количества ножек стола на заданное количество.

        :param num_of_legs: Новый цвет стола.
        :return: None
        """
        ...


class Tree:
    def __init__(self, species: str, age: int):
        """
        Конструктор класса Tree.

        :param species: Вид дерева.
        :param age: Возраст дерева.
        """
        self.species = species
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целыым числом")
        if age <= 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.age = age

    def grow(self, years: int) -> None:
        """
        Метод для увеличения возраста дерева на заданное количество лет.

        :param years: Количество лет.
        :return: None
        >>>tree.grow(10)
        """
        ...
    def drop_leaves(self) -> None:
        """
        Метод для сбрасывания листвы с дерева.

        :return: None
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass
