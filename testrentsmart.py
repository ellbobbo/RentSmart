
import unittest
from decimal import Decimal

from rentsmart import Apartamento, Casa, Estudio, ContratoLocacao


class TestRentSmart(unittest.TestCase):

    def test_apartamento_com_desconto(self):
        apartamento = Apartamento(1, 0, False)
        self.assertEqual(
            apartamento.calcular_aluguel(),
            Decimal("665.00")
        )

    def test_apartamento_sem_desconto(self):
        apartamento = Apartamento(2, 1, True)
        self.assertEqual(
            apartamento.calcular_aluguel(),
            Decimal("1200.00")
        )

    def test_casa(self):
        casa = Casa(1, 0)
        self.assertEqual(
            casa.calcular_aluguel(),
            Decimal("900.00")
        )

    def test_estudio_sem_vagas(self):
        estudio = Estudio(0)
        self.assertEqual(
            estudio.calcular_aluguel(),
            Decimal("1200.00")
        )

    def test_estudio_com_vagas_extras(self):
        estudio = Estudio(3)
        self.assertEqual(
            estudio.calcular_aluguel(),
            Decimal("1510.00")
        )

    def test_parcelamento_tres_vezes(self):
        contrato = ContratoLocacao(Casa(1, 0), 3)

        valores = [
            contrato.calcular_taxa_mes(mes)
            for mes in range(1, 13)
        ]

        self.assertEqual(
            valores[:3],
            [
                Decimal("666.67"),
                Decimal("666.67"),
                Decimal("666.66")
            ]
        )

        self.assertEqual(sum(valores), Decimal("2000.00"))
        self.assertTrue(all(valor == 0 for valor in valores[3:]))

    def test_quartos_invalidos(self):
        with self.assertRaises(ValueError):
            Casa(3, 0)

    def test_vagas_invalidas(self):
        with self.assertRaises(ValueError):
            Estudio(1)

    def test_parcelas_invalidas(self):
        with self.assertRaises(ValueError):
            ContratoLocacao(Casa(1, 0), 6)


if __name__ == "__main__":
    unittest.main()
