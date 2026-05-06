import pandas as pd
from sqlalchemy import create_engine, text

# 1. Conexão (Ajustado para o banco padrão 'postgres' onde você tem permissão total)
engine = create_engine('postgresql://postgres:2090@localhost:5432/postgres')

# 2. SQL de Criação e Inserção (Garante que o ambiente esteja pronto)
setup_query = """
CREATE TABLE IF NOT EXISTS inventario_ti (
    id SERIAL PRIMARY KEY,
    ativo_nome VARCHAR(100),
    categoria VARCHAR(50),
    departamento VARCHAR(50),
    custo_mensal_usd NUMERIC(10, 2),
    status VARCHAR(20),
    data_aquisicao DATE
);

TRUNCATE TABLE inventario_ti; -- Limpa para não duplicar dados no teste

INSERT INTO inventario_ti (ativo_nome, categoria, departamento, custo_mensal_usd, status, data_aquisicao) VALUES
('Servidor-Dell-R740', 'Servidor Físico', 'TI', 450.00, 'Ativo', '2024-01-15'),
('Instancia-Prod-Web', 'Cloud EC2', 'Marketing', 120.00, 'Ativo', '2025-05-01'),
('Switch-Cisco-2960', 'Switch', 'Redes', 80.00, 'Ativo', '2023-11-20'),
('DB-Aurora-Postgres', 'Cloud RDS', 'Financeiro', 350.00, 'Ativo', '2026-02-10'),
('Storage-Backup-Local', 'Servidor Físico', 'TI', 200.00, 'Manutenção', '2024-06-12');
"""

with engine.connect() as conn:
    conn.execute(text(setup_query))
    conn.commit()

# 3. ETL e Consulta (Experiência com consumo de dados em bancos relacionais)
query = "SELECT * FROM inventario_ti WHERE status = 'Ativo'"
df = pd.read_sql(query, engine)

# 4. Lógica de Negócio (Projeção de Custos 2026)
df['projeção_custo_2026'] = df['custo_mensal_usd'] * 1.15

# 5. Exportação (Workflow automatizado)
df.to_csv('C:/Git/inventario_processado.csv', index=False)
print("Sucesso! Tabela criada/atualizada e CSV gerado em C:/Git/")