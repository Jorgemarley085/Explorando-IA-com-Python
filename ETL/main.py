from etl.pipeline import run_pipeline
from dotenv import load_dotenv
load_dotenv()
if __name__ == "__main__":
    run_pipeline()


import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        user="postgres",
        password="250175",
        dbname="santander"
    )
    print("✅ Conectado direto com psycopg2")
    conn.close()
except Exception as e:
    print("❌ Erro:", e)





# from sqlalchemy import create_engine

# DATABASE_URL = "postgresql://postgres:250175@localhost:5432/santander"

# engine = create_engine(DATABASE_URL)

# try:
#     with engine.connect() as conn:
#         print("✅ Conectado com sucesso!")
# except Exception as e:
#     print("❌ Erro ao conectar:")
#     print(e)
