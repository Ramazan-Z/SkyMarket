"""Тесты модуля orders.py"""

from src.orders import Order
from src.products import Product


# Тест инициализации класса Order
def test_order_init(product: Product) -> None:
    order = Order(product, 10)
    assert order.number == 1
    assert order.price == 10999.99
    assert order.quantity == 10
    assert order.cost == 109999.9


# Тест метода get_products класса Order
def test_order_get_products(product: Product) -> None:
    order = Order(product, 10)
    assert order.number == 2
    assert order.get_products == "Описание продукта"


# Тест метода add_product класса Order
def test_order_add_product(product: Product) -> None:
    order = Order(product, 10)
    assert order.number == 3
    assert len(order) == 10
    assert order.cost == 109999.9
    order.add_product(90)
    assert len(order) == 100
    assert order.cost == 1099999


# Тест метода __str__ класса Order
def test_order_str(product: Product) -> None:
    order = Order(product, 10)
    assert str(order) == "Заказ №4: Имя продукта - 10 шт. Всего 109999.9 руб."


# Тест метода __repr__ класса Order
def test_order_repr(product: Product) -> None:
    order = Order(product, 10)
    assert repr(order) == ("Order(5, Product('Имя продукта', 'Описание продукта', 10999.99, 100), 10999.99, 10)")
