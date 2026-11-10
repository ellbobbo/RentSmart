"Depois da Fatoração"
import csv
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP





class Imovel:
    def __init__(self, quartos, vagas):
        if type(quartos) is not int or quartos not in (1, 2):
            raise ValueError(
                "A quantidade de quartos deve ser 1 ou 2."
            )

        if type(vagas) is not int or vagas < 0:
            raise ValueError(
                "A quantidade de vagas deve ser um inteiro não negativo."
            )

        self.quartos = quartos
        self.vagas = vagas

    def validar_vaga_padrao(self):
        if self.vagas not in (0, 1):
            raise ValueError(
                "Casas e apartamentos aceitam 0 ou 1 vaga."
            )

    def calcular_aluguel(self):
        componentes = self.detalhar_aluguel()
        return sum(componentes.values(), Decimal("0.00"))



    def detalhar_aluguel(self):
        base = Decimal("700.00")
        quartos = Decimal("200.00") if self.quartos == 2 else Decimal("0.00")
        garagem = Decimal("300.00") if self.vagas == 1 else Decimal("0.00")

        subtotal = base + quartos + garagem
        desconto = subtotal * Decimal("0.05") if not self.possui_criancas else Decimal("0.00")

        return {
            "Aluguel-base": base,
            "Segundo quarto": quartos,
            "Garagem": garagem,
            "Desconto": -desconto
        }


class Apartamento(Imovel):
    def __init__(self, quartos, vagas, possui_criancas):
        super().__init__(quartos, vagas)

        self.validar_vaga_padrao()

        if type(possui_criancas) is not bool:
            raise ValueError(
                "A informação sobre crianças deve ser True ou False."
            )

        self.possui_criancas = possui_criancas

    def detalhar_aluguel(self):
        base = Decimal("700.00")

        quartos = (
            Decimal("200.00")
            if self.quartos == 2
            else Decimal("0.00")
        )

        garagem = (
            Decimal("300.00")
            if self.vagas == 1
            else Decimal("0.00")
        )

        subtotal = base + quartos + garagem

        desconto = (
            subtotal * Decimal("0.05")
            if not self.possui_criancas
            else Decimal("0.00")
        )

        return {
            "Aluguel-base": base,
            "Segundo quarto": quartos,
            "Garagem": garagem,
            "Desconto": -desconto
        }


class Casa(Imovel):

    def __init__(self, quartos, vagas):
        if type(quartos) is not int or quartos not in (1, 2):
            raise ValueError(
                "A quantidade de quartos deve ser 1 ou 2."
            )

        if type(vagas) is not int or vagas not in (0, 1):
            raise ValueError(
                "Casas e apartamentos aceitam 0 ou 1 vaga."
            )

        self.quartos = quartos
        self.vagas = vagas

    
    def __init__(self, quartos, vagas):
        super().__init__(quartos, vagas)
        self.validar_vaga_padrao()
    


    def detalhar_aluguel(self):
        return {
            "Aluguel-base": Decimal("900.00"),
            "Segundo quarto": Decimal("250.00") if self.quartos == 2 else Decimal("0.00"),
            "Garagem": Decimal("300.00") if self.vagas == 1 else Decimal("0.00")
        }


class Estudio(Imovel):  
    
    def __init__(self, vagas):
        super().__init__(1, vagas)

        if vagas == 1:
            raise ValueError(
                "Estúdios aceitam 0 vagas ou um pacote de 2 ou mais."
            )




    def detalhar_aluguel(self):
        pacote = Decimal("250.00") if self.vagas >= 2 else Decimal("0.00")
        extras = max(0, self.vagas - 2) * Decimal("60.00")

        return {
            "Aluguel-base": Decimal("1200.00"),
            "Pacote de vagas": pacote,
            "Vagas adicionais": extras
        }




class ContratoLocacao:
    
    def __init__(self, imovel, parcelas):
        if not isinstance(imovel, Imovel):
            raise TypeError("O contrato precisa receber um imóvel válido.")

        if type(parcelas) is not int or not 1 <= parcelas <= 5:
            raise ValueError(
                "Escolha de 1 a 5 parcelas."
            )

        self.imovel = imovel
        self.parcelas = parcelas
        self.taxa_contratual = Decimal("2000.00")


    
    def calcular_parcela(self):
        return (
            self.taxa_contratual / self.parcelas
        ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    
    def calcular_taxa_mes(self, mes):
        if mes > self.parcelas:
            return Decimal("0.00")

        parcela = self.calcular_parcela()

        if mes == self.parcelas:
            return self.taxa_contratual - parcela * (self.parcelas - 1)

        return parcela


    def exibir_resumo(self):
        aluguel = self.imovel.calcular_aluguel()
        parcela = self.calcular_parcela()

        ultima_parcela = self.calcular_taxa_mes(self.parcelas)

        if parcela == ultima_parcela:
            print(f"Parcelamento: {self.parcelas}x de R$ {parcela:.2f}")
        else:
            print(f"Parcelamento: {self.parcelas - 1}x de R$ {parcela:.2f}")
            print(f"Última parcela: R$ {ultima_parcela:.2f}")

       
        for descricao, valor in self.imovel.detalhar_aluguel().items():
            if valor != 0:
                print(f"{descricao}: R$ {valor:.2f}")

        print("-----------------------------------------")
        print(f"Aluguel mensal: R$ {aluguel:.2f}")
        print(f"Taxa contratual: R$ {self.taxa_contratual:.2f}")
        print(f"Parcelamento: {self.parcelas}x de R$ {parcela:.2f}")
        print(f"Total do primeiro mês: R$ {aluguel + parcela:.2f}")


        total_anual = aluguel * 12 + self.taxa_contratual

        print("-----------------------------------------")
        print(f"Total previsto em 12 meses: R$ {total_anual:.2f}")


    def gerar_csv(self):
        caminho = Path(__file__).resolve().parent / "projecao_12_meses.csv"

        aluguel = self.imovel.calcular_aluguel()
        parcela = self.calcular_parcela()

        with caminho.open("w", newline="", encoding="utf-8-sig") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")

            escritor.writerow([
                "Mês",
                "Aluguel (R$)",
                "Taxa contratual (R$)",
                "Total (R$)"
            ])

            for mes in range(1, 13):
                taxa_mes = self.calcular_taxa_mes(mes)

                total = aluguel + taxa_mes

                escritor.writerow([
                    mes,
                    f"{aluguel:.2f}".replace(".", ","),
                    f"{taxa_mes:.2f}".replace(".", ","),
                    f"{total:.2f}".replace(".", ",")
                ])

        print(f"\nArquivo CSV gerado: {caminho}")




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
    contrato.gerar_csv()


if __name__ == "__main__":
    main()



