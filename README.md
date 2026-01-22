# 🗂️ 2️⃣ Estrutura Padrão — Flask

Arquitetura baseada em Blueprints (padrão profissional)

```
flask-todo-api/
│
├── app/
│   ├── __init__.py        # Criação da app Flask
│   ├── config.py          # Configurações (env, db, secret)
│   │
│   ├── extensions.py      # db, migrate, jwt, etc.
│   │
│   ├── models/
│   │   └── task.py
│   │
│   ├── routes/
│   │   └── task_routes.py
│   │
│   ├── services/
│   │   └── task_service.py
│   │
│   └── schemas/
│       └── task_schema.py
│
├── migrations/            # Alembic / Flask-Migrate
│
├── tests/
│   └── test_tasks.py
│
├── .env.example           # Variáveis de ambiente (modelo)
├── .gitignore
├── requirements.txt
├── run.py                 # Ponto de entrada
├── README.md
└── wsgi.py                # Para deploy

```

## Sugestão para criação de README (Use em todos)

```
# Nome do Projeto

Descrição curta do projeto.

## Tecnologias
- Python
- Flask/Django
- SQLite/PostgreSQL

## Como rodar
1. git clone
2. python -m venv venv
3. pip install -r requirements.txt
4. python run.py / python manage.py runserver

```

## 📌 Dica profissional (muito importante)

Sempre crie um arquivo:

```
.env.example

# Adicione o seguinte conteúdo:

SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

```
