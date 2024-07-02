"""Модуль объектов продуктов и их категорий"""

from typing import Any


class Product:
    """Класс продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация экземпляра класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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


class Category:
    """Класс категорий продуктов"""

    category_count: int = 0
    product_unique_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """Инициализация экземпляра класса"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_unique_count += len(products)

    @property
    def products(self) -> list[Product]:
        """Геттер для атрибута products"""
        return self.__products

    def add_product(self, product: Product) -> None:
        """Метод для добавления объекта продукта в категорию"""
        self.__products.append(product)
        Category.product_unique_count += 1

    def get_products(self) -> list[str]:
        """Метод для получения списка продуктов в категории в виде строк"""
        products_list = []
        for product in self.__products:
            name = product.name
            price = product.price
            quantity = product.quantity
            products_list.append(f"{name}, {price} руб. Остаток: {quantity} шт.")
        return products_list
