"""Модуль вспомогательных функций"""

import json
import os

from src.categories import Category
from src.products import Product

ROOT = os.path.join(os.path.dirname(__file__), "..", "data")


def create_class_objects(file_name: str) -> list[Category]:
    """Функция принимает строку с именем файла JSON, создает объекты классов
    и возвращает список этих объектов"""
    try:
        with open(os.path.join(ROOT, file_name)) as file:
            try:
                json_data = json.load(file)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []

    categories_list = []
    for category in json_data:
        category_obj = Category(
            category["name"], category["description"], [Product(**product) for product in category["products"]]
        )
        categories_list.append(category_obj)

    return categories_list
