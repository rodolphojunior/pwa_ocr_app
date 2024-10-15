# PWA OCR para Processamento de Notas Fiscais

Este projeto é um miniaplicativo PWA que permite o upload de imagens de notas fiscais para processamento OCR (Reconhecimento Óptico de Caracteres) e posterior armazenamento em um arquivo CSV. O backend é desenvolvido em Python com Flask e o frontend é construído em HTML, CSS, e JavaScript, usando [Pico.css](https://picocss.com/) para estilização.

## Requisitos

Certifique-se de ter o Docker e o Docker Compose instalados em seu sistema. Se não tiver, siga as instruções abaixo para instalá-los em um sistema **Linux Ubuntu**.

### Verificando se o Docker está instalado

Execute o comando a seguir no terminal para verificar se o Docker está instalado:

```bash
docker --version
```

Se o Docker estiver instalado, você verá a versão instalada. Caso contrário, siga os passos abaixo para instalar o Docker.

### Instalando o Docker no Ubuntu

1. **Atualize o sistema e instale dependências**:

   ```bash
   sudo apt update
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```

2. **Adicione a chave GPG do Docker**:

   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```

3. **Adicione o repositório Docker**:

   ```bash
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

4. **Instale o Docker**:

   ```bash
   sudo apt update
   sudo apt install docker-ce
   ```

5. **Verifique se o Docker está rodando**:

   ```bash
   sudo systemctl status docker
   ```

6. **(Opcional) Adicione o usuário ao grupo Docker** para evitar usar `sudo` em todos os comandos do Docker:

   ```bash
   sudo usermod -aG docker ${USER}
   ```

   **Logout e login** para aplicar a mudança.

### Instalando o Docker Compose

Verifique se o Docker Compose está instalado com o comando:

```bash
docker-compose --version
```

Se não estiver instalado, siga as etapas abaixo:

1. **Baixe a versão mais recente do Docker Compose**:

   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep 'tag_name' | cut -d'v' -f2 | tr -d '",')/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   ```

2. **Dê permissão de execução**:

   ```bash
   sudo chmod +x /usr/local/bin/docker-compose
   ```

3. **Verifique a instalação**:

   ```bash
   docker-compose --version
   ```

## Como Executar o Aplicativo

### Clonar o Repositório

Clone o repositório do projeto para o seu ambiente local:

```bash
git clone <URL_DO_REPOSITORIO>
cd pwa_ocr_app
```

### Rodar o Aplicativo com Docker Compose

1. **Suba os containers** com o comando:

   ```bash
   docker-compose up --build
   ```

   Isso vai construir e rodar o backend e o frontend em containers separados.

2. **Acesse o frontend** no navegador:

   Abra o navegador e acesse `http://127.0.0.1:8080` para carregar a interface do usuário.

### Envio de Imagens

1. No navegador, use o formulário exibido para **tirar uma foto** da nota fiscal ou selecionar um arquivo de imagem existente no seu dispositivo.
   
2. Clique no botão **Enviar** para processar a imagem e enviar a nota fiscal para o backend, onde será analisada com OCR e salva como um registro no CSV.

3. O status da operação será exibido na tela.

## Estrutura do Projeto

```
pwa_ocr_app/
├── backend/                 # Backend em Python (Flask)
│   ├── app.py               # Código do backend
│   ├── Dockerfile           # Dockerfile para o backend
│   ├── requirements.txt     # Dependências do backend
│   └── output/              # Diretório para salvar os CSVs
├── frontend/                # Frontend PWA
├── Dockerfile               # Dockerfile para o frontend
├── icons/                   # Icons obrigatórios
│   ├── icon-192x192.png
│   └── icon-512x512.png
├── index.html               # Página HTML principal
├── manifest.json            # Manifest define como o aplicativo deve ser exibido quando instalado 
├── scripts.js               # Lógica JavaScript
├── service-worker.js        # Service Worker é responsável por controlar o comportamento offline
└── styles.css   
├── docker-compose.yml       # Arquivo Docker Compose para orquestração
└── README.md                # Documentação do projeto

```

## Problemas Comuns

- **Erro de Permissões no Docker**: Se você encontrar problemas de permissão ao rodar o Docker, certifique-se de que seu usuário está no grupo Docker (veja a seção sobre adicionar o usuário ao grupo Docker).
  
- **Erro de Upload de Arquivos**: Caso o upload de imagens falhe, verifique os logs do backend executando:

   ```bash
   docker-compose logs web
   ```

## Próximos Passos

- Implementar melhorias no processamento OCR.

- Melhorar a interface do usuário para dar feedback durante o upload e processamento das notas fiscais.

- Para que o PWA funcione completamente (incluindo o recurso de instalação), ele precisa estar rodando em HTTPS. Para testes locais, o navegador permite localhost sem HTTPS, mas para produção você precisará de um servidor HTTPS.

- O Dockerfile atual do frontend pode continuar usando o servidor HTTP básico, mas para um ambiente de produção, seria interessante configurar algo como Nginx com SSL.

## Contribuindo

Pull requests são bem-vindos! Para mudanças maiores, abra uma issue para discutirmos o que você gostaria de modificar.

---

Este README cobre os pontos essenciais e permite que qualquer desenvolvedor ou usuário configure o ambiente e execute o projeto sem grandes problemas. Conforme o desenvolvimento progride, você pode adicionar mais seções detalhadas, como melhorias nas instruções de instalação e uso.

Me avise se quiser fazer alguma alteração ou adicionar mais detalhes!
