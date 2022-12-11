import doctest
# TODO Написать 3 класса с документацией и аннотацией типов


class Flat:
    def __init__(self, rooms: int, price: (float, int)):
        """
        Создание и подготовка к работе объекта квартира
        :param rooms: количество комнат в квартире
        :param price: цена квартиры в млн руб
        """
        if not isinstance(rooms, int):
            raise TypeError("Количество комнат должно быть типа int")
        if rooms <= 0:
            raise ValueError("Количество комнат не может быть равно нулю или быть отрицательным")
        self.rooms = rooms

        if not isinstance(price, (float, int)):
            raise TypeError("Цена квартиры должна быть типа float или int")
        if price <= 0:
            raise ValueError("Цена не может быть равно нулю или быть отрицательной")
        self.price = price

    def cleaning(self) -> None:
        """ уборка квартиры """
        ...

    def alarm_system_on(self) ->None:
        """
        включение сигнализации

        Примеры:
        >>> flat1 = Flat(3, 10)
        >>> flat1.cleaning()
        """
        ...


class Toy:
    def __init__(self, color: str, size: str, name: str):
        """
               Создание и подготовка к работе объекта ваза
               :param color: цвет игрушки
               :param size: размер игрушки
               :param name: имя игрушки
               """
        if not isinstance(color, str):
            raise TypeError("Цвет игрушки должен быть типа str")
        self.color = color

        if not isinstance(size, str):
            raise TypeError("Размер игрушки должен быть типа str")
        self.size = size

        if not isinstance(name, str):
            raise TypeError("Имя игрушки должно быть типа str")
        self.name = name

    def buy(self) -> None:
        """покупка игрушки"""
        ...

    def play(self) -> None:
        """
        играем с игрушкой

        Примеры:
        >>> toy = Toy("коричневый", "средний", "Тедди")
        >>> toy.play()
        """
        ...


class PDF:
    def __init__(self, set_pdf: str, particle_id: int, Q2: (float, int), x: (float, int)):
        """
         Создание и подготовка к работе объекта функция партонного распределения, который создает pdf
         для определенной частицы и считает значение при определенных Q2 и х
         :param set_pdf: имя сета pdf's в LHAPDF
         :param particle_id: id частицы в схеме PDG
         :param Q2: модуль переданного импульса
         :param x: переменная Бьоркена
         """

        if not isinstance(set_pdf, str):
            raise TypeError("Название сета pdf's должно быть типа str")
        self.set_pdf = set_pdf

        if not isinstance(particle_id, int):
            raise TypeError("id частицы должно быть типа int")
        self.particle_id = particle_id

        if not isinstance(Q2, (float, int)):
            raise TypeError("Модуль переданного импульса должен быть типа float или int ")
        if Q2 < 0:
            raise ValueError("Модуль переданного импульса не может быть отрицательным")
        self.Q2 = Q2

        if not isinstance(x, (float, int)):
            raise TypeError("Переменная Бьоркена должна быть типа float или int ")
        if (x < 0 or x > 1):
            raise ValueError("Переменная Бьоркена лежит в пределах от 0 до 1")
        self.x = x

    def make_pdf(self) -> list:
        """
        Создание списка с известными pdf
        >>> pdf1 = PDF("cteq61", 2, 1.01, 0.3)
        >>> pdf_list = pdf1.make_pdf()
        """
        ...


    def get_value(self) -> float:
        """
        нахождение значения pdf

        """
        ...


if __name__ == "__main__":
     doctest.testmod()

    # TODO работоспособность экземпляров класса проверить с помощью doctest
