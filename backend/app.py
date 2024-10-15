from flask import Flask, request, jsonify
from flask_cors import CORS  # Adicione essa linha
import os
import csv

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Função mock para simular o processamento OCR
def process_ocr(image):
    return {
        "data": {
            "nota_fiscal": "12345",
            "valor_total": "R$ 250,00",
            "data_emissao": "2024-10-10"
        }
    }

# Rota para receber a imagem e processar OCR
@app.route('/upload', methods=['POST'])
def upload_file():
    # Verifica se o arquivo de imagem foi enviado corretamente
    if 'nota-fiscal' not in request.files:
        return jsonify({"message": "Nenhuma imagem enviada"}), 400

    # Salva o arquivo de imagem enviado
    file = request.files['nota-fiscal']
    image_path = os.path.join('/output', file.filename)
    file.save(image_path)

    # Simulação do processamento OCR (você vai integrar isso depois)
    ocr_result = process_ocr(image_path)

    # Retorna uma resposta de sucesso
    return jsonify({"message": "Nota fiscal processada com sucesso!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

