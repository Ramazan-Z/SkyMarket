"""Модуль объектов продуктов"""

from typing import Any

from src.abstract_classes import BaseProduct
from src.mixins import MixinLog


class Product(BaseProduct, MixinLog):
    """Класс продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация экземпляра класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __len__(self) -> int:
        """Метод для вывода общего количества продукта"""
        return self.quantity

    def __str__(self) -> str:
        """Метод для строкового представления продукта"""
        return f"{self.name}, {self.__price} руб. Остаток: {len(self)} шт."

    def __add__(self, other: Any) -> float:
        """Метод для сложения стоимостей товаров"""
        if type(self) is not type(other):
            raise TypeError("Складывать товары можно только из одинаковых классов продуктов.")
        return self.__price * len(self) + float(other.price) * len(other)

    @property
    def price(self) -> float:
        """Геттер для атрибута price"""
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        """Сеттер для атрибута price"""
        if price <= 0:
            print("Введена некорректная цена")
        elif self.__price <= price:
            self.__price = price
        elif input("Понизить цену? y/n: ").lower() == "y":
            self.__price = price

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, products: list[Any] = []) -> Any:
        """Метод для создания нового продукта или добавления к существующим
        с обновлением цены"""
        for product in products:
            if name == product.name:
                product.price = max([product.price, price])
                product.quantity += quantity
                return product
        return cls(name, description, price, quantity)


class Smartphone(Product):
    """Класс продукта категории «Смартфон»"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        performance: int,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализация новых атрибутов экземпляра класса"""
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, products: list[Any] = []) -> Any:
        """Метод для создания нового продукта или добавления к существующим
        с обновлением цены"""
        performance = 2  # Ггц
        model = "No model"
        memory = 64  # Gb
        color = "black"

        for product in products:
            if name == product.name:
                product.price = max([product.price, price])
                product.quantity += quantity
                return product
        return cls(name, description, price, quantity, performance, model, memory, color)


class LawnGrass(Product):
    """Класс продукта категории «Трава газонная»"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        manufacturer: str,
        germination_period: int,
        color: str,
    ) -> None:
        """Инициализация новых атрибутов экземпляра класса"""
        self.manufacturer = manufacturer
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, products: list[Any] = []) -> Any:
        """Метод для создания нового продукта или добавления к существующим
        с обновлением цены"""
        manufacturer = "unknown"
        germination_period = 10
        color = "green"

        for product in products:
            if name == product.name:
                product.price = max([product.price, price])
                product.quantity += quantity
                return product
        return cls(name, description, price, quantity, manufacturer, germination_period, color)
