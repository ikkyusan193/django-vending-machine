
# Vending Machine API

**Vending Machine (RESTful API) using Django & SQL**


## API Endpoints


host: [127.0.0.1:8000](https://github.com/user/repo/blob/branch/other_file.md)
```bash
produc: "http://127.0.0.1:8000/product/"
stock: "http://127.0.0.1:8000/stock/"
vending-machine: "http://127.0.0.1:8000/vending-machine/"
product/$: "http://127.0.0.1:8000/product/"
stock/$: "http://127.0.0.1:8000/vending-machine/"
vending-machine/$: "http://127.0.0.1:8000/vending-machine/"
```
### Supported Operations

Applied for all enpoints & Object:

```
GET / GET<ID>
POST / POST<ID>
PUT / PUT<ID>
DELETE / DELETE<ID>
```

## Installation



### 1. Creating & Enabling Virtual Environment

Change directory to the project directory

```bash
 ~ cd vending-machine 
 ```

Create & Enabling virtual environment:
```bash
 ~ python -m venv <ENVIRONMENT-NAME>
 ~ <ENVIRONMENT-NAME>/bin/activate
```

### 2. Installing requirements



```bash
(env) pip install -r requirements.txt
```

## How to run application

Change directory into the application directory
```bash
 (env) cd vending-machine/vendor 
```

Migrate database and Run the application

```bash
 (env) python manage.py makemigrations
 (env) python manage.py migrate
 (env) python manage.py runserver
```

### In case of DB Error

```bash
(env) python3 manage.py migrate --run-syncdbest_f
```