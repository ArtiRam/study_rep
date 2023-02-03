class KitchenAppliance:
    def __init__(self, brand: str, material: str, price: int):
        self.brand = brand
        self.material = material
        self.price = price

    def __str__(self):
        return f"Кухонный прибор марки {self.brand}. Из материала {self.material}, по ценой без скидки {self.price}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, material={self.material!r})"

    def change_material(self, new_material) -> None:
        self.material = new_material

    def check_price(self) -> None:
        print(self.price)


class Fork(KitchenAppliance):
    def __init__(self, brand: str, material: str, price: int, type_of_fork: str):
        super().__init__(brand, material, price)
        self.type = type_of_fork

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}," \
               f" material={self.material!r}, " \
               f"type_of_fork={self.type!r})"

    # Деревянные столовые вилки дешевле на 10

    def check_price(self) -> None:
        if self.type == 'dining' and self.material == 'wood':
            print(self.price - 10)

        else:
            print(self.price)


if __name__ == "__main__":
    fork = Fork("no_name", "metal", 100, "dining")
    print(fork)
    fork.check_price()
    fork.change_material('wood')
    fork.check_price()
    print(fork)
    print(repr(fork))
