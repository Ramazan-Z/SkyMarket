"""Тесты модуля products.py"""

from src.products import Category, Product


# Тест инициализации класса Product
def test_product_init(product: Product) -> None:
    assert product.name == "Имя продукта"
    assert product.description == "Описение продукта"
    assert product.price == 10999.99
    assert product.quantity == 100


# Тест инициализации класса Category
def test_category_init(category: Category) -> None:
    assert category.name == "Мебель"
    assert category.description == "Для дома и офиса"
    product = category.products[0]
    assert product.name == "Стол компьютерный"
    assert product.description == "Aceline Basic 01 белый"
    assert product.price == 1699
    assert product.quantity == 16

    assert Category.category_count == 1
    assert Category.product_unique_count == 2
