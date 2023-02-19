if __name__ == "__main__":
    # Write your solution here
    pass
class Carbonated_drinks:
    def __init__(self, name: str, carbonation_level: str, volume: int, producer: str):
        self.carbonation_level = carbonation_level
        self.volume = volume
        self.producer = producer
        self.name = name
        if not isinstance(name, str):
            raise TypeError("Название напитка должно быть типа str")
        if not isinstance(producer, str):
            raise TypeError("Название компании-производителя должно быть типа str")
        if not isinstance(volume, int):
            raise TypeError("Объём жидкости должно быть типа int")
        if not isinstance(carbonation_level, str):
            raise TypeError("Степень насыщения углекислым газом должна быть типа str") #сильногазированная, среднегазированная или слабогазированная

    def __str__(self) -> str:
        return f'Название напитка "{self.name}"'

    def __repr__(self) -> str:
        return f"Carbonated drinks (name={self.name!r}, carbonation_level={self.carbonation_level!r}, producer={self.producer!r})"

class Cola(Carbonated_drinks):
    def __init__(self, name: str, carbonation_level: str, volume: int, producer: str, sugar_level:int, taste: str):
        self.carbonation_level = carbonation_level
        self.volume = volume
        self.producer = producer
        self.name = name
        self.sugar_level = sugar_level
        self.taste = taste
        if not isinstance(name, str):
            raise TypeError("Название напитка должно быть типа str")
        if not isinstance(producer, str):
            raise TypeError("Название компании-производителя должно быть типа str")
        if not isinstance(volume, str):
            raise TypeError("Объём жидкости должно быть типа int")
        if not isinstance(carbonation_level, str):
            raise TypeError("Степень насыщения углекислым газом должна быть типа str") #сильногазированная, среднегазированная или слабогазированная
        if not isinstance(taste, str):
            raise TypeError("Вкус напитка должен быть типа str")
        if not isinstance(sugar_level, int):
            raise TypeError("Кличество сахара должно быть типа int")

    def __str__(self) -> str:
        return f'Название напитка "{self.name}"'

    def __repr__(self) -> str:
        return f"Carbonated drinks (name={self.name!r}, taste={self.taste}, carbonation_level={self.carbonation_level!r}, producer={self.producer!r})"
