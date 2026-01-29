import pandas as pd
from database.database import get_engine

engine = get_engine()
def extract_users():
    query = "SELECT id, nome, email,saldo FROM usuarios"
    return pd.read_sql(query, engine)
#df_usuarios= pd.read_sql("SELECT * FROM usuarios",engine)

# print(df_usuarios)