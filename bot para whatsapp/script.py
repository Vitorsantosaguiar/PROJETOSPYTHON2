import pywhatkit as kit
import datetime
from time import sleep

# Configurações (pode ser movido para um arquivo .env depois)
CONFIG = {
    "NUMERO_DESTINO": "+5511983650773",
    "MENSAGEM_PADRAO": "Olá! Esta é uma mensagem automática enviada via WhatsApp.",
    "TEMPO_ESPERA": 15  # segundos
}

def enviar_mensagem_whatsapp(numero, mensagem, tentativas=2):
    """Envia mensagem via WhatsApp com tratamento de erros"""
    hora = datetime.datetime.now().hour
    minuto = datetime.datetime.now().minute + 2
    
    for tentativa in range(tentativas):
        try:
            kit.sendwhatmsg(numero, mensagem, hora, minuto, wait_time=15, tab_close=True)
            sleep(CONFIG["TEMPO_ESPERA"])
            return True
        except Exception as e:
            print(f"Tentativa {tentativa+1} falhou: {str(e)}")
            sleep(30)
    return False

if __name__ == "__main__":
    try:
        print("Iniciando envio de mensagem...")
        if enviar_mensagem_whatsapp(CONFIG["NUMERO_DESTINO"], CONFIG["MENSAGEM_PADRAO"]):
            
            print("✅ Mensagem enviada com sucesso!")
        else:
            print("❌ Falha ao enviar mensagem após múltiplas tentativas")
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário")
    except Exception as e:
        print(f"Erro crítico: {str(e)}")