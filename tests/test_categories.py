"""Тесты модуля categories.py"""

from typing import Any
from unittest.mock import Mock

from src.categories import Category
from src.products import Product


# Тест добавления продукта в категорию продукта с ненулевым количеством
def test_add_product_positive_quantity(category: Category, product: Product, capsys: Any) -> None:
    assert len(category.products) == 2
    category.add_product(product)
    assert len(category.products) == 3
    captured = capsys.readouterr()
    assert captured.out == ("Товар добавлен в категорию\nОбработка добавления товара завершена\n")


# Тест добавления в категорию продукта с нулевым количеством
def test_add_product_zero_quantity(category: Category, product: Product, capsys: Any) -> None:
    mock_quantity = Mock(return_value=0).return_value
    product.quantity = mock_quantity
    assert len(category.products) == 2
    category.add_product(product)
    assert len(category.products) == 2
    captured = capsys.readouterr()
    assert captured.out == (
        "Товар с нулевым количеством не может быть добавлен в категорию\nОбработка добавления товара завершена\n"
    )


# Тест метода calculate_average_price
def test_calculate_average_price(category: Category) -> None:
    assert category.calculate_average_price() == 6544.5


# Тест метода calculate_average_price с пустым списком продуктов
def test_calculate_average_price_empty() -> None:
    category = Category("name", "description", [])
    assert category.calculate_average_price() == 0
