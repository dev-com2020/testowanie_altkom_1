import pytest


@pytest.fixture
def greetings():
    print("WITAJ")
    yield
    print("WITAJ PONOWNIE")


class TestCase:
    def test_second(self):
        assert 10 == 10

    @pytest.mark.usefixtures("greetings")
    def test_third(self):
        assert 20 == 20
