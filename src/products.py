"""Модуль объектов продуктов и их категорий"""

from typing import Any, Iterator


class Product:
    """Класс продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация экземпляра класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __len__(self) -> int:
        """Метод для вывода общего количества продукта"""
        return self.quantity

    def __repr__(self) -> str:
        """Метод для вывода отладочной информации"""
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.__price}, {self.quantity})"

    def __str__(self) -> str:
        """Метод для строкового представления продукта"""
        return f"{self.name}, {self.__price} руб. Остаток: {len(self)} шт."

    def __add__(self, other: Any) -> float:
        """Метод для сложения стоимостей товаров"""
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

    def __len__(self) -> int:
        """Метод для вывода общего количества продуктов в категории"""
        return sum([product.quantity for product in self.__products])

    def __repr__(self) -> str:
        """Метод для вывода отладочной информации"""
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.__products})"

    def __str__(self) -> str:
        """Метод для строкового представления категории"""
        return f"{self.name}, количество продуктов: {len(self)} шт."

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
        return [str(product) for product in self.__products]


class CategoryIterator:
    """Класс итератора категорий продуктов"""

    def __init__(self, category: Category) -> None:
        self.category = category

    def __iter__(self) -> Iterator:
        self.index_product = -1
        return self

    def __next__(self) -> Product:
        if self.index_product + 1 < len(self.category.products):
            self.index_product += 1
            return self.category.products[self.index_product]
        else:
            raise StopIteration
