import pywhatkit as kit
import pandas as pd
import re
from time import sleep
import datetime

def formatar_numero(numero):
    """Corrige números mantendo exatamente 11 dígitos após +55"""
    try:
        # Passo 1: Limpeza básica
        numero = str(numero).strip()
        numero = re.sub(r'[^0-9+]', '', numero)
        
        # Passo 2: Remove zeros finais problemáticos
        while len(numero) > 11 and numero.endswith('0'):
            numero = numero[:-1]
            
        # Passo 3: Remove 5's extras no início
        if numero.startswith('555'):
            numero = '55' + numero[3:]
        elif numero.startswith('55') and len(numero) > 11:
            numero = '55' + numero[2:] if numero[2] == '5' else numero
            
        # Passo 4: Formatação internacional
        if not numero.startswith('+'):
            numero = f"+55{numero.lstrip('55')}"
            
        # Passo 5: Validação rigorosa
        if not re.match(r'^\+55\d{11}$', numero):
            raise ValueError(f"Formato inválido. Esperado: +55DDDNNNNNNNN | Recebido: {numero}")
            
        return numero
        
    except Exception as e:
        print(f"❌ Erro na formatação: {str(e)}")
        return None

def carregar_contatos(caminho_planilha):
    """Carrega e valida os contatos da planilha"""
    try:
        df = pd.read_excel(caminho_planilha)
        
        # Verifica colunas obrigatórias
        if not {'numero', 'mensagem'}.issubset(df.columns):
            print("❌ Planilha deve conter colunas: 'numero' e 'mensagem'")
            return []
        
        # Processamento dos números
        df = df.dropna(subset=['numero', 'mensagem'])
        df['numero'] = df['numero'].apply(formatar_numero)
        df = df.dropna(subset=['numero'])
        
        return df.to_dict('records')
    except Exception as e:
        print(f"❌ Erro ao processar planilha: {str(e)}")
        return []

def enviar_mensagem(numero, mensagem, tentativas=2):
    """Envia mensagem com tempo de espera reduzido"""
    try:
        # Configura tempo de envio (1 minuto no futuro)
        now = datetime.datetime.now()
        hora = now.hour
        minuto = now.minute + 1
        
        for tentativa in range(tentativas):
            try:
                print(f"\n⚡ Tentativa {tentativa+1} para {numero}...")
                
                kit.sendwhatmsg(
                    phone_no=numero,
                    message=mensagem,
                    time_hour=hora,
                    time_min=minuto,
                    wait_time=8,    # Tempo reduzido para carregar
                    tab_close=False,
                    close_time=1    # Fecha rápido após enviar
                )
                
                print(f"✅ Enviado para {numero}")
                return True
                
            except Exception as e:
                print(f"⚠️ Erro: {str(e)}")
                sleep(5)  # Espera curta entre tentativas
                
        return False
        
    except Exception as e:
        print(f"❌ Falha crítica: {str(e)}")
        return False

if __name__ == "__main__":
    contatos = carregar_contatos("contatos.xlsx")
    
    if not contatos:
        print("❌ Nenhum contato válido encontrado")
    else:
        print(f"📊 Total de contatos válidos: {len(contatos)}")
        
        for contato in contatos:
            if enviar_mensagem(contato['numero'], contato['mensagem']):
                print(f"✔️ Sucesso: {contato['numero']}")
            else:
                print(f"❌ Falha: {contato['numero']}")
            
            sleep(2)  # Intervalo ultrarrápido entre contatos