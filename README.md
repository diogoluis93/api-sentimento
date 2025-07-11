# 📊 API de Análise de Texto e Sentimento

Este projeto é uma API desenvolvida com **FastAPI** em Python, que realiza:

- Contagem de palavras em frases
- Extração das 5 palavras mais relevantes (ignorando stopwords)
- Análise de sentimento com IA da HuggingFace
- Cache em memória para reaproveitamento de resultados

---

## 🚀 Tecnologias Utilizadas

- Python 3.12
- FastAPI
- Transformers (Hugging Face)
- Uvicorn
- Pydantic
- Pytest + HTTPX (testes automatizados)

---

## ⚙️ Como executar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/diogoluis93/api-sentimento.git
cd api-sentimento
```

### 2. Criar ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar o servidor

```bash
uvicorn app.main:app --reload
```

Acesse: http://localhost:8000/docs

---

## 📫 Endpoints disponíveis

### POST /analyze-text
### GET /search-term

---

## 🧪 Executar os testes automatizados

### 1. Instale os pacotes de testes:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Rode os testes com:

```bash
pytest
```

---

## 👨‍💻 Autor

Diogo Luis Oliveira de Lima
https://github.com/diogoluis93
