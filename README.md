Este projeto foi desenvolvido para centralizar a gestão de ativos de hardware e serviços em nuvem, permitindo o controle financeiro e a previsão orçamentária para os próximos anos.

1. Extração e Tratamento de Dados (ETL)
Banco de Dados (PostgreSQL): Os dados brutos de inventário, incluindo custos e datas de aquisição, foram extraídos de um ambiente relacional estruturado.

Linguagem Python: Foi utilizado o Python para realizar o processo de ETL (Extract, Transform, Load). Através de scripts, conectamos ao banco, limpamos os dados e aplicamos uma regra de negócio para calcular a Projeção de Custos 2026, prevendo um aumento de 15% nos gastos de infraestrutura.

2. Modelagem de Dados no Power BI
Modelagem Tabular (Star Schema): Foi criada uma tabela de dimensão de datas (dCalendario) via linguagem M no Power Query para garantir a integridade das análises temporais.

Relacionamentos: Estabelecemos um relacionamento do tipo 1:N (Um para Muitos) entre a dCalendario e a tabela de fatos inventario_processado, permitindo filtros dinâmicos por ano e mês.

3. Inteligência de Dados com DAX
Foram desenvolvidas medidas personalizadas para gerar insights rápidos e precisos:

Total Custo Mensal: Uma soma agregada de todos os ativos para visão macro do orçamento.

Custo Cloud: Utilização da função CALCULATE para filtrar especificamente gastos com serviços de nuvem (AWS EC2 e RDS), destacando a especialização em Cloud Computing.

Projeção Total 2026: Medida para consolidar a previsão orçamentária futura calculada previamente.

4. Visualização e Dashboards
KPIs (Cartões): Exibição clara dos valores monetários formatados para tomada de decisão imediata.

Análise de Composição (Gráfico de Rosca): Divisão visual entre custos de infraestrutura física (On-Premise) e serviços em nuvem (Cloud).

Segmentação de Dados: Filtros interativos que permitem ao gestor navegar entre os anos de 2024 e 2026 para acompanhar a evolução dos gastos.....
