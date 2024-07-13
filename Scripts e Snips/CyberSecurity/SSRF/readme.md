# Honeypot com Monitoramento e Testes SSRF

Este projeto implementa um honeypot para capturar tentativas de acesso maliciosas e monitorar essas atividades por meio de uma interface web. Além disso, inclui um conjunto de testes SSRF para avaliar a vulnerabilidade de redirecionamento de URL em diferentes técnicas de evasão.

## Resumo

O honeypot é configurado para rodar em um servidor HTTP simples que captura e registra todas as requisições recebidas. Se uma requisição suspeita for detectada, um alerta por email é enviado. O projeto também inclui um servidor Flask que fornece uma interface web para visualizar os logs das atividades do honeypot.

Adicionalmente, o projeto contém um script de teste SSRF que envia várias requisições para avaliar a segurança do honeypot contra ataques de redirecionamento de URL.

## Conceitos Aplicados

- **Configuração e uso de variáveis de ambiente** 
- **Log e monitoramento:** Configuração de logs detalhados usando o módulo `logging` e envio de alertas por email com `smtplib` e `email.mime.text.MIMEText` para notificar sobre atividades suspeitas.
- **Testes e requisições HTTP:** Uso de `httpx` e `requests` para enviar requisições HTTP, incluindo testes de SSRF com diferentes técnicas de evasão e cabeçalhos customizados para verificar a segurança contra redirecionamentos de URL.
- **Servidores e APIs:** Criação de um honeypot usando `http.server.SimpleHTTPRequestHandler` e configuração de um servidor Flask para fornecer uma interface web de monitoramento das atividades.

Este projeto fornece uma base robusta para monitoramento de atividades maliciosas e avaliação da segurança contra ataques SSRF, utilizando uma combinação de técnicas avançadas de programação e segurança.