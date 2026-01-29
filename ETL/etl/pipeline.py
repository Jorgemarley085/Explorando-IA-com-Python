from etl.extract import extract_users
from etl.transform import gerar_mensagem
from etl.load import salvar_mensagem

def run_pipeline():
    users = extract_users()
    #print(df.columns)
    print(users)
    for _, user in users.iterrows():
        mensagem = gerar_mensagem(user["nome"],user["saldo"])
        salvar_mensagem(user["id"], mensagem)
    