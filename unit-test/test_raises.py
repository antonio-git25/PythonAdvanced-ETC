import unittest

def divide_numbers(a: int | float, b: int | float) -> float:
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        raise ValueError("Нельзя делить на ноль")
    except TypeError:
        raise ValueError("Оба аргумента должны быть числами")


class DivideTestCase(unittest.TestCase):
    def test_valid_division(self):
        result = divide_numbers(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaisesRegex(ValueError, 'Нельзя делить на ноль'):
            divide_numbers(10, 0)

    def test_invalid_input(self):
        with self.assertRaisesRegex(ValueError, 'Оба аргумента должны быть числами'):
            divide_numbers("10", 2)

if __name__ == '__main__':
    unittest.main()
