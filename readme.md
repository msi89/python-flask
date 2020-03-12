## commands

- init database and create some users

```bash
cp .env.example .env
flask create_database && flask create_user
```

- run app

```bash
flask run
```

## sqlite

- show

```bash
sqlite3 myapp/db.sqlite3
.tables
.schema
.exit
```
