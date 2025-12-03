# My LLM Project
Кратко: практический 30-дневный проект — summarizer + retrieval (RAG) + тесты.

## Цель
Собрать простой production-ish pipeline для summarization + vector search за 30 дней:
- API (FastAPI) `/summarize`
- локальный FAISS retriever
- tests + CI + docker
- basic safety / PII scrubber

## Быстрый старт (локально)
```bash
# склонировать репозиторий
git clone git@github.com:YOUR_USER/REPO.git
cd REPO

# создать и активировать виртуальное окружение
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# установить зависимости
pip install -r requirements.txt

# переименовать .env.example -> .env и заполнить ключи
cp .env.example .env
# отредактировать .env (API keys и т.д.)

# запустить пример сервиса
uvicorn service.main:app --reload --port 8000

## Project status
See [STATUS.md](./STATUS.md) for the current Day-by-day status.

