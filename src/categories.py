"""Модуль объектов категорий товаров"""

from typing import Any, Iterator

from src.mixins import MixinLog
from src.products import Product


class Category(MixinLog):
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

    def __str__(self) -> str:
        """Метод для строкового представления категории"""
        return f"{self.name}, количество продуктов: {len(self)} шт."

    @property
    def products(self) -> list[Product]:
        """Геттер для атрибута products"""
        return self.__products

    def add_product(self, product: Any) -> None:
        """Метод для добавления объекта продукта в категорию"""
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавить только объекты класса Product или его подклассов")
        self.__products.append(product)
        Category.product_unique_count += 1

    def get_products(self) -> list:
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
