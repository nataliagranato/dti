import unittest
from datetime import datetime

from petshop import melhor_petshop


def test_melhor_petshop(self):
    # Teste com data válida
    data = datetime.strptime("2023-12-01", "%Y-%m-%d")
    resultado = melhor_petshop(data, 2, 3)
    self.assertEqual(resultado, "Meu Canino Feliz")

    # Teste com data inválida
    data = datetime.strptime("2023-12-31", "%Y-%m-%d")
    with self.assertRaises(ValueError):
        melhor_petshop(data, 2, 3)

    # Teste com diferentes combinações de quantidades de cães pequenos e grandos
    resultado = melhor_petshop(data, 5, 0)
    self.assertEqual(resultado, "Vai Rex")

    resultado = melhor_petshop(data, 0, 5)
    self.assertEqual(resultado, "ChowChawgas")

    resultado = melhor_petshop(data, -1, 0)
    self.assertEqual(resultado, "Meu Canino Feliz")


if __name__ == '__main__':
    unittest.main()
