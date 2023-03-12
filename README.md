# Data Challenge | Globant

##### *Alex Steven Nieto Arboleda*

This project is developed in Python and aims to load historical data from CSV files into a database and provide an API to insert data into the same database. The project directory is structured as follows:

```css
pruebaGlobant/
	data/raw/
		departments.csv
		hired_employees.csv
		jobs.csv
	src/
		db/
			connection.py
			queries.py
		schemas/
			departments.json
			hired_employees.json
			jobs.json
		api.py
		main.py
	__init__.py 
```

The execution of the project starts with the **init**.py file, which contains the following code:

```python
import subprocess
import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

src_dir = os.path.join(ROOT_DIR, 'src')
sys.path.append(src_dir)

with open(os.path.join(ROOT_DIR, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

def check_installed_libraries():
    for requirement in requirements:
        try:
            __import__(requirement)
        except ImportError:
            subprocess.check_call(["pip", "install", requirement])

check_installed_libraries()

from api import main

if __name__ == '__main__':
    main()
```

This file sets up the project environment by adding the src directory to the Python path and installing the required libraries listed in requirements.txt. Then, it executes the main function in the api.py module.

## Insert historical data

The main.py module is responsible for loading the historical data from CSV files into the database. It defines the expected data types for each column in the CSV files and uses the pandas library to read the CSV files into pandas.DataFrame objects. Then, it checks that the data types of each column match the expected data types and inserts the data into the database using the insert_historical_data function in the queries.py module.

The queries.py module contains the SQL queries used to create the database tables and insert data into them. It also contains the get_schema and create_table functions used by the main.py module to create the database tables.

The connection.py module contains the code to establish a connection to the database.

The schemas directory contains JSON files that define the schema for each table in the database. These schemas are used by the create_table function in the queries.py module.

The data/raw directory contains the CSV files with the historical data to be loaded into the database.

## API

This API provides endpoints to insert data into different tables in a database.

### Authentication

The API uses JSON Web Tokens (JWT) for authentication. To obtain a token, you must call the /login endpoint with valid credentials. The default credentials are:

-   username: "admin"
-   password: "admin"

The response will contain an access token that you can use to authenticate subsequent requests by including it in the Authorization header using the Bearer scheme.

### Endpoints

#### /login

**Method** : POST
**URL** : "/login"

**Request Parameters:**

| Parameter | Type   | Description  |
| --------- | ------ | ------------ |
| username  | string | The username |
| password  | string | The password |

**Response Parameters:**

| Parameter    | Type   | Description                 |
| ------------ | ------ | --------------------------- |
| access_token | string | The JWT access token to use |

**Example**

```css
POST /login HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
    "username": "admin",
    "password": "admin"
}
```

**Response**

```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJhZG1pbiIsImlhdCI6MTYxOTI3MDg5OX0.82clFZfxQl_gzjGAlhJ96-QFY_QH82PjxnLgXCBK1fA"
}
```

#### /insert/{table_name}

**Method** : POST
**URL** : "/insert/{table_name}"

**Request Parameters:**

| Parameter   | Type   | Description                                                     |
| ----------- | ------ | --------------------------------------------------------------- |
| table_name  | string | The name of the table to insert the data into                   |
| data        | object | A dictionary containing the data to be inserted into the table  |
| credentials | object | The JWT credentials for authentication (included in the header) |

**Response Parameters:**

| Parameter | Type   | Description                                      |
| --------- | ------ | ------------------------------------------------ |
| message   | string | A message indicating the number of rows inserted |

**Example**

```css
POST /insert/hired_employees HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJhZG1pbiIsImlhdCI6MTYxOTI3MDg5OX0.82clFZfxQl_gzjGAlhJ96-QFY_QH82PjxnLgXCBK1fA

{
    "id": 1,
    "name": "John Doe",
    "datetime": "2023-03-12 15:00:00",
    "department_id": 1,
    "job_id": 1
}
```

**Response**

```json
{
    "message": "1 row(s) inserted into hired_employees table."
}
```

## Running the Project

To run the project, follow these steps:

1.  Clone the project repository.
2.  Create a Python virtual environment and activate it.
3.  Run python pruebaGlobant/**init**.py to start the API and that's it!  ✨