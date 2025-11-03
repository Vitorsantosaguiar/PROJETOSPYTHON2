import pywhatkit as kit
import pandas as pd
import re
from time import sleep, time
import datetime
import logging
import urllib.request

# Solução para a importação das exceções
try:
    from pywhatkit.exceptions import WhatsAppException
except ImportError:
    print("⚠️ Usando fallback para WhatsAppException")
    class WhatsAppException(Exception):
        pass

# Configuração de logging
logging.basicConfig(
    filename='whatsapp_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

# Controle de taxa de envio
ULTIMO_ENVIO = 0
INTERVALO_MINIMO = 2  # segundos

def verificar_conexao():
    """Verifica se há conexão com a internet"""
    try:
        urllib.request.urlopen('http://google.com', timeout=5)
        return True
    except:
        logging.warning("Sem conexão com a internet")
        return False

def formatar_numero(numero):
    """Corrige números mantendo formato internacional"""
    try:
        numero = str(numero).strip()
        numero = re.sub(r'[^0-9+]', '', numero)
        
        # Remove zeros finais
        while len(numero) > 11 and numero.endswith('0'):
            numero = numero[:-1]
            
        # Remove 5's extras
        if numero.startswith('555'):
            numero = '55' + numero[3:]
        elif numero.startswith('55') and len(numero) > 11:
            numero = '55' + numero[2:] if numero[2] == '5' else numero
            
        # Formatação internacional
        if not numero.startswith('+'):
            numero = f"+55{numero.lstrip('55')}"
            
        # Validação final
        if not re.match(r'^\+55\d{11}$', numero):
            raise ValueError(f"Formato inválido: {numero}")
            
        return numero
        
    except Exception as e:
        logging.error(f"Erro ao formatar número: {str(e)}")
        return None

def carregar_contatos(caminho_planilha):
    """Carrega e valida os contatos da planilha"""
    try:
        df = pd.read_excel(caminho_planilha)
        
        if not {'numero', 'mensagem'}.issubset(df.columns):
            logging.error("Planilha sem colunas obrigatórias")
            return []
        
        df = df.dropna(subset=['numero', 'mensagem'])
        df['numero'] = df['numero'].apply(formatar_numero)
        df = df.dropna(subset=['numero'])
        
        logging.info(f"Carregados {len(df)} contatos válidos")
        return df.to_dict('records')
    except Exception as e:
        logging.critical(f"Erro ao carregar planilha: {str(e)}")
        return []

def enviar_mensagem(numero, mensagem, tentativas=2):
    """Envia mensagem com todas as otimizações"""
    global ULTIMO_ENVIO
    
    try:
        if not verificar_conexao():
            return False

        # Controle de taxa de envio
        agora = time()
        if agora - ULTIMO_ENVIO < INTERVALO_MINIMO:
            sleep(INTERVALO_MINIMO - (agora - ULTIMO_ENVIO))
        ULTIMO_ENVIO = time()
        
        now = datetime.datetime.now()
        for tentativa in range(tentativas):
            try:
                logging.info(f"Enviando para {numero} (Tentativa {tentativa+1})")
                
                kit.sendwhatmsg(
                    phone_no=numero,
                    message=mensagem,
                    time_hour=now.hour,
                    time_min=now.minute + 1,
                    wait_time=8,
                    tab_close=False,
                    close_time=1
                )
                
                logging.info(f"Sucesso: {numero}")
                print(f"✅ Enviado para {numero}")
                return True
                
            except WhatsAppException as e:
                logging.warning(f"Erro WhatsApp (Tentativa {tentativa+1}): {str(e)}")
                print(f"⚠️ Erro WhatsApp: {str(e)}")
                sleep(5)
            except Exception as e:
                logging.error(f"Erro inesperado (Tentativa {tentativa+1}): {str(e)}")
                print(f"⚠️ Erro: {str(e)}")
                sleep(5)
                
        logging.warning(f"Falha após {tentativas} tentativas: {numero}")
        return False
        
    except Exception as e:
        logging.critical(f"Falha crítica: {str(e)}")
        print(f"❌ Falha crítica: {str(e)}")
        return False

if __name__ == "__main__":
    print("Iniciando WhatsApp Bot...")
    logging.info("Iniciando execução")
    
    contatos = carregar_contatos("contatos.xlsx")
    
    if not contatos:
        print("❌ Nenhum contato válido encontrado")
        logging.warning("Nenhum contato válido")
    else:
        print(f"📊 Total de contatos válidos: {len(contatos)}")
        
        for contato in contatos:
            if enviar_mensagem(contato['numero'], contato['mensagem']):
                print(f"✔️ Sucesso: {contato['numero']}")
            else:
                print(f"❌ Falha: {contato['numero']}")
            
            sleep(2)
    
    logging.info("Execução concluída")
    print("✅ Processo finalizado")