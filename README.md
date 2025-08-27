# AutoU Case

Uma aplicação FastAPI que utiliza a API Gemini do Google para classificar emails e sugerir respostas profissionais. A aplicação pode processar texto diretamente ou extrair texto de arquivos TXT e PDF enviados.

## Funcionalidades

- Classificação de emails (Produtivo vs. Improdutivo)
- Sugestões de respostas profissionais
- Suporte para entrada direta de texto
- Suporte para upload de arquivos TXT e PDF
- Interface limpa e responsiva com Tailwind CSS

## Pré-requisitos

- Python 3.9+
- Node.js e npm (para Tailwind CSS)
- Chave de API do Google Gemini
- Modelo de linguagem portuguesa para spaCy (`pt_core_news_sm`)

## Instalação

### 1. Clone o repositório

```bash
git clone <url-do-repositório>
cd autou-case
```

### 2. Configure o ambiente virtual Python

```bash
python -m venv .venv
```

#### Ative o ambiente virtual

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 3. Instale as dependências Python

```bash
pip install -r requirements.txt
```

### 4. Instale o modelo de linguagem portuguesa do spaCy

```bash
python -m spacy download pt_core_news_sm
```

### 5. Instale as dependências do Node.js

```bash
npm install
```

### 6. Configure as variáveis de ambiente

Crie um arquivo `.env` no diretório raiz com sua chave de API do Google Gemini:

```
GEMINI_API_KEY=sua_chave_de_api_gemini_aqui
```

## Compilando CSS

Para compilar os arquivos Tailwind CSS:

```bash
npx tailwindcss -i ./app/static/css/input.css -o ./app/static/css/output.css --watch
```

## Executando a Aplicação

```bash
python -m uvicorn main:app --reload
```

A aplicação estará disponível em http://127.0.0.1:8000

## Endpoints da API

- `GET /`: Interface principal do formulário
- `GET /health`: Endpoint de verificação de saúde
- `POST /process`: Processa texto ou uploads de arquivos

## Estrutura do Projeto

```
autou-case/
├── .env                    # Variáveis de ambiente
├── .venv/                  # Ambiente virtual Python
├── app/                    # Código da aplicação
│   ├── api/                # Endpoints da API
│   │   └── routes.py       # Rotas FastAPI
│   ├── core/               # Funcionalidades principais
│   │   └── npl.py          # Processamento de linguagem natural
│   ├── services/           # Serviços externos
│   │   └── gemini.py       # Integração com API Google Gemini
│   ├── static/             # Arquivos estáticos
│   │   ├── assets/         # Imagens e outros recursos
│   │   └── css/            # Arquivos CSS
│   └── templates/          # Templates Jinja2
│       └── form.html       # Template principal do formulário
├── main.py                 # Ponto de entrada da aplicação
├── package.json            # Dependências Node.js
├── postcss.config.mjs      # Configuração PostCSS
└── requirements.txt        # Dependências Python
```

## Licença

ISC
