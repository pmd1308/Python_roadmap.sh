import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_visualizations():
    if not os.path.isfile('data/processed/processed_audit_data_with_anomalies.csv'):
        logging.error('O arquivo de dados com anomalias não foi encontrado.')
        return
    
    df = pd.read_csv('data/processed/processed_audit_data_with_anomalies.csv')
    
    os.makedirs('reports/graphs', exist_ok=True)
    
    plt.figure(figsize=(10, 6))
    sns.histplot(df['total_amount'], bins=50, kde=True)
    plt.title('Distribuição dos Montantes das Transações')
    plt.savefig('reports/graphs/transaction_amount_distribution.png')
    plt.close()
    
    plt.figure(figsize=(10, 6))
    sns.countplot(x='transaction_type', data=df)
    plt.title('Número de Transações por Tipo')
    plt.savefig('reports/graphs/transactions_by_type.png')
    plt.close()
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='year', y='total_amount', hue='anomaly', data=df, palette={0: 'blue', 1: 'red'})
    plt.title('Anomalias Detectadas')
    plt.savefig('reports/graphs/anomalies_detected.png')
    plt.close()
    
    logging.info('Visualizations successfully generated.')

if __name__ == "__main__":
    generate_visualizations()
