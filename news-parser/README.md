# Парсер новостей

Проект для сбора и обработки новостных статей с различных источников.

## Структура проекта

\`\`\`
news-parser/
├── config/
│   └── config.yaml
├── data/
├── logs/
├── src/
│   ├── main.py
│   └── parser/
│       └── parser.py
├── tests/
│   └── test_parser.py
├── .gitignore
├── requirements.txt
└── README.md
\`\`\`

## Установка

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Запуск

\`\`\`bash
python src/main.py --config config/config.yaml
\`\`\`

## Тесты

\`\`\`bash
pytest tests/
\`\`\`
