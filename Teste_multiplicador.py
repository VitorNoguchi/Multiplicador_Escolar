#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from mult_escola_vitor import Multiplicador

class TestMultiplicador(unittest.TestCase):

    def test_positives(self):
        result = Multiplicador.multiplica(self, 12345, 98765)
        self.assertEqual(result[0], 12345 * 98765)

    def test_positive1(self):
        result = Multiplicador.multiplica(self, 12345, -98765)
        self.assertEqual(result[0], 12345 * -98765)

    def test_positive2(self):
        result = Multiplicador.multiplica(self, -12345, 98765)
        self.assertEqual(result[0], -12345 * 98765)

    def test_negative(self):
        result = Multiplicador.multiplica(self, -12345, -98765)
        self.assertEqual(result[0], -12345 * -98765)

    def test_decimal1(self):
        result = Multiplicador.multiplica(self, -123.45, -98765)
        self.assertEqual(result[0], -123.45 * -98765)

    def test_decimal2(self):
        result = Multiplicador.multiplica(self, -1.2345, -0.98765)
        self.assertEqual(result[0], -1.2345 * -0.98765)

    def test_zero(self):
        result = Multiplicador.multiplica(self, -1.2345, 0)
        self.assertEqual(result[0], -1.2345 * 0)

    def test_error(self):
        with self.assertRaises(ValueError):
            Multiplicador.multiplica(self, -1.2345, 'ads')


suite = unittest.TestLoader().loadTestsFromTestCase(TestMultiplicador)
unittest.TextTestRunner(verbosity=2).run(suite)