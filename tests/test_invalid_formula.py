import unittest

import xlrd

from .helpers import from_sample


class TestInvalidFormula(unittest.TestCase):
    def test_evaluate_name_formula_with_invalid_operand(self):
        xlrd.open_workbook(from_sample('invalid_formula.xls'))


if __name__ == '__main__':
    unittest.main()
