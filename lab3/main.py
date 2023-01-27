class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name_(self) -> str:
        return self.name

    @property
    def author_(self) -> str:
        return self.author


class PaperBook(Book):
    def __init__(self, pages: int, name: str, author: str):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    @property
    def pages_(self) -> int:
        return self.pages

    @pages_.setter
    def pages_(self, pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages


class AudioBook(Book):
    def __init__(self, duration: float, name: str, author: str):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    @property
    def duration_(self) -> float:
        return self.duration

    @duration_.setter
    def duration_(self, duration: float) -> None:
        """Устанавливает продолжительность книги."""
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self.duration = duration
