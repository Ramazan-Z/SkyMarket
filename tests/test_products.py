"""Тесты модуля products.py"""

from typing import Any

import pytest

from src.products import Category, CategoryIterator, Product


# Тест инициализации класса Product
def test_product_init(product: Product) -> None:
    assert product.name == "Имя продукта"
    assert product.description == "Описание продукта"
    assert product.price == 10999.99
    assert product.quantity == 100


# Тест сеттера класса Product случай с повышением цены
def test_product_setter_price_up(product: Product) -> None:
    assert product.price == 10999.99
    product.price = 15000.0
    assert product.price == 15000.0


# Тест сеттера класса Product случай с отрицательной ценой
def test_product_setter_price_negative(product: Product, capsys: Any) -> None:
    assert product.price == 10999.99
    product.price = -150
    captured = capsys.readouterr()
    assert captured.out == "Введена некорректная цена\n"
    assert product.price == 10999.99


# Тест сеттера класса Product случай с понижением цены и подтверждением
def test_product_setter_price_down_yes(product: Product, monkeypatch: Any) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert product.price == 10999.99
    product.price = 1000.0
    assert product.price == 1000.0


# Тест сеттера класса Product случай с понижением цены и отказом
def test_product_setter_price_down_no(product: Product, monkeypatch: Any) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert product.price == 10999.99
    product.price = 1000.0
    assert product.price == 10999.99


# Тест метода create_product случай повтора имени и повышения цены
def test_create_product_repeat_name_price_up(product: Product) -> None:
    assert product.price == 10999.99
    assert product.quantity == 100.0
    new_product = Product.create_product("Имя продукта", "Описание продукта", 15000.0, 10, [product])
    assert new_product is product
    assert new_product.price == 15000.0
    assert new_product.quantity == 110


# Тест метода create_product случай повтора имени и понижения цены
def test_create_product_repeat_name_price_down(product: Product) -> None:
    assert product.price == 10999.99
    assert product.quantity == 100.0
    new_product = Product.create_product("Имя продукта", "Описание продукта", 5000.0, 10, [product])
    assert new_product is product
    assert new_product.price == 10999.99
    assert new_product.quantity == 110


# Тест метода create_product случай нового имени
def test_create_product_new_product(product: Product) -> None:
    assert product.price == 10999.99
    assert product.quantity == 100
    new_product = Product.create_product("Новый продукт", "Описание продукта", 12000.0, 10, [product])
    assert new_product is not product
    assert new_product.price == 12000.0
    assert new_product.quantity == 10
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


# Тест метода add_product
def test_add_product(category: Category) -> None:
    assert len(category.products) == 2
    category.add_product(Product("New name", "New description", 12999.0, 4))
    assert len(category.products) == 3
    assert Category.category_count == 2
    assert Category.product_unique_count == 5


# Тест метода get_products
def test_get_products(category: Category) -> None:
    assert category.get_products() == [
        "Стол компьютерный, 1699.0 руб. Остаток: 16 шт.",
        "Стул, 11390.0 руб. Остаток: 8 шт.",
    ]


# Тест метода __len__ класса Product
def test_len_product(product: Product) -> None:
    assert len(product) == 100


# Тест метода __repr__ класса Product
def test_repr_product(product: Product) -> None:
    assert repr(product) == "Product('Имя продукта', 'Описание продукта', 10999.99, 100)"


# Тест метода __str__ класса Product
def test_str_product(product: Product) -> None:
    assert str(product) == "Имя продукта, 10999.99 руб. Остаток: 100 шт."


# Тест метода __add__ класса Product
def test_magic_add_product(product: Product) -> None:
    new_product = Product("Новый продукт", "Новое описание", 500.0, 20)
    assert product + new_product == 1109999.0


# Тест метода __len__ класса Category
def test_len_category(category: Category) -> None:
    assert len(category) == 24


# Тест метода __repr__ класса Category
def test_repr_category(category: Category) -> None:
    assert repr(category) == (
        "Category('Мебель', 'Для дома и офиса', "
        + "[Product('Стол компьютерный', 'Aceline Basic 01 белый', 1699.0, 16), "
        + "Product('Стул', 'Opus 1 beige / black', 11390.0, 8)])"
    )


# Тест метода __str__ класса Category
def test_str_category(category: Category) -> None:
    assert str(category) == "Мебель, количество продуктов: 24 шт."


# Тест класса CategoryIterator
def test_category_iterator(category: Category) -> None:
    category_iterator = iter(CategoryIterator(category))
    assert repr(next(category_iterator)) == "Product('Стол компьютерный', 'Aceline Basic 01 белый', 1699.0, 16)"
    assert repr(next(category_iterator)) == "Product('Стул', 'Opus 1 beige / black', 11390.0, 8)"
    with pytest.raises(StopIteration):
        next(category_iterator)
