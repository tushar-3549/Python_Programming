import pytest
import math
import source.shape as shapes

# Define a fixture for the Circle object
@pytest.fixture
def circle():
    return shapes.Circle(10)

# Define a fixture for the Rectangle object
@pytest.fixture
def rectangle():
    return shapes.Rectangle(10, 5)

class TestCircle:
    def test_area(self, circle):
        expected_area = math.pi * circle.radius ** 2
        assert circle.area() == expected_area

    def test_perimeter(self, circle):
        expected_perimeter = 2 * math.pi * circle.radius
        assert circle.perimeter() == expected_perimeter


class TestRectangle:
    def test_area(self, rectangle):
        expected_area = rectangle.length * rectangle.height
        assert rectangle.area() == expected_area

    def test_perimeter(self, rectangle):
        expected_perimeter = 2 * (rectangle.length + rectangle.height)
        assert rectangle.perimeter() == expected_perimeter

@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (9, 81)])
def test_multiple_square_area(side_length, expected_area):
    square = shapes.Square(side_length)
    assert square.area() == expected_area
