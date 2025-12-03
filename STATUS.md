# first-llm-project

Практический 30‑дневный проект: собрать рабочий pipeline для summarization + retrieval (RAG) + тесты.

## Краткое описание

Цель: за 30 дней собрать POC сервиса, включающего промпты, LLM-интеграцию, локальный retriever и набор автоматических тестов.

## Быстрый старт

1. Склонировать репозиторий

```bash
git clone git@github.com:greengrand/first-llm-project.git
cd first-llm-project
```

2. Создать виртуальное окружение и активировать

```bash
py -3.14 -m venv .venv
# PowerShell
.\.venv\Scripts\Activate.ps1
```

3. Установить зависимости

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

4. Положить ключи в `.env` (скопировать из `.env.example` и заполнить). Не коммитить `.env`.

---

## Status — Day 1

**Сделано:**

* Репозиторий и начальный scaffold (README, .gitignore, .env.example) — добавлены и закоммичены.
* Локальное окружение: Python 3.14 и `.venv` созданы и активированы.
* `requirements.txt` добавлен; зависимости установлены в venv.
* Примеры: `examples/hello_llm.py` (проверка .env) и `examples/call_openai.py` (простой вызов модели) — созданы и протестированы.
* `learning/journal.md` — создан и частично заполнен (Day 1).

**Проверки:**

* `.env` не попал в git (наличие в .gitignore подтверждено).
* Успешный push изменений в origin/main.

**Что осталось:**

* Завершить заполнение `learning/journal.md` (3 вывода) — при необходимости.
* Создать шаблоны prompts и тестовую группу (следующие дни).

---

## Что запустить локально сейчас

* Проверка примеров:

```bash
# в активированном venv
python examples/hello_llm.py
python examples/call_openai.py
```

* Запуск FastAPI (если создан skeleton):

```bash
uvicorn service.main:app --reload --port 8000
```

## Дальше (кратко roadmap)

* Week 1: prompt-engineering, few-shot, output format validation, journal
* Week 2: FastAPI интеграция, unit/integration tests, prompt versioning
* Week 3: Embeddings → FAISS/Pinecone, retriever, RAG
* Week 4: Docker, CI, monitoring, demo

---

## Лицензия

MIT

---

Если нужно — могу автоматически применить этот README в репозитории (сгенерировать патч), или подготовить отдельный `STATUS.md`.

