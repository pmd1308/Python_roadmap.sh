import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_data(filename):
    """
    - Limpar dados do dataset coletado
    - Parametros: data/raw/audit_dataset.csv
    """
    if filename.isnull().sum().sum() > 0:
        logging.warning(f'Missing values detected in {filename}')
        return None

    filename['amount'] = filename['amount'].apply(lambda x: x if x > 0 else None) # remove valores negativos
    filename.dropna(subset=['amount'], inplace=True) #Remove linhas com valores nulos no campo amount

    return filename

def process_data():
    """
    - Criação do arquivo a ser estudado
    - Parametros: data/raw/audit_dataset.csv
    """
    file = pd.read_csv('data/raw/audit_dataset.csv')

    if file is not None:        
            file = clean_data(file)
            os.makedirs('data/procesed', exist_ok=True)
            file.to_csv('data/processed/processed_audit_data.csv', index=False)
            logging.info('Data processing completed successfully')
    else:
         logging.error('file not found')

if __name__ == '__main__':
     process_data()