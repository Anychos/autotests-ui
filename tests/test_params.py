import pytest


@pytest.mark.parametrize("number", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_params(number: int):
    print(f"test number {number}")
    assert number >= 5
 