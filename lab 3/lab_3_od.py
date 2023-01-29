class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError('значение name должно соответствовать типу str')
        self._name = name
        if not isinstance(author, str):
            raise TypeError('значение author должно соответствовать типу str')
        self._author = author

    @property
    def name(selfself):
        return self._name

    @property
    def author(selfself):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages,int):
            raise TypeError('значение pages должно соответствовать типу int')
        if not pages > 0:
            raise ValueError("значение pages должно быть положительным")
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        super_repr = super().__repr__()
        return f'{super_repr}'

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError('значение duration должно соответствовать типу float')
        if not duration > 0:
            raise ValueError("значение duration должно быть положительным")
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        super_repr = super().__repr__()
        return f'{super_repr}'