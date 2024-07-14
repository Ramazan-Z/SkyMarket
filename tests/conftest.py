"""Фикстуры для pytest"""

import pytest

from src.products import Category, LawnGrass, Product, Smartphone


# Фикстура для класса Product
@pytest.fixture
def product() -> Product:
    name = "Имя продукта"
    description = "Описание продукта"
    price = 10999.99
    quantity = 100
    return Product(name, description, price, quantity)


# Фикстура для класса Smartphone
@pytest.fixture
def smartphone() -> Smartphone:
    name = "Смартфон"
    description = "Описание смартфона"
    price = 15000.0
    quantity = 1
    performance = 2  # ГГц
    model = "Samsung"
    memory = 64  # Gb
    color = "black"
    return Smartphone(name, description, price, quantity, performance, model, memory, color)


# Фикстура для класса LawnGrass
@pytest.fixture
def lawn_grass() -> LawnGrass:
    name = "Трава газонная"
    description = "Описание газона"
    price = 5000.0
    quantity = 10
    manufacturer = "China"
    germination_period = 10  # day
    color = "green"
    return LawnGrass(name, description, price, quantity, manufacturer, germination_period, color)


# Фикстура для класса Category
@pytest.fixture
def category() -> Category:
    name = "Мебель"
    description = "Для дома и офиса"
    table = Product("Стол компьютерный", "Aceline Basic 01 белый", 1699.0, 16)
    chair = Product("Стул", "Opus 1 beige / black", 11390.0, 8)
    return Category(name, description, [table, chair])
