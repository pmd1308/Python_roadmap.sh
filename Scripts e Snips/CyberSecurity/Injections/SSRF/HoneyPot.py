import http.server
import socketserver
import logging
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template_string
import threading
import urllib.parse

PORT = 8000
LOG_FILE = 'honeypot.log'

# Configurando o logger
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

# Função para enviar alertas por email
def send_alert(message):
    sender = "seu_email@example.com"
    receiver = "destinatario@example.com"
    msg = MIMEText(message)
    msg['Subject'] = "Alerta do Honeypot"
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender, 'sua_senha')
        server.sendmail(sender, receiver, msg.as_string())

# Função para verificar se a requisição é maliciosa
def is_malicious_request(path, headers):
    suspicious_keywords = ['internal', 'admin', 'sensitive', 'redirect', 'file', 'url']
    decoded_path = urllib.parse.unquote(path)
    
    for keyword in suspicious_keywords:
        if keyword in decoded_path or keyword in headers:
            return True
    return False

# Handler do honeypot
class HoneyPotHandler(http.server.SimpleHTTPRequestHandler):
    def log_request(self, code='-', size='-'):
        client_ip = self.client_address[0]
        request_path = self.path
        headers = str(self.headers)
        
        log_message = f"Requisição de {client_ip} para {request_path} com headers:\n{headers}"
        logging.info(log_message)
        
        if is_malicious_request(request_path, headers):
            send_alert(log_message)

    def do_GET(self):
        self.log_request()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, this is a honey pot!")
    
    def do_POST(self):
        self.log_request()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, this is a honey pot!")
    
    def do_PUT(self):
        self.log_request()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, this is a honey pot!")
    
    def do_DELETE(self):
        self.log_request()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, this is a honey pot!")
    
    def do_OPTIONS(self):
        self.log_request()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, this is a honey pot!")

# Configuração do servidor Flask para monitoramento
app = Flask(__name__)

@app.route('/')
def home():
    with open(LOG_FILE, 'r') as file:
        logs = file.read().split('\n')
    return render_template_string('''<html><body><h1>Honeypot Logs</h1><pre>{{ logs }}</pre></body></html>''', logs='\n'.join(logs))

def run_honeypot_server():
    with socketserver.TCPServer(("", PORT), HoneyPotHandler) as httpd:
        print(f"Servindo no porto {PORT}")
        httpd.serve_forever()

if __name__ == '__main__':
    threading.Thread(target=run_honeypot_server).start()
    app.run(port=5000)
