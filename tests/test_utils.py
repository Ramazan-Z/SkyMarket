"""Тесты модуля utils.py"""

import json
from unittest.mock import Mock, patch

from src.utils import create_class_objects


# Тест функции create_class_objects
def test_create_class_objects() -> None:
    result = create_class_objects("products.json")
    assert result[0].name == "Смартфоны"
    assert result[1].name == "Телевизоры"


# Тест функции create_class_objects с несуществующим файлом
def test_create_class_objects_not_file() -> None:
    result = create_class_objects("No_file.json")
    assert result == []


# Тест функции create_class_objects с ошибкой файла JSON
@patch("json.load")
def test_create_class_objects_error(mock_json: Mock) -> None:
    mock_json.side_effect = json.decoder.JSONDecodeError("", "}", 0)
    result = create_class_objects("products.json")
    assert result == []
    mock_json.assert_called_once()
