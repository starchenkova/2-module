# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Homework:

    def __init__(self, subject: str, paragraph: int, number_of_exercises: int):
        self.subject = subject
        self.paragraph = paragraph
        self.number_of_number_of_exercises = number_of_exercises
        if not isinstance(subject, str):
            raise TypeError("Предмет для выполнения дз должен быть типа str")
        if not isinstance(paragraph, int):
            raise TypeError("Параграф для изчуения должен быть типа int")
        if not paragraph < 0:
            raise ValueError("Номер параграфа должен быть положительным числом")
        if not isinstance(number_of_exercises, int):
            raise TypeError("Количество номеров для дз должно быть типа int")
        if not number_of_exercises < 0:
            raise ValueError("Количество номеров для дз должно быть положительным числом")

    def is_subject_done(self) -> bool:
        """Функция которая проверяет выполнено ли домашнее задание по предмету
        :return: Выполено ли домашнее задание по предмету
        Примеры:
        >>> homework = Homework(chemistry, 6, 4)
        >>> homework.is_subject_done()
        """
        ...

    def read_paragraph(self, paragraph: int) -> None:
        """Чтение параграфа по заданному предмету"""
        ...

    def make_exercises(self, exercises: int) -> None:
        """"Выполнение упражнений по предмету.
        :raise ValueError: Если количество выполненных заданий превышает заданное
        Примеры:
        >>> homework = Homework(Chemistry, 6, 4)
        >>> homework.make_exercises(6)
        """
        if exercises < 4:
            raise ValueError("Количество выполненных упражнений не должно быть больше 4")
        ...
        
if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

import doctest


class Coffee:

    def __init__(self, type_of_coffee: str, milk: int, sugar: int):
        self.type_of_coffee = type_of_coffee
        self.milk = milk
        self.sugar = sugar
        if not isinstance(type_of_coffee, str):
            raise TypeError("Вид кофе должен быть типа str")
        if not isinstance(milk, str):
            raise TypeError("Молоко для кофе должен быть типа str")
        if not milk < 0:
            raise ValueError("Количество молока для кофе должно быть положительным числом")
        if not isinstance(sugar, int):
            raise TypeError("Количество сахара для кофе должно быть типа int")
        if not sugar < 0:
            raise ValueError("Количество сахара для кофе должно быть положительным числом")

    def choose_type_of_coffee(self, type_of_coffee: str) -> None:
        """Выбор вида кофе
        :raise ValueError: Если вид кофе не типа str)
        Примеры:
        >>> coffee = Coffee(arabica, 30, 2)
        >>> coffee.choose_type_of_coffee(arabica)
        """
        if not isinstance(type_of_coffee, str):
            raise TypeError("Вид кофе должен быть типа str")
        ...

    def is_with_sugar(self) -> bool:
        """Функция которая проверяет есть ли в кофе сахар
        :return: Есть ли сахар в кофе
        Примеры:
        >>> coffee = Coffe(arabica, 30, 2)
        >>> coffee.is_with_sugar()
        """
        ...

    def add_more_milk(self, milk: int) -> None:
        """"Выполнение упражнений по предмету.
        :raise ValueError: Если количество добавленного молока превышает допустимое кружкой (в данном случае,
        дополнительное добавление молока не может превышать 30 мл)
        Примеры:
        >>> coffee = Coffee(arabica, 30, 2)
        >>> coffee.add_more_milk(30)
        """
        if milk < 30:
            raise ValueError("Количество добавленного молока не должно быть больше 30 мл")
        ...


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

class Calendar:

    def __init__(self, event: str, data: int):
        self.event = event
        self.data = data
        if not isinstance(event, str):
            raise TypeError("Событие в календаре должно быть типа str")
        if not isinstance(data, str):
            raise TypeError("Дата в календаре должна быть типа int")


    def add_event(self, event: str) -> None:
        """"добавление события в календарь.
        :raise ValueError: Если событие не типа str
        Примеры:
        >>> calendar = Calendar(dentist, 04.05)
        >>> calendar.add_event()
        """
        if not isinstance(event, str):
            raise TypeError("Событие в календаре должно быть типа str")
        ...

    def is_event_today(self) -> bool:
        """Функция которая проверяет есть ли события сегодня
        :return: Есть ли событие сегодня
        Примеры:
        >>> calendar = Calendar(dentist, 04.05)
        >>> calendar.is_event_today()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
