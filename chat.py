#𝐅𝐄𝐈𝐓𝐎 𝐏𝐎𝐑 𝐕𝐈𝐍𝐈𝐂𝐈𝐔𝐒 𝐒𝐀𝐍𝐓𝐎𝐒-𝐓𝐄𝐂𝐇

from openai import OpenAI

client = OpenAI(api_key=" ------------------------------")  #CHAVE API!

instructions = "Você é quem vai responder as diversas perguntas enviadas aqui."

def chat():
    print("Digite sua mensagem ou 'sair' para encerrar.")

    while True:
        Mensagem = input("Você: ")

        if Mensagem.lower() in ["sair", "exit", "quit"]:
            print("Encerrando...")
            break

        resposta = client.responses.create(
            model="gpt-4o-mini",
            instructions=instructions,
            input=[
                {"role": "user", "content": Mensagem}
            ]
        )

        print("IA:", resposta.output_text)

chat()
