#𝐅𝐄𝐈𝐓𝐎 𝐏𝐎𝐑 𝐕𝐈𝐍𝐈𝐂𝐈𝐔𝐒 𝐒𝐀𝐍𝐓𝐎𝐒-𝐓𝐄𝐂𝐇
#𝐂𝐇𝐀𝐓𝐁𝐎𝐓.V2
from openai import OpenAI
import customtkinter as ctk

historico = []
client = OpenAI(api_key="*********************") #𝗗𝗜𝗚𝗜𝗧𝗘 𝗦𝗨𝗔 𝗖𝗛𝗔𝗩𝗘 𝗔𝗤𝗨𝗜!
instructions = "Responda as perguntas, porem da forma mais curta possivel. Caso O cliente fale algo proibido, ou que abra Qualquer sentido para partes intimas e sexuais, fale que nao pode ajudar com isso."

def enviar_mensagem():
    mensagem = entrada.get()
    
    if mensagem.strip():
        caixa_texto.insert("end", f"Você: {mensagem}\n")
        entrada.delete(0, "end")
        historico.append({"role": "user", "content": mensagem})
        
        resposta = client.responses.create(
            model="gpt-4o-mini",
            instructions=instructions,
            input=historico
        )
        caixa_texto.insert("end", f"IA: {resposta.output_text}\n\n")
        historico.append({"role": "assistant", "content": resposta.output_text})

        caixa_texto.see("end")

Tela = ctk.CTk()
ctk.set_appearance_mode('dark')
Tela.geometry("400x400")
Tela.resizable(False, False)
Tela.title("ChatGPT - Vinicius Santos-Tech")

Texto = ctk.CTkLabel(Tela, text='Bem Vindo ao Chat!', font=("Arial", 16, "bold"))
Texto.pack(pady=10)
#----------------------------
caixa_texto = ctk.CTkTextbox(Tela, width=360, height=300)
caixa_texto.pack(pady=10)
#----------------------------
entrada = ctk.CTkEntry(Tela, width=360, placeholder_text="Digite sua pergunta...", font=("Arial", 16))
entrada.pack(pady=5)
#----------------------------
botao_enviar = ctk.CTkButton(Tela, text="Enviar", command=enviar_mensagem)
botao_enviar.pack(pady=5)
def enviar_enter(event):
    enviar_mensagem()

Tela.bind('<Return>', enviar_enter)

Tela.mainloop()
