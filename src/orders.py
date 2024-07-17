"""Модуль объектов заказов"""

from typing import Any

from src.abstract_classes import AbstractOrder
from src.mixins import MixinLog
from src.products import Product


class Order(AbstractOrder, MixinLog):
    """Класс заказов"""

    _order_number: int = 1  # Номер заказа

    def __init__(self, product: Product, quantity: int) -> None:
        """Инициализация заказа"""
        self.number = self._order_number
        self.product = product
        self.price = product.price
        self.quantity = quantity
        Order._order_number += 1
        super().__init__()

    def __str__(self) -> str:
        """Метод для строкового представления заказа"""
        return f"Заказ №{self.number}: {self.product.name} - {self.quantity} шт. Всего {self.cost} руб."

    def __len__(self) -> int:
        """Метод для вывода количества товаров в заказе"""
        return self.quantity

    @property
    def cost(self) -> float:
        """Геттер для атрибута стоимости заказа"""
        return self.price * self.quantity

    @property
    def get_products(self) -> Any:
        """Геттер для получения описания товара в корзине"""
        return self.product.description

    def add_product(self, quantity: int = 1) -> None:
        """Метод для увеличения количества товара в корзине"""
        self.quantity += quantity
