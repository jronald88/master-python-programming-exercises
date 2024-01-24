import pytest
from app import MathOperations

@pytest.mark.it("The 'MathOperations' class should exist")
def test_math_operations_class_exists():
    try:
        assert MathOperations
    except AttributeError:
        raise AttributeError("The class 'MathOperations' should exist in app.py")

@pytest.mark.it("The MathOperations class includes the 'add_numbers' static method")
def test_math_operations_has_add_numbers_static_method():
    assert hasattr(MathOperations, "add_numbers")

@pytest.mark.it("The 'add_numbers' static method should return the expected sum")
def test_add_numbers_static_method_returns_expected_sum():
    result = MathOperations.add_numbers(5, 7)
    assert result == 12

@pytest.mark.it("There should be an instance of MathOperations")
def test_math_operations_instance_exists():
    try:
        assert isinstance(MathOperations(), MathOperations)
    except AttributeError:
        raise AttributeError("An instance of 'MathOperations' should exist")
