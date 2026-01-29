from sqlalchemy import create_engine

DATABASE_URL="postgresql://postgres:250175@localhost:5432/santander"

engine = create_engine(DATABASE_URL)

def get_engine():
    return engine