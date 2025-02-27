import google.generativeai as genai

chave_api = ""

genai.configure(api_key=chave_api)

model = genai.GenerativeModel("gemini-pro")

historico = []

limite_historico = 10


def enviar_mensagem(mensagem):
    global historico

    historico.append({"role": "assistant", "content": mensagem})

    if len(historico) > limite_historico:
        historico.pop(0) # Remove a mensagem mais antiga

    # Envia todas as mensagens acumuladas para manter o contexto
    resposta = model.generate_content([m["content"] for m in historico if m["content"]])

    resposta_texto = resposta.text # Gemini retorna a resposta como string

    historico.append({"role": "assistant", "content": resposta_texto})

    return resposta_texto


while True:
    texto = input("Escreva aqui sua pergunta: ")

    if texto.lower() == "sair":
        break
    else:
        resposta = enviar_mensagem(texto)
        print("Chatbot: ", resposta)
