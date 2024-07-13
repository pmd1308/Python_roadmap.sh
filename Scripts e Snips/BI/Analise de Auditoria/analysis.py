import pandas as pd
import os
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def trainmodel():
    """"
    Treina um modelo de Isolation Forest para detectção de anomalias e salva os resultados.

    Esta função carrega dados processados em um arquivo CSV, treina um modelo Isolation Forest para detectção de anomalias, e salva o modelo treinado e os dados com as anomalias identificadas. Também divide os dados em conjuntos de treinamento e teste, treina o modelo RandomForestClassifier para avaliação e salva um relatorio de classificação.

    Isolation Forest:
    - É um método de aprendizado não supervisionado para detectar anomalias. O algoritmo constroi varias arvores de isolamento, onde observações anômalas são isoladas com menos divisões (menos profundidade). A profundeza media é usada para calcular a pontuação de anomalia

    Salva:
    - 'data/models/audit_model.pkl': Modelo Isolation Forest treinado.
    - 'data/processed/processed_audit_data_with_anomalies.csv': Dados com as anomalias identificadas.
    - 'data/models/classification_report.txt': Relatório de classificação do RandomForestClassifier.

    """

    if not os.path.isfile('data/processed/processed_audit_data.csv'):
        logging.error("Processed audit data not found. Please run preprocess_data.py first.")
        return None
    
    df = pd.read_csv('data/processed/processed_audit_data.csv')
    X = df.drop(columns=['year', 'month', 'day'])

    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(X)
    df['anomaly'] = model.predict(X)
    df['anomaly'] = df['anomaly'].apply(lambda x: 1 if x == -1 else 0) # Conversão para valores binarios

    os.makedirs('data/models', exist_ok=True)
    joblib.dump(model, 'data/models/audit_model.pkl') # Salvamento do modelo
    df.to_csv('data/processed/processed_audit_data_with_anomalies.csv', index=False)
    logging.info("Isolation Forest model trained and saved.")

    #relatorio de Classificação
    X_train, X_test, y_train, y_test = train_test_split(X, df['anomaly'], test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    with open('data/models/classification_report.txt', 'w') as file:
        file.write(classification_report(y_test, y_pred))
    logging.info("Classification report saved.")

if __name__ == '__main__':
    trainmodel()
