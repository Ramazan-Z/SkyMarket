"""Тесты модуля mixins.py"""

from typing import Any

from src.categories import Category, CategoryIterator
from src.orders import Order
from src.products import LawnGrass, Product, Smartphone

products_dict = {}  # для использования объекта в следующем тесте
category_dict = {}  # для использования объекта в следующем тесте


# Тест MixinLog с классом Product
def test_mixin_product(capsys: Any, product: Product) -> None:
    captured = capsys.readouterr()
    assert captured.out == "Product('Имя продукта', 'Описание продукта', 10999.99, 100)\n"
    products_dict["product"] = product


# Тест MixinLog с классом Smartphone
def test_mixin_smartphone(capsys: Any, smartphone: Smartphone) -> None:
    captured = capsys.readouterr()
    assert captured.out == "Smartphone(2, 'Samsung', 64, 'black', 'Смартфон', 'Описание смартфона', 15000.0, 1)\n"
    products_dict["smartphone"] = smartphone


# Тест MixinLog с классом LawnGrass
def test_mixin_lawn_grass(capsys: Any, lawn_grass: LawnGrass) -> None:
    captured = capsys.readouterr()
    assert captured.out == "LawnGrass('China', 10, 'green', 'Трава газонная', 'Описание газона', 5000.0, 10)\n"
    products_dict["lawn_grass"] = lawn_grass


# Тест MixinLog с классом Category
def test_mixin_category(capsys: Any) -> None:
    category = Category("Категория", "Тест", [products_dict["product"]])
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Category('Категория', 'Тест', [Product('Имя продукта', 'Описание продукта', 10999.99, 100)])\n"
    )

    Category.category_count = 0
    Category.product_unique_count = 0
    category_dict["category"] = category


# Тест MixinLog с классом CategoryIterator
def test_mixin_category_iterator(capsys: Any) -> None:
    CategoryIterator(category_dict["category"])
    captured = capsys.readouterr()
    assert captured.out == (
        "CategoryIterator(Category('Категория', 'Тест', "
        + "[Product('Имя продукта', 'Описание продукта', 10999.99, 100)]))\n"
    )


# Тест MixinLog с классом Order
def test_mixin_order(capsys: Any) -> None:
    Order(products_dict["smartphone"], 5)
    captured = capsys.readouterr()
    assert captured.out == (
        "Order(1, Smartphone(2, 'Samsung', 64, 'black', 'Смартфон', 'Описание смартфона', 15000.0, 1), 15000.0, 5)\n"
    )

    Order._order_number = 1
