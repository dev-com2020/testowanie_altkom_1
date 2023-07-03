import pytest


@pytest.fixture
def greetings():
    print("WITAJ")
    yield
    print("WITAJ PONOWNIE")


@pytest.fixture(scope="class")
def provide_current_time(request):
    import datetime
    request.cls.now = datetime.datetime.now()
    print("WEJŚCIE DO KLASY")
    yield
    print("OPUSZCZENIE KLASY")


@pytest.mark.usefixtures("provide_current_time")
class TestClass:
    def test_first(self):
        print("DATA ROZPOCZĘCIA", self.now)
        assert 1 == 1

    @pytest.mark.usefixtures("greetings")
    def test_second(self):
        assert 2 == 2


class TestCase:
    def test_second(self):
        assert 10 == 10

    @pytest.mark.usefixtures("greetings")
    def test_third(self):
        assert 20 == 20
