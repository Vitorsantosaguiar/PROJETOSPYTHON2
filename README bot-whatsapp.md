Explicação do Script Atualizado
Este é um bot profissionalizado para envio de mensagens automáticas no WhatsApp. Aqui está sua estrutura:

Configurações (linhas 5-9):
NUMERO_DESTINO: Número de telefone (você alterou para "+55119836507")
MENSAGEM_PADRAO: Texto da mensagem
TEMPO_ESPERA: 15 segundos para carregar o WhatsApp Web
Função principal (linhas 11-22):
enviar_mensagem_whatsapp()
:
Recebe número, mensagem e número de tentativas
Tenta enviar 2 vezes (padrão) com intervalo de 30s
Retorna True se sucesso, False se falhar
Execução (linhas 24-33):
Bloco principal (if __name__ == "__main__")
Trata:
Interrupção manual (Ctrl+C)
Erros críticos
Mostra status com emojis (✅/❌)
Fluxo de operação:

Pega hora atual + 2 minutos para agendamento
Tenta enviar a mensagem
Se falhar, espera 30s e tenta novamente
Informa o resultado final
Diferenciais da versão atual:

Código modularizado
Melhor tratamento de erros
Configuração centralizada
Feedback visual melhorado
