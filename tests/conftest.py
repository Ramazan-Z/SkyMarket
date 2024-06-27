"""Фикстуры для pytest"""

import pytest

from src.products import Category, Product


# Фикстура для класса Product
@pytest.fixture
def product() -> Product:
    name = "Имя продукта"
    description = "Описение продукта"
    price = 10999.99
    quantity = 100
    return Product(name, description, price, quantity)


# Фикстура для класса Category
@pytest.fixture
def category() -> Category:
    name = "Мебель"
    description = "Для дома и офиса"

    table = Product("Стол компьютерный", "Aceline Basic 01 белый", 1699, 16)
    chair = Product("Стул", "Opus 1 beige / black", 11390.0, 8)

    return Category(name, description, [table, chair])
