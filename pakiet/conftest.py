import pytest


@pytest.fixture
def random_number_generator():
    import random
    def _number_provider():
        return random.choice(range(10))
    yield _number_provider

