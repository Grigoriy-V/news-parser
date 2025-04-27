# Парсер новостей

Проект для сбора и обработки новостных статей с различных веб-источников.

---

## 🚀 Возможности

- Загрузка HTML или RSS по списку URL
- Парсинг статей через BeautifulSoup (теги `<article>`, `<h2>`, `<a>`)
- Сохранение результатов в CSV-файл через pandas
- Гибкая настройка источников и параметров в YAML-конфиге
- Логи работы и хранение «сырых» данных

---

## 🧰 Технологии

- Python 3.7+
- requests
- beautifulsoup4
- pandas
- PyYAML
- pytest

---

## 📁 Структура проекта

```
news-parser/
├── config/
│   └── config.yaml        # Список источников, путь вывода и user-agent
├── data/                  # Сырые или итоговые данные (CSV, JSON и т.п.)
├── logs/                  # Логи работы парсера
├── src/
│   ├── main.py            # Точка входа, загрузка конфига, запуск парсера
│   └── parser/
│       └── parser.py      # Класс NewsParser: fetch, parse, save
├── tests/
│   └── test_parser.py     # Юнит-тест для метода parse()
├── .gitignore             # Исключения для Git
├── requirements.txt       # Зависимости проекта
├── init_news_parser.sh    # Скрипт создания структуры
└── README.md              # Этот файл
```

---

## ⚙️ Установка

```bash
git clone https://github.com/ВАШ_ЛОГИН/news-parser.git
cd news-parser
pip install -r requirements.txt
```

---

## 💾 Конфигурация

Отредактируйте файл `config/config.yaml`:

```yaml
source_urls:
  - https://example.com/news
  - https://another.com/rss
output_path: data/articles.csv
user_agent: NewsParserBot/1.0
```

- `source_urls` — список страниц или RSS для парсинга
- `output_path` — путь сохранения CSV
- `user_agent` — заголовок HTTP-запросов

---

## 🚀 Запуск

```bash
python src/main.py --config config/config.yaml
```

После выполнения в `data/articles.csv` появится таблица со столбцами:

- `title` — заголовок статьи
- `url` — ссылка на статью

---

## ✅ Тесты

```bash
pytest tests/
```

---


