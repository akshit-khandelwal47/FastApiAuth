# Fast-API-Login-Authentication
This fastapi application demonstrates user authentication using OAuth2 bearer with JWT token. There are other endpoints for CRUD operation on orders table.

## Clone the repository
```sh
git clone https://github.com/akshit-khandelwal47/FastApiAuth.git
```

## Create virtual environment
```sh
python -m venv env
```

## Activate the virtual environment
```sh
source env/bin/activate
```

## Installation of Requirements
```sh
cd FastApiAuth
pip install -r requirements.txt
```

## Database Connectivity
PostgreSQL is used as database and to connect it with database make changes in database.py.
`POSTGRES_URL = "postgresql://<db_user>:<db_password>@localhost/<db_name>"`

## Run the server for the app locally
```sh
uvicorn main:app --reload
```

## Swagger UI
Put '/docs' after your localhost url.

## Docker Containerization
```sh
docker compose-up
```