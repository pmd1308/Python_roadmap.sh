# Trojan Python

Fiz esse script para aprender como codar um trojan, que executa um ransomware que rouba arquivos, além de mandar dados da rede que o dispositivo alvo está para o atacante. Esse script não é funcional, mas pelo menos me ajudou a entender a logica por trás de vetorização, criptografia e engenharia social, coisas que me deixam de *** duro (amo matematica) kkkkkk.

## Visão Geral

Implementei três tecnicas:

1. **Ransomware**: Criptografa arquivos importantes e exige um resgate.
2. **Trojan**: Coleta informações do sistema e as envia para um servidor remoto.
3. **Bomba Lógica**: Executa ações maliciosas após um período específico.

No final acabei entendendo como são capturados os dados, e repito, no mundo real o script seria mais complexo. Esse script é 100% didático, e se eu realmente quisesse fazer um estrago, o trabalho seria mais complexo, pois teria que entrar em foruns mais brisa errada da internet, e participar de chats na Dark Web, é dahora, mas ao mesmo tempo meio paia de fazer kkkkkk.

## Funcionalidades

### 1. Ransomware

O componente de ransomware criptografa arquivos importantes no sistema da vítima. Usei AES no modo CFB, além de ter usando um vetor de inicialização para garantir a unanimidade das chaves.

### 2. Trojan

O trojan coleta informações do sistema da vítima e as envia para um servidor remoto. Decidi coletar algumans informações uteis usando pacotes terceiros, além da solicitação para uma API ficticia. E estou ligado que poderia usar o Burp Suit para ver quais as urls internas poderia tentar solicitar dados, e através dessa lista, iterar cada item para fazer uma solicitação unica, e uma vez sabendo, poderia organizar um DDOS, caso implementa-se um backdoor, mas como eu disse, é 100% educacional.

### 3. Bomba Lógica

A bomba lógica verifica uma data e hora específicas para acionar o ataque do ransomware.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```plaintext
src
├── trojan
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── utils.py
│
├── .env
└── requirements.txt
```