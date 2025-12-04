# Learning journal — Day 1

Дата: 2025-12-03

1. Что сделано:

* Инициализирован репозиторий, создано README, .gitignore, .env.example
* Создано виртуальное окружение и установлены зависимости
* Примеры hello\_llm и call\_openai проверены — ключ подхватывается

2. 3 вывода:

*Что сработало: Создание venv и установка зависимостей прошли без проблем; примеры hello_llm.py и call_openai.py успешно подтянули ключ и дали ответ от модели.
*Что не сработало / вызвало сложности: Настройка SSH для нескольких GitHub-аккаунтов потребовала отдельного ключа и ~/.ssh/config, но сейчас всё работает — push проходит под нужным аккаунтом.
*Идея/план на завтра: Прогнать temperature_test.py и json_prompt_test.py, записать результаты и выбрать лучший prompt для строгого JSON-вывода.

3. План на завтра:

* Запустить temperature\_test.py и json\_prompt\_test.py
* Сформировать prompts.md с 3 few-shot примерами
### 2025-12-04 — temperature & json tests
- Temperature test: results saved to logs/temperature_test_results.json
  * temperature=0.0 -> deterministic greeting (same as 0.2)
  * temperature=0.2 -> same greeting as 0.0
  * temperature=0.7 -> slight variation (more creative)
  * temperature=1.0 -> ERROR 429 (rate limit exceeded)
- JSON prompt test: model returned valid JSON (parsed OK).
- Выводы / next steps:
  1. Использовать temperature 0.0–0.2 для стабильных/форматированных ответов.
  2. Использовать 0.7–1.0 для разнообразия, но с retry/backoff и лимитированием частоты запросов.
  3. Добавить retry/backoff в тестовый скрипт или понизить concurrency / увеличить лимит в панели.
  
  ### 2025-12-04 — Day 3: temperature & JSON tests

- Что сделано:
  * Проведены тесты `temperature` (0.0,0.2,0.7,1.0) в examples/temperature_test.py.
  * Исправлена retry-логика: добавлен post_with_retry с exponential backoff и jitter.
  * Результаты сохранены в logs/temperature_test_results.json, пример в results/.
  * Проверен json_prompt_test.py — модель вернула валидный JSON.

- Выводы:
  1. Temperature 0.0–0.2 даёт стабильные, предсказуемые ответы — полезно для формализованных/строгих форматов.
  2. Temperature 0.7 увеличивает разнообразие; полезно для креативных задач.
  3. Для temperature 1.0 возник 429 (rate limit) — нужно управлять частотой запросов или повышать квоты.

- План на завтра:
  * Day 4 — реализовать JSON-валидатор и интегрировать проверку в /summarize endpoint.
  * Подготовить prompts/prompts_v1.md с few-shot примерами.

