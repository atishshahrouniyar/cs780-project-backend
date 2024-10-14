
# Setup Project

## Create/activate virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

## Install requirements
```
pip install -r requirements.txt
```

## Database setup
###  Install Postgres
```
brew tap homebrew/core
brew install postgresql
brew services start postgresql
```

###  Setup schemas
```
createdb cs780
```

### Setup .env file in project root
```
SECRET_KEY=django-insecure-#9p$zd*&6w#q$kixe&344pir9nx+#t0$(w(q!u2uqav9av+r$(
DEBUG=True
DATABASE_NAME=cs780
DATABASE_USER=cs780
DATABASE_PASSWORD=cs780
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

## Migrate data
```
python manage.py migrate
```

## Run project
```
python manage.py runserver
```

# Add dependency
```
pip freeze > requirements.txt #ansi format
```

