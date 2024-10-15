# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos do backend para o container
COPY . /app

# Atualize o pip antes de instalar as dependências
RUN pip install --upgrade pip

# Instalar as dependências a partir do requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta 5000 para o backend Flask
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]

