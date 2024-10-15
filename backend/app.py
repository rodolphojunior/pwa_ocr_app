from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from process_ocr import Phi3VisionModel  # Importa a classe OCR do arquivo process_ocr

app = Flask(__name__)
# Habilita CORS para todas as rotas e todas as origens
CORS(app, resources={r"/*": {"origins": "*"}})

# Inicializa o modelo Phi-3 Vision para OCR
phi_model = Phi3VisionModel(device="cpu")  # Usar "cpu" ou "cuda" conforme o hardware disponível

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

    # Prompt personalizado para a extração de dados da nota fiscal
    prompt = """
    Por favor, extraia os seguintes campos da nota fiscal:
    - Data da emissão
    - Valor total
    - CNPJ da empresa
    - Número da nota
    - Nome da empresa
    """

    # Processa o OCR utilizando a imagem salva
    ocr_result = phi_model.predict(image_path, prompt)

    # Retorna uma resposta de sucesso com os dados extraídos
    return jsonify({"message": "Nota fiscal processada com sucesso!", "dados_extraidos": ocr_result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
