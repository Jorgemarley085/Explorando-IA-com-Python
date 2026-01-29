from database.database import engine

def salvar_mensagem(user_id, mensagem):
    with engine.begin() as conn:
        conn.execute(
            "UPDATE usuarios SET news = %s WHERE id = %s",
            (mensagem, user_id)
        )
