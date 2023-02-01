import doctest


class Car:
    def __init__(self, max_speed: int, type_of_engine: str):

        if not isinstance(max_speed, int):
            raise TypeError("Скорость должена быть типа int")
        if max_speed <= 0:
            raise ValueError("Скорость должена быть положительным числом")

        if not isinstance(type_of_engine, str):
            raise ValueError("Тип должена быть типом string")

    def add_fuel(self, fuel: int) -> None:
        """
        Добавление топлива в машину
        :fuel: объем топлива
        tests:
        >>> car = Car(12, 'Diesel')
        >>> car.add_fuel(35)

        """
        ...

    def what_is_type(self) -> bool:
        """

        Проверка типа машины

        tests:
        >>> car = Car(12, 'Diesel')
        >>> car.what_is_type()

        """
        ...


class GameCharacter:
    def __init__(self, main_weapon: str, max_hp: int):

        if not isinstance(max_hp, int):
            raise TypeError("Здоровье должено быть типа int")
        if max_hp <= 0:
            raise ValueError("Здоровье должено быть положительным числом")

        if not isinstance(main_weapon, str):
            raise ValueError("Оружее должено быть типом string")

    def use_skill(self, number_of_skill: int) -> None:
        """
        Использование способности
        :number_of_skill: порядковый номер способности

        tests:
        >>> character = GameCharacter("knife", 100)
        >>> character.use_skill(1)

        """
        ...

    def check_hp(self) -> int:
        """
        Проверка здоровья

        tests:
        >>> character = GameCharacter("knife", 100)
        >>> character.check_hp()

        """
        ...


class Shop:
    def __init__(self, amount_of_product: int, amount_of_space: int):
        if not isinstance(amount_of_product, int):
            raise TypeError("Кол-во продукта должено быть типа int")
        if not isinstance(amount_of_product, int):
            raise TypeError("Кол-во места в магазине должено быть типа int")
        if amount_of_space <= 0:
            raise ValueError("Кол-во места в магазине должено быть положительным числом")

    def add_product(self, amount) -> None:
        """
        Добавление товара
        :amount: кол-во добовляемого товара
        tests:
        >>> shop = Shop(100, 200)
        >>> shop.add_product(12)

        """
        ...

    def sell_product(self, amount) -> None:
        """
        Продажа товара
        :amount: кол-во проданного товара
        tests:
        >>> shop = Shop(100, 200)
        >>> shop.add_product(23)


        """

        ...


if __name__ == "__main__":
    doctest.testmod()
