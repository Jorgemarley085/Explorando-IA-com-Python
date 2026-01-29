import pandas as pd
from sqlalchemy import text
from database.database import get_engine

engine = get_engine()

dados = pd.DataFrame([
    {"nome": "João Silva", "email": "joao@email.com", "saldo": 1500},
    {"nome": "Maria Souza", "email": "maria@email.com", "saldo": 3200},
    {"nome": "Carlos Lima", "email": "carlos@email.com", "saldo": 800},
    {"nome": "Ana Costa", "email": "ana@email.com", "saldo": 5400},
    {"nome": "Pedro Alves", "email": "pedro@email.com", "saldo": 1200}

])

dados.to_sql("usuarios",engine,if_exists="append", index=False)