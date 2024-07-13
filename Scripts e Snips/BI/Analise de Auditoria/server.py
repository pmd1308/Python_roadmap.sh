from flask import Flask, send_file
import shutil
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/download')
def download_file():
    if not os.path.isdir('reports'):
        logging.error('O diretório de relatórios não foi encontrado.')
        return "Relatórios não encontrados", 404
    
    shutil.make_archive('reports', 'zip', 'reports')
    logging.info('Reports zipped and ready for download.')
    return send_file('reports.zip', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
