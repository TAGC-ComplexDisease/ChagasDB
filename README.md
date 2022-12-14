# Introduction
ChagasDB is a web application which aims to reference all the published data about the Chagas disease.

# Installation

## Docker installation
You may need to run the following with sudo permissions:
```
# Build image
docker-compose build
# Start ChagasDB container
docker-compose up -d
```

Using your web browser go to: http://127.0.0.1:8000

## Manual installation

```
conda create -n venv_chagasDB python=3.9
conda activate venv_chagasDB
pip install -r requirements.txt
```

### Setup environment variables based on local or production deployment
Localhost:
```
export CHAGAS_PROD="False"
export DB_FILE="Your/path/to/the/SQL/file/db.sqlite3"
export ALLOWED_HOSTS="127.0.0.1"
```

### Setup checking (optional; on changes to static folder)

```
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
```

### Starting application

```
python manage.py runserver
```

Using your web browser go to: http://127.0.0.1:8000

# Update data

```
python chagas_upd.py --help
```