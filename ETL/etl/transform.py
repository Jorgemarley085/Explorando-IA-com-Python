# import os
# from dotenv import load_dotenv
# import cohere

# load_dotenv()


# co = cohere.Client(os.getenv("COHERE_API_KEY"))


# def gerar_mensagem(nome, saldo):
#     prompt = f"Crie uma mensagem curta, amigável e profissional incentivando {nome} a investir melhor seu dinheiro. Saldo atual: R${saldo:.2f}."
    
#     try:
#         response = co.chat(
#             model="command-light-nightly",  # modelo recomendado atual
#             message=prompt,                    # <<< aqui é query, não messages
#             #max_output_tokens=80,
#             temperature=0.7
#         )

#         return response.output[0].content[0].text.strip()  # caminho correto na resposta

#     except Exception as e:
#         print(f"⚠️ Erro ao gerar mensagem para {nome}: {e}")
#         return f"Olá {nome}, considere investir seu saldo de R${saldo:.2f} para potencializar seus ganhos!"











# import os
# from dotenv import load_dotenv
# import cohere

# load_dotenv()

# co = cohere.Client(os.getenv("COHERE_API_KEY"))

# def gerar_mensagem(nome, saldo):
#     messages =[
#         {"role": "system", "content": "Você é um assistente amigável e profissional para gerar mensagens de investimento."},
#         {"role": "user", "content": f"Crie uma mensagem curta, amigável e profissional incentivando {nome} a investir melhor seu dinheiro. Saldo atual: R${saldo:.2f}."}
#     ]

#     response = co.chat(
#         model="command",  # modelo principal da Cohere
#         messages=messages,
#         max_tokens=80,
#         temperature=0.7
#     )

#     return response.choices[0].message["content"].strip()











# from dotenv import load_dotenv
# from google import genai
# import os



# load_dotenv()
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# #model = genai.GenerativeModel("gemini-1.5-flash")

# # client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def gerar_mensagem(nome,saldo):
#     prompt = f"""Esta na hora de investir {nome} o seu dinheiro. Saldo atual: R${saldo}"""

#     response = client.models.generate_content(
#         model="gemini-1.0-pro",
#         contents=prompt
#     )
#     return response.text.strip()






    # response =client.chat.completions.create(
    #     model = "gpt-4o-mini",
    #     messages=[{"role":"user","content":prompt}]

    # )
    # return response.choices[0].message.content.strip()




import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Cria o cliente usando a variável de ambiente
client = OpenAI()

def gerar_mensagem(nome, saldo):
    prompt = f"""
    Você é um especialista em marketing bancário.
    Crie uma mensagem curta e clara incentivando {nome} a investir melhor seu dinheiro.
    Saldo atual: R${saldo:.2f}.
    """

    # Chamada ao modelo
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # modelo mais leve e com custo baixo
        messages=[
            {"role": "system", "content": "Você é um assistente amigável para geração de mensagens."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )

    # Retorna apenas o texto da resposta
    return response.choices[0].message.content.strip()
