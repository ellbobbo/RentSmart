RentSmart — Sistema de Orçamentos de Locação

Uma aplicação de terminal desenvolvida em Python para automatizar orçamentos de locação da imobiliária fictícia R.M. Imóveis. O sistema calcula o aluguel mensal conforme as características do imóvel, aplica adicionais e descontos, apresenta a taxa contratual separadamente e gera um arquivo CSV com a projeção de pagamentos dos primeiros 12 meses.



				Projeto acadêmico para praticar Programação Orientada a Objetos.

		Funcionalidades

• Seleção entre apartamento, casa e estúdio.
• Entrada e validação das características da locação.
• Cálculo automático de aluguel-base, adicionais e desconto aplicável.
• Cálculo da taxa contratual de R$ 2.000,00, parcelável em 1 a 5 vezes.
• Tratamento de arredondamento de centavos no parcelamento.
• Exibição de um orçamento detalhado, com aluguel e taxa contratual separados.
• Apresentação do total previsto para os 12 primeiros meses.
• Geração de PROJECAO_12_MESES.CSV com aluguel, taxa e total de cada mês.

		Regras de negócio

 Tipo de imóvel | Aluguel-base | Adicional para 2 quartos | Estacionamento 

 Apartamento | R$ 700,00 | R$ 200,00 | R$ 300,00 por 1 vaga 
 Casa | R$ 900,00 | R$ 250,00 | R$ 300,00 por 1 vaga 
 Estúdio | R$ 1.200,00 | Não se aplica | R$ 250,00 pelo pacote inicial de 2 vagas, mais R$ 60,00 por vaga extra 

Desconto de apartamento: quando o cliente informa que não possui crianças, recebe 5% de desconto sobre o aluguel após a inclusão dos adicionais.

Taxa contratual: R$ 2.000,00, cobrada separadamente do aluguel. A taxa pode ser dividida em até cinco parcelas. Quando houver diferença de centavos, a última parcela é ajustada para que a soma corresponda exatamente a R$ 2.000,00.

		Premissas adotadas

• Casas e apartamentos podem ter 1 ou 2 quartos e 0 ou 1 vaga de garagem.
• O estúdio utiliza a categoria prevista no enunciado, sem opção de quarto adicional.
• Para estúdios, são permitidas 0 vagas ou 2 ou mais vagas. A opção de apenas 1 vaga não foi adotada porque o enunciado define o preço a partir de um pacote inicial de 2 vagas.
• A projeção considera 12 meses com aluguel constante, sem reajustes, pois o enunciado não estabelece índices ou datas de reajuste.
• O arquivo CSV é atualizado a cada novo orçamento executado.


	Organização orientada a objetos

O código utiliza classes, objetos, atributos, métodos, herança e polimorfismo:

	 Imovel: classe base; guarda os atributos comuns (QUARTOS  e VAGAS), realiza validações gerais e calcula o aluguel a partir dos componentes informados pelas subclasses.
	 Apartamento: define o aluguel-base, adicional por segundo quarto, garagem e desconto pela ausência de crianças.
	Casa: define o aluguel-base e os adicionais específicos de quartos e garagem.
	Estudio: define o aluguel-base e as regras de pacote e vagas adicionais.
	ContratoLocacao: recebe um objeto de imóvel, calcula as parcelas da taxa, apresenta o orçamento e gera a projeção em CSV.

As classes APARTAMENTO, CASA e ESTUDIO herdam de IMOVEL e implementam o método DETALHAR_ALUGUEL() com regras próprias. Dessa forma, CONTRATOLOCACAO pode trabalhar com qualquer uma dessas categorias sem duplicar o cálculo de cada tipo de imóvel.


Requisitos:

	 Python 3 instalado.
	 Nenhuma biblioteca externa é necessária. O projeto utiliza módulos da biblioteca padrão do Python, como CSV, PATHLIB e DECIMAL.

Como executar

1. Baixe ou clone o repositório do projeto.
2. Abra um terminal na pasta que contém o arquivo RENTSMART.PY.
3. Execute:

   bash
   python3 rentsmart.py
   

   No Windows, caso PYTHON3 não esteja disponível, utilize PV RENTSMART.PY ou PYTHON RENTSMART.PY, conforme a instalação.

4. Escolha a categoria do imóvel e informe os dados solicitados.
5. Consulte o orçamento exibido no terminal e abra o arquivo PROJECAO_12_MESES.CSV gerado na pasta do programa.

		Exemplo de orçamento

	Entrada: casa, 2 quartos, 1 vaga de garagem e taxa contratual em 5 parcelas.

 Item | Valor 
 
 Aluguel-base | R$ 900,00 
 Adicional por segundo quarto | R$ 250,00 
 Garagem | R$ 300,00 
 Aluguel mensal | R$ 1.450,00 
 Taxa contratual | R$ 2.000,00 
 Parcelamento | 5 × R$ 400,00 
 Total previsto no primeiro mês | R$ 1.850,00 
 Total previsto para 12 meses | R$ 19.400,00 

O total anual inclui 12 aluguéis (R$ 17.400,00) e a taxa contratual uma única vez (R$ 2.000,00).

		Arquivo CSV

Após cada orçamento, o programa gera PROJECAO_12_MESES.CSV, contendo 12 registros mensais, além do cabeçalho, com as colunas:

 Mês | Aluguel(R$) | Taxa contratual(R$) | TOTAL (R$)

O arquivo utiliza ponto e vírgula ( ; ) como separador e valores monetários com vírgula decimal, para facilitar a abertura em planilhas configuradas para o padrão brasileiro. A taxa aparece apenas nos meses correspondentes ao parcelamento escolhido.

		Fluxograma

O fluxograma, em fase de finalização, representa o processo de orçamento, desde a seleção do imóvel e validação das entradas até os cálculos, a apresentação dos valores e a exportação do CSV. Ele será incluído na entrega.

		Testes realizados

	Foram verificados:

• Orçamentos de apartamento, casa e estúdio com diferentes características.
• Aplicação do desconto de 5% somente aos apartamentos elegíveis.
• Valores de estacionamento e quartos adicionais.
• Rejeição de escolhas inválidas no menu e na criação direta dos objetos.
• Parcelamento em três vezes, com ajuste da última parcela para evitar diferenças de centavos.
• Geração do CSV com a projeção dos 12 meses.




Estrutura prevista para a entrega:



RentSmart/
├── rentsmart.py
├── README.md
├── projecao_12_meses.csv
├── fluxograma_rentsmart.drawio
└── fluxograma_rentsmart.png



