import unittest
import main

class TestMain(unittest.TestCase):
    def test_verificar_aprovacao(self):
        casos_de_teste = [
        # (nota1, nota2, media)
            (0, 0, 0),
            (10, 0, 5),
            (10, 10, 10),
            (5, 5, 5),
            (8, 2, 5),
            (7, 3, 5),
        ]

        for nota1, nota2, resultado_esperado in casos_de_teste:
            resultado_obtido = main.calcular_media(nota1, nota2)
            self.assertEqual(resultado_obtido, resultado_esperado, f"nota1: {nota1}, nota2: {nota2}")

        for media, resultado_esperado in casos_de_teste:
            resultado_obtido = main.verificar_aprovacao(media)
            self.assertEqual(resultado_obtido, resultado_esperado, f"media: {media}")

if __name__ == '__main__':
    unittest.main()