# Chatbot com Gemini API

Este é um projeto de teste utilizando a API Gemini da Google para criar um chatbot básico. Ele permite interagir com um modelo de IA que gera respostas com base no histórico da conversa.

## Requisitos

- Python 3.x
- Biblioteca `google-generativeai`

## Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. Instale as dependências necessárias:
   ```sh
   pip install google-generativeai
   ```
3. Obtenha uma chave de API do Google Gemini e substitua `chave_api` no código.

## Uso

1. Execute o script:
   ```sh
   python chatbot.py
   ```
2. Digite suas perguntas no terminal e obtenha respostas da IA.
3. Para sair, digite `sair`.

## Como Funciona

- O histórico de mensagens é armazenado em uma lista para manter o contexto da conversa.
- Apenas as últimas 10 mensagens são mantidas.
- O chatbot usa o modelo `gemini-pro` para gerar respostas.


