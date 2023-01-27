class Accelerator:

    GEV_TO_J = 0.938

    """ Базовый класс ускоритель """

    def __init__(self, name: str, energy: float, mass: float):
        """
        Создание и подготовка к работе объекта ускоритель
        :param name: название ускорителя
        :param energy: начальная энергия частиц в ГэВ
        :param mass: масса частиц в ГэВ
        """
        self.name = name
        self.energy = energy
        self.mass = mass

    def __str__(self):
        return f"Ускоритель - {self.name}. Начальная энергия частиц - {self.energy}. Масса - {self.mass}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, energy={self.energy}, mass={self.mass})"

    @property
    def name_(self) -> str:
        """"Возвращает название ускорителя."""
        return self.name

    @property
    def mass(self) -> float:
        """"Возвращает массу частицы."""
        return self._mass

    @mass.setter
    def mass(self, mass: float) -> None:
        """Устанавливает массу частицы."""
        if not isinstance(mass, float):
            raise TypeError("Масса должна быть типа float")
        if mass < 0:
            raise ValueError("Масса должна быть положительным числом")
        self._mass = mass

    @property
    def energy(self) -> float:
        """"Возвращает начальную энергию пучка."""
        return self._energy

    @energy.setter
    def energy(self, energy: float) -> None:
        """Устанавливает энергию пучка частиц."""
        if not isinstance(energy, float):
            raise TypeError("Энергия должна быть типа float")
        if energy < 0:
            raise ValueError("Энергия должна быть положительным числом")
        self._energy = energy

    def is_relative(self) -> bool:
        """"Проверяет релятивистский или нет пучок."""
        return self.energy > self.mass

    def boost(self, delta_energy: float, time: float) -> float:
        """
        Вычисляет конечную энергию пучка
        :delta_energy: приращение энергии в ГэВ/c
        :time: время ускорения в секундах

        Примеры:
        accelerator1 = Accelerator("NICA", 20, 1)
        final_energy = accelerator1.boost(0.5, 20)
        print(accelerator1.is_relative())
        """
        return self.energy + delta_energy * time


class Linear(Accelerator):
    """ Дочерний класс линейный ускоритель """
    def __init__(self, name: str, energy: float, mass: float, length: float):
        """
        Создание и подготовка к работе объекта линейный ускоритель
        :param length: длина линейного ускорителя в метрах
        """
        super().__init__(name, energy, mass)
        self.length = length

    def __str__(self):
        return f"Соударение - {self.name}. Начальная энергия частиц - {self.energy}." \
               f" Масса - {self.mass}. Длина - {self.length}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, energy={self.energy}," \
               f" mass={self.mass}, length={self.length})"

    @property
    def length_(self) -> float:
        """"Устанавливает длину ускорителя"""
        return self.length

    def boost(self, delta_energy: float, **kwargs) -> float:
        """
        Вычисляет конечную энергию пучка
        :param delta_energy: приращение энергии в ГэВ/м

        Примеры:
        accelerator2 = Linear("LINAC", 20, 1, 100)
        final_energy = accelerator2.boost(0.5)
        print(accelerator2.is_relative())
        """
        return self.energy + delta_energy * self.length


class Cyclic(Accelerator):
    """ Дочерний класс циклический ускоритель """

    def __init__(self, name: str, energy: float, mass: float, radius: float):
        """
        Создание и подготовка к работе объекта линейный ускоритель
        :param radius: радиус орбиты ускорителя
        """
        super().__init__(name, energy, mass)
        self.radius = radius

    def __str__(self):
        return f"Ускоритель - {self.name}. Начальная энергия частиц - {self.energy}." \
               f" Масса - {self.mass}. Радиус - {self.radius}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, energy={self.energy}," \
               f" mass={self.mass}, radius={self.radius})"

    @property
    def radius_(self) -> float:
        """Устанавливает радиус орбиты ускорителя"""
        return self.radius

    def boost(self, b: float, **kwargs) -> float:
        """
        Вычисляет конечную энергию пучка
        :param b: индукция магнитного поля

        Примеры:
        accelerator3 = Cyclic("LHC", 20, 1, 100)
        final_energy = accelerator3.boost(200)
        print(accelerator3.is_relative())
        """
        v = self.radius * b / self.GEV_TO_J
        return self.mass * v * v / 2


if __name__ == "__main__":
    a = Accelerator("NICA", 20., 10.)
    b = Linear("LINAC", 20., 1., 10.)
    c = Cyclic("LHC", 1., 1., 10.)
    print(c.boost(1.))
    print(b.is_relative())
    pass
