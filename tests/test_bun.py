from praktikum.bun import Bun


class TestBun:
    def test_get_name_returns_name(self):
        bun = Bun("Именная булочка", 60)
        assert bun.get_name() == "Именная булочка"

    def test_get_price_returns_price(self):
        bun = Bun("Дорогая булочка", 1000)
        assert bun.get_price() == 1000
