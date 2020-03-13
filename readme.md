## commands

- init database and create some users

```bash
cp .env.example .env
flask migrate # create sqlite database
flask createautousers # create examples users(optional)
```

- run app

```bash
flask run
```

## sqlite

- show

```bash
sqlite3 core/db.sqlite3
.tables
.schema
.exit
```
