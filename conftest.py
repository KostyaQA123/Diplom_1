import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "Моковая булочка"
    bun.get_price.return_value = 74
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_name.return_value = "Моковый ингредиент"
    ingredient.get_price.return_value = 233
    ingredient.get_type.return_value = "Моковый тип"
    return ingredient
