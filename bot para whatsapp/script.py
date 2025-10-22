import pywhatkit as kit
import datetime
from time import sleep

numero = "+5511999999999"  # Substitua pelo número de telefone desejado

mensagem = "Olá! Esta é uma mensagem automática enviada via WhatsApp."

hora_atual = datetime.datetime.now().hour

minuto_atual = datetime.datetime.now().minute + 2  # Enviar a mensagem em 2 minutos

kit.sendwhatmsg(numero, mensagem, hora_atual, minuto_atual)

sleep(15)  # Espera 15 segundos para garantir que o WhatsApp Web carregue

# Informar ao usuário que a mensagem está sendo enviada
print('Aguarde... A mensagem será enviada em breve!')

kit.sendwhatmsg(numero, mensagem, hora_atual, minuto_atual)

print('Mensagem enviada com sucesso!')