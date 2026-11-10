''' antes da Fatoração'''
from decimal import Decimal


class Imovel:
    def __init__(self, quartos, vagas):
        self.quartos = quartos
        self.vagas = vagas


class Apartamento(Imovel):
    def __init__(self, quartos, vagas, possui_criancas):
        super().__init__(quartos, vagas)
        self.possui_criancas = possui_criancas

    def calcular_aluguel(self):
        valor = Decimal("700.00")

        if self.quartos == 2:
            valor += Decimal("200.00")

        if self.vagas == 1:
            valor += Decimal("300.00")

        if not self.possui_criancas:
            valor *= Decimal("0.95")

        return valor

 
class Casa(Imovel):
    def __init__(self, quartos, vagas):
        super().__init__(quartos, vagas)

    def calcular_aluguel(self):
        valor = Decimal("900.00")

        if self.quartos == 2:
            valor += Decimal("250.00")

        if self.vagas == 1:
            valor += Decimal("300.00")

        return valor



class Estudio(Imovel):
    def __init__(self, vagas):
        super().__init__(1, vagas)

    def calcular_aluguel(self):
        valor = Decimal("1200.00")

        if self.vagas >= 2:
            valor += Decimal("250.00")

            vagas_extras = self.vagas - 2
            valor += vagas_extras * Decimal("60.00")

        return valor


class ContratoLocacao:
    def __init__(self, imovel, parcelas):
        if parcelas < 1 or parcelas > 5:
            raise ValueError("Escolha de 1 a 5 parcelas.")

        self.imovel = imovel
        self.parcelas = parcelas
        self.taxa_contratual = Decimal("2000.00")

    def calcular_parcela(self):
        return self.taxa_contratual / self.parcelas

    def exibir_resumo(self):
        aluguel = self.imovel.calcular_aluguel()
        parcela = self.calcular_parcela()

        print("\n--- RESUMO DO CONTRATO ---")
        print(f"Aluguel mensal: R$ {aluguel:.2f}")
        print(f"Taxa contratual: R$ {self.taxa_contratual:.2f}")
        print(f"Parcelamento: {self.parcelas}x de R$ {parcela:.2f}")


def escolher_opcao(mensagem, opcoes_validas):
    while True:
        resposta = input(mensagem).strip().lower()

        if resposta in opcoes_validas:
            return resposta

        print("Opção inválida. Tente novamente.")


def main():
    print("\n========== RENTSMART ==========")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")

    tipo = escolher_opcao(
        "Escolha o tipo de imóvel: ",
        ("1", "2", "3")
    )

    if tipo == "1":
        quartos = int(escolher_opcao(
            "Quantidade de quartos (1 ou 2): ",
            ("1", "2")
        ))

        garagem = escolher_opcao(
            "Deseja garagem? (s/n): ",
            ("s", "n")
        )
        vagas = 1 if garagem == "s" else 0

        criancas = escolher_opcao(
            "Possui crianças? (s/n): ",
            ("s", "n")
        )

        imovel = Apartamento(
            quartos, vagas, criancas == "s"
        )

    elif tipo == "2":
        quartos = int(escolher_opcao(
            "Quantidade de quartos (1 ou 2): ",
            ("1", "2")
        ))

        garagem = escolher_opcao(
            "Deseja garagem? (s/n): ",
            ("s", "n")
        )
        vagas = 1 if garagem == "s" else 0

        imovel = Casa(quartos, vagas)

    else:
        while True:
            entrada = input(
                "Quantidade de vagas (0 ou 2 ou mais): "
            ).strip()

            if entrada.isdigit():
                vagas = int(entrada)

                if vagas == 0 or vagas >= 2:
                    break

            print("Quantidade de vagas inválida.")

        imovel = Estudio(vagas)

    parcelas = int(escolher_opcao(
        "Parcelas da taxa contratual (1 a 5): ",
        ("1", "2", "3", "4", "5")
    ))

    contrato = ContratoLocacao(imovel, parcelas)
    contrato.exibir_resumo()


if __name__ == "__main__":
    main()
