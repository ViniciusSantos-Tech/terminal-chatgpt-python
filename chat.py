#𝐅𝐄𝐈𝐓𝐎 𝐏𝐎𝐑 𝐕𝐈𝐍𝐈𝐂𝐈𝐔𝐒 𝐒𝐀𝐍𝐓𝐎𝐒-𝐓𝐄𝐂𝐇
#𝐂𝐇𝐀𝐓𝐁𝐎𝐓
from openai import OpenAI

client = OpenAI(api_key="edrftghujtfrftgyhujiuhygtfrdftgy")  # COLOQUE SUA CHAVE AQUI!

instructions = "Responda as perguntas, porem da forma mais curta possivel."
historico =[]
def chat():
    print("Digite sua mensagem ou 'sair' para encerrar.")

    while True:
        Mensagem = input("Você: ")

        if Mensagem.lower() in ["sair", "exit", "quit"]:
            print("Encerrando...")
            break
        historico.append({"role": "user", "content": Mensagem})

        resposta = client.responses.create(
            model="gpt-4o-mini",
            instructions=instructions,
            input=history
        )

        print("IA:", resposta.output_text)
        
        history.append({"role": "assistant", "content": resposta.output_text})

chat()
