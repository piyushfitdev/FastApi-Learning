# Python Virtual Environment (`venv`)

# 📚 Table of Contents

## 🚀 FastAPI Basics
- [What is Virtual Environment?](#what-is-virtual-environment)
- [Creating a Virtual Environment](#creating-a-virtual-environment)
- [Activating (PowerShell)](#activating-powershell)
- [Deactivating](#deactivating)
- [Installing FastAPI and Uvicorn](#installing-fastapi-and-uvicorn)
- [Basic FastAPI Code](#basic-fastapi-code)
- [Running the Server](#running-the-server)
- [Web Architecture: Frontend, Backend, Database Flow](#web-architecture-frontend-backend-database-flow)
---

## 🔄 CRUD Operations
- [What is CRUD?](#what-is-crud)
  - [GET (Read)](#get---read-data)
  - [POST (Create)](#post---create-data)
  - [PUT (Update)](#put---update-data)
  - [DELETE (Delete)](#delete---delete-data)

- [Using `models.py`](#what-is-modelspy-and-why-we-use-it)

---

## 🗄️ PostgreSQL & SQLAlchemy
- [Install Required Libraries](#install-required-libraries)
- [Connecting FastAPI with PostgreSQL](#connecting-fastapi-with-postgresql)
- [Creating Database Tables](#creating-database-tables)
- [Insert Initial Data into Database](#insert-initial-data-into-database)
- [Dependency Injection](#dependency-injection-in-fastapi)

---

## 🛠️ Database CRUD Operations
- [Get Product by ID](#get-product-by-id)
- [Add Product](#add-a-product-to-database)
- [Update Product](#update-product-in-database)
- [Delete Product](#delete-product-from-database)

---

## 🌐 Frontend Integration
- [CORS Middleware](#cors-middleware)

---
## 🔐 JWT Authentication
- [Installing JWT Dependencies](#installing-jwt-dependencies)
  - [python-jose](#python-jose)
  - [passlib](#passlib)
  - [python-multipart](#python-multipart)
- [JWT Authentication Setup](#jwt-authentication-setup)
  - [Create `auth.py`](#create-authpy)
  - [Create APIRouter](#create-apirouter)
  - [JWT Secret Key](#jwt-secret-key)
  - [Password Hashing with `CryptContext`](#password-hashing-with-cryptcontext)
  - [OAuth2 Bearer Authentication](#oauth2-bearer-authentication)
  - [Request Models](#request-models)
  - [Database Dependency](#database-dependency)
  - [Create User API](#create-user-api)
  - [Creating a New User](#creating-a-new-user)
  - [Hashing the Password](#hashing-the-password)
  - [Saving User to Database](#saving-user-to-database)
  - [JWT Login & Authentication](#jwt-login--authentication)
  - [Login API](#login-api)
  - [Authenticating the User](#authenticating-the-user)
  - [Creating an Access Token](#creating-an-access-token)
  - [Getting the Current User](#getting-the-current-user)
- [Protecting Routes with JWT](#protecting-routes-with-jwt)
  - [Register Authentication Router](#register-authentication-router)
  - [Creating Dependencies](#creating-dependencies)
  - [Creating a Protected API](#creating-a-protected-api)


---

## What is Virtual Environment?

A virtual environment is a **separate isolated space** for a Python project.

It allows you to install libraries **only for that project**, without affecting other projects or your system Python.

This keeps your projects clean and avoids version conflicts.

---

## Creating a Virtual Environment

```bash
python -m venv myvenv
```
# Activating (PowerShell)

## What is this?

When you create a virtual environment using:

```bash
python -m venv myvenv
```

# Deactivating

## How to deactivate venv

To exit the virtual environment, simply run:

```bash
deactivate
```

# Installing FastAPI and Uvicorn

## Install command

To install both FastAPI and Uvicorn, use:

```bash id="fastapi2"
pip install fastapi uvicorn
```

## Basic FastAPI Code

```python id="code1"
from fastapi import FastAPI

app = FastAPI()

def greet():
    return "Welcome to my web server"
```
## Running the Server
```bash
uvicorn main:app --reload
```
---
# Web Architecture: Frontend, Backend, Database Flow

## Overview
<img width="745" height="277" alt="Screenshot 2026-07-04 111741" src="https://github.com/user-attachments/assets/73af8859-b27b-45c7-af5e-20340d4a8974" />

This diagram shows how a modern web application works using three layers:
- Frontend (UI)
- Backend (Server/API)
- Database (Storage)

---

## 🔁 Flow of Communication

### 1. Frontend → Backend (Request)
User interacts with UI (button click, page load, form submit).

Frontend sends a **request** to backend API.

---

### 2. Backend Processing
Backend receives the request and:
- Applies business logic
- Validates data
- Decides what data is needed

---

### 3. Backend → Database (Query)
If data is required, backend sends a query to the database.

---

### 4. Database → Backend (Data)
Database returns requested data back to backend.

---

### 5. Backend → Frontend (Response)
Backend sends response in **JSON format**.

---

## 🧠 Simple Understanding

- Frontend = UI layer (what user sees)
- Backend = Logic layer (processing)
- Database = Storage layer (data)

---

## ⚡ Core Concept

Everything in web development works on:
**Request → Process → Response cycle**
## What is CRUD?

CRUD stands for:
- **C** → Create
- **R** → Read
- **U** → Update
- **D** → Delete

These are the **basic operations of any backend system**.

---

### GET - Read Data

Used to fetch data from server. "/" defines the route, currently this is the homepage means the first page

```python id="get1"
from fastapi import FastAPI

app =FastAPI()

@app.get("/")
def greet():
    return "Welcome to my web server"
```
<img width="405" height="275" alt="image" src="https://github.com/user-attachments/assets/46ad6158-6bd8-45d8-84dc-8beda46481cb" />

This is the inside path now. Add this below the code

```python id="get1"
@app.get("/products")
def get_all_products():
    return "all products working"
```
<img width="520" height="276" alt="image" src="https://github.com/user-attachments/assets/2f079ff2-1a63-4955-8250-52cbf26cc58c" />

## What is models.py and why we use it

We use `models.py` to:

- Keep data structure separate from API logic
- Make code clean and organized
- Reuse classes across multiple files
- Follow real-world backend architecture

### 💡 Simple idea:

- `main.py` → API logic (routes)
- `models.py` → data structure (blueprint of objects)

---

## Product Class (models.py)

```python id="model1"
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name : str
    description: str
    price: float
    quantity: int

```

## Main FastAPI Code

```python id="main.py"
from fastapi import FastAPI
from models import Product

app =FastAPI()

@app.get("/")
def greet():
    return "Welcome to my web server"

products = [
    Product(id= 1, name= "phone", description="sasta phone",price= 99,quantity=10),
    Product(id=2, name ="phone", description="luxury phone", price=10000,quantity=9)
]

@app.get("/product/{id}") #id is dynamic
def get_product_by_id(id: int): #here put the id 
    return products[id-1] #according to indexing 
```
<img width="572" height="453" alt="image" src="https://github.com/user-attachments/assets/4bef8520-ff59-41ff-8672-b98d00c76814" />

Small change if you want to get away from errors
```python id="main.py"
@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id== id:
            return product
    return "Product not found"
```

### POST - Create Data

Used to add new data to the server.

POST is one of the most important HTTP methods in FastAPI and backend development. It is used when the client wants to **send data to the server and create something new**.

---

#### 🧠 How POST works

1. Client sends data (usually JSON) to the server  
2. Server receives the data  
3. Server processes or stores it  
4. Server sends back a response confirming creation  

---


```python id="get1"
from fastapi import FastAPI
from models import Product

app =FastAPI()

@app.get("/")
def greet():
    return "Welcome to my web server"

products = [
    Product(id= 1, name= "phone", description="sasta phone",price= 99,quantity=10),
    Product(id=2, name ="phone", description="luxury phone", price=10000,quantity=5)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id== id:
            return product
    return "Product not found"
---
@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return products
---
```
<img width="413" height="207" alt="image" src="https://github.com/user-attachments/assets/7c869880-df67-44e1-9e1c-be8788a53720" />
<img width="952" height="473" alt="image" src="https://github.com/user-attachments/assets/574d9f0c-7424-4443-a7a7-28054beff912" />


### PUT - Update Data

Used to update existing data on the server.

The client sends the updated information, and the server replaces or modifies the existing data.

---

## 🧠 How PUT works

1. Client sends updated data.
2. Server searches for the existing item.
3. If the item is found, it is updated.
4. Server returns a success message.
5. If the item is not found, an error message is returned.

---

## 📦 Example in FastAPI

```python
@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Updated Successfully"
    return "No Product Found"
```
<img width="1091" height="515" alt="image" src="https://github.com/user-attachments/assets/fd2b8c91-3c85-4fa9-8c68-1f3b5648284d" />
<img width="1072" height="161" alt="image" src="https://github.com/user-attachments/assets/45de9fd0-4001-419c-8799-be8757e3f075" />

---

## 📤 What happens here

- `id` is used to find the product.
- `product` contains the updated information sent by the client.
- The server loops through the `products` list.
- If the product ID matches, the old product is replaced with the new one.
- If no matching product is found, the server returns **"No Product Found"**.

---

## ⚡ Key Points

- PUT is used to **update existing data**.
- The updated data is sent in the **request body**.
- The product is searched using its **ID**.
- If the ID exists, the product information is replaced.

---

## 📝 Note

This example uses an in-memory Python list, so all changes are lost when the server restarts.

In real applications, PUT requests usually update data stored in a database such as PostgreSQL or MySQL.

### DELETE - Delete Data

Used to remove existing data from the server.

The client sends an ID, and the server deletes the matching item from memory or database.

---

## 🧠 How DELETE works

1. Client sends the ID of the item to delete.
2. Server searches for the item in the data list.
3. If found, the item is removed.
4. Server sends a confirmation message.
5. If not found, an error message is returned.

---

## 📦 Example in FastAPI

```python
@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"
    return "No Product Found"
```
<img width="1075" height="295" alt="image" src="https://github.com/user-attachments/assets/a7b3dcb3-5195-4470-ac85-1a88a9b72041" />
<img width="1046" height="177" alt="image" src="https://github.com/user-attachments/assets/7200e9f9-dfdf-4d97-950a-007cb0666141" />

---

## 📤 What happens here

- The `id` is received from the client.
- The server loops through the `products` list.
- If a matching product is found:
  - It is removed using `del`.
  - A success message is returned.
- If no match is found:
  - A failure message is returned.

---

## ⚡ Key Points

- DELETE is used to **remove data permanently**.
- It identifies data using an **ID**.
- In this example, data is stored in a Python list (temporary storage).
- Changes are lost when the server restarts.

---

## 🧠 Important Note

In real-world applications:
- DELETE requests usually use a path parameter like:
  ```python
  @app.delete("/product/{id}")
  ```
- Data is deleted from a database (not a list).
- Proper status codes like `200 OK` or `404 Not Found` are used instead of plain strings.

---

# Connecting FastAPI with PostgreSQL

To connect your FastAPI backend with a PostgreSQL database, create two new files:

- `database.py`
- `database_models.py`

These files help separate **database connection logic** from **database models**, making the project clean and organized.

---

## Create `database.py`

This file is responsible for creating the connection between FastAPI and PostgreSQL.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:123@localhost:5432/fastapi"

# Connect Python with PostgreSQL
engine = create_engine(db_url)

# Create database session
session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
```

### 🧠 Explanation

- `create_engine()` creates a connection between Python and PostgreSQL.
- `db_url` contains the database credentials.
- `sessionmaker()` is used to create database sessions for performing CRUD operations.

---

## Create `database_models.py`

This file contains all the database tables (models).

```python
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):

    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
```

### 🧠 Explanation

- `Base` is the parent class for all database models.
- Each class represents one database table.
- `__tablename__` specifies the table name inside PostgreSQL.
- `Column()` defines the columns of the table along with their data types.

---

## Changes in `main.py`

Import the database connection and models.

```python
from database import session, engine
import database_models
```

Then create all tables automatically when the server starts.

```python
database_models.Base.metadata.create_all(bind=engine)
```

### 🧠 What does this do?

- Checks whether the tables already exist.
- If a table does **not** exist, SQLAlchemy creates it automatically.
- If the table already exists, nothing happens.

This only creates tables—it does **not** delete or overwrite existing data.

---

## 📌 Summary

| File | Purpose |
|------|---------|
| `database.py` | Connects FastAPI to PostgreSQL and creates database sessions |
| `database_models.py` | Defines database tables (models) |
| `Base.metadata.create_all()` | Creates tables automatically if they don't already exist |


---

# Install Required Libraries

Install SQLAlchemy and PostgreSQL driver using:

```bash
pip install sqlalchemy psycopg2
```

### 🧠 Why these libraries?

### SQLAlchemy
- SQLAlchemy is an ORM (Object Relational Mapper).
- It lets you interact with the database using Python code instead of writing long SQL queries.
- It makes database operations cleaner, easier to read, and easier to maintain.

### psycopg2
- `psycopg2` is the PostgreSQL driver for Python.
- It creates the connection between the FastAPI backend and the PostgreSQL database.
- Without it, Python cannot communicate with PostgreSQL.

---

# Connecting FastAPI with PostgreSQL

To connect your FastAPI backend with a PostgreSQL database, create two new files:

- `database.py`
- `database_models.py`

These files separate the database connection from the database models, making the project clean and organized.

---

## Create `database.py`

This file creates the connection between Python and PostgreSQL.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:123@localhost:5432/fastapi"

# Connect Python with PostgreSQL
engine = create_engine(db_url)

# Create database session
session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
```

### 🧠 Explanation

- `create_engine()` creates the connection with PostgreSQL.
- `db_url` stores the database connection details.
- `sessionmaker()` creates sessions that are used to perform CRUD operations.

---

## Create `database_models.py`

This file defines the database tables.

```python
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):

    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
```

### 🧠 Explanation

- `Base` is the parent class for all database models.
- Every class represents one database table.
- `__tablename__` specifies the table name.
- `Column()` defines each column and its data type.

---

## Changes in `main.py`

Add these imports:

```python
from database import session, engine
import database_models
```

---

## Creating Database Tables

After creating the FastAPI application:

```python
app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)
```

### 🧠 What does this do?

- Connects to the database.
- Checks if the tables already exist.
- If a table does not exist, SQLAlchemy creates it automatically.
- Existing tables are not modified or deleted.

---

## Fetching Data from Database

Update the `/products` endpoint:

```python
@app.get("/products")
def get_all_products():
    db = session()
    db.query()
    return products
```

### 🧠 Explanation

- `db = session()` creates a new database session.
- `db.query()` is used to query data from the database.
- Later, you'll specify which table to query, for example:

```python
db.query(database_models.Product)
```

or

```python
db.query(database_models.Product).all()
```

to fetch all products from the database.

---

## 📌 Summary

| File | Purpose |
|------|---------|
| `database.py` | Creates the PostgreSQL connection and database session |
| `database_models.py` | Defines the database tables (models) |
| `Base.metadata.create_all()` | Creates database tables automatically if they don't exist |
| `session()` | Opens a database session |
| `query()` | Retrieves data from the database |

---

# Insert Initial Data into Database

The `init_db()` function is used to insert the products stored in the Python list into the PostgreSQL database.

This is useful when you want to populate the database with some initial data.

---

## Creating `init_db()`

```python
def init_db():
    db = session()

    for product in products:
        db.add(database_models.Product(**product.model_dump()))

    db.commit()
```

Call the function once:

```python
init_db()
```

---

## 🧠 How it works

1. Create a new database session.
2. Loop through every product in the `products` list.
3. Convert the Pydantic model into a dictionary.
4. Create a SQLAlchemy `Product` object.
5. Add it to the database session.
6. Save all changes using `db.commit()`.

---

## Understanding `model_dump()`

```python
product.model_dump()
```

`model_dump()` is a Pydantic function that converts a model object into a Python dictionary.

### Example

Pydantic object:

```python
Product(
    id=1,
    name="Phone",
    description="Budget Phone",
    price=99,
    quantity=10
)
```

After calling:

```python
product.model_dump()
```

Output:

```python
{
    "id": 1,
    "name": "Phone",
    "description": "Budget Phone",
    "price": 99,
    "quantity": 10
}
```

This dictionary can then be used to create a SQLAlchemy model.

---

## Understanding `**` (Double Asterisk)

The `**` operator is used to unpack a dictionary into keyword arguments.

Example:

```python
data = {
    "id": 1,
    "name": "Phone",
    "description": "Budget Phone",
    "price": 99,
    "quantity": 10
}
```

Instead of writing:

```python
database_models.Product(
    id=data["id"],
    name=data["name"],
    description=data["description"],
    price=data["price"],
    quantity=data["quantity"]
)
```

You can simply write:

```python
database_models.Product(**data)
```

The `**` operator automatically converts the dictionary into:

```python
database_models.Product(
    id=1,
    name="Phone",
    description="Budget Phone",
    price=99,
    quantity=10
)
```

This makes the code shorter, cleaner, and easier to maintain.

---

## 📌 Why use `model_dump()` with `**`?

- `model_dump()` converts a Pydantic object into a dictionary.
- `**` unpacks that dictionary into keyword arguments.
- SQLAlchemy models expect keyword arguments when creating new objects.
- Together, they make it easy to convert a Pydantic model into a SQLAlchemy model.

---

## ⚠️ Important

After adding objects using:

```python
db.add(...)
```

the data is **not** saved immediately.

You must call:

```python
db.commit()
```

to permanently store the data in the PostgreSQL database.

Without `commit()`, the inserted data will not be saved.

---

# Dependency Injection in FastAPI

Dependency Injection is a FastAPI feature that automatically provides the resources a function needs.

Instead of creating a database session inside every API function, FastAPI creates and manages it for us.

This keeps the code clean, reusable, and easier to maintain.

---

## Creating `get_db()`

```python
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
```

### 🧠 What does this function do?

- Creates a new database session.
- Provides (`yield`) the session to the API endpoint.
- Automatically closes the session after the request is completed.

Using `finally` ensures that the database connection is always closed, even if an error occurs.

---

## Using `Depends()`

```python
db: Session = Depends(get_db)
```

### 🧠 What is `Depends()`?

`Depends()` tells FastAPI:

> "Before executing this API, call `get_db()` and provide its returned database session."

FastAPI automatically:
- Calls `get_db()`
- Gets the database session
- Passes it to the API function
- Closes the session after the request is completed

This process is called **Dependency Injection**.

---

## Fetching Data Using Dependency Injection

```python
from fastapi import Depends
from sqlalchemy.orm import Session

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):

    db_products = db.query(database_models.Product).all()
    return db_products
```

---

## 🧠 How this works

1. A client sends a request to `/products`.
2. FastAPI sees `Depends(get_db)`.
3. It calls `get_db()`.
4. A database session is created.
5. The session is passed to the `db` parameter.
6. The query fetches all products from the database.
7. After the response is sent, the database session is automatically closed.

---

## 📌 Why use Dependency Injection?

- No need to create a database session inside every API.
- Automatically opens and closes database connections.
- Makes the code clean and reusable.
- Prevents database connection leaks.
- Recommended approach for FastAPI applications.

---

## 📌 Summary

| Function | Purpose |
|----------|---------|
| `get_db()` | Creates and manages a database session |
| `yield` | Temporarily provides the session to the API |
| `Depends()` | Tells FastAPI to automatically inject the dependency |
| `db: Session` | Receives the database session created by `get_db()` |

---

# Get Product by ID

This API is used to retrieve a single product from the database using its unique **ID**.

---

## Example

```python
@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(
        database_models.Product.id == id
    ).first()

    if db_product:
        return db_product

    return "Product not found"
```

---

## 🧠 How it works

1. The client sends a request with a product ID.
2. FastAPI receives the `id` from the URL.
3. A database session is automatically provided using `Depends(get_db)`.
4. SQLAlchemy searches the `Product` table.
5. If a matching product is found, it is returned.
6. Otherwise, a **"Product not found"** message is returned.

---

## Finding a Product Using `filter()`

```python
db.query(database_models.Product).filter(database_models.Product.id == id)
```

### 🧠 What does `filter()` do?

`filter()` is used to search for records that satisfy a specific condition.

In this example, it searches for the product whose `id` matches the value received from the URL.

Example:

```python
database_models.Product.id == id
```

means:

> Find the product where the **Product ID is equal to the requested ID**.

---

## Using `first()`

```python
.first()
```

### 🧠 What does `first()` do?

`first()` returns the **first matching record** from the query.

If no matching record exists, it returns `None`.

Since `id` is a **Primary Key**, there can only be one matching product.

Using `first()` retrieves that single product directly.

---

## 📌 Why use `filter()` and `first()` together?

- `filter()` selects the matching record.
- `first()` retrieves the first matching result.
- If no record matches, `first()` returns `None`.

Together they make it easy to fetch a single product from the database.

---

## 📌 Summary

| Function | Purpose |
|----------|---------|
| `db.query()` | Selects the table to query |
| `filter()` | Finds records matching a condition |
| `first()` | Returns the first matching record or `None` |
| `Depends(get_db)` | Automatically provides a database session |

---

# Add a Product to Database

This API is used to insert a new product into the PostgreSQL database.

---

## Adding a Product

```python
@app.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product
```

---

## 🧠 How it works

1. The client sends a new product in JSON format.
2. FastAPI converts the JSON into a Pydantic `Product` object.
3. `model_dump()` converts the Pydantic object into a Python dictionary.
4. `**` unpacks the dictionary into keyword arguments.
5. A SQLAlchemy `Product` object is created.
6. `db.add()` adds the object to the current database session.
7. `db.commit()` permanently saves the changes to the database.
8. The newly added product is returned as the response.

---

## Using `db.add()`

```python
db.add(database_models.Product(**product.model_dump()))
```

### 🧠 What does `db.add()` do?

- Adds a new object to the current database session.
- The data is **not saved immediately**.
- The object waits in the session until `db.commit()` is called.

---

## Using `db.commit()`

```python
db.commit()
```

### 🧠 What does `db.commit()` do?

`db.commit()` permanently saves all pending changes to the database.

Without calling `db.commit()`:
- The product is added only to the current session.
- The database is **not updated**.
- The new product will not be stored permanently.

---

## 📌 Why is `db.commit()` important?

`db.commit()` is one of the most important database operations.

It is responsible for:
- Saving new records
- Updating existing records
- Deleting records

Without it, the database remains unchanged.

---

## 📌 Summary

| Function | Purpose |
|----------|---------|
| `db.add()` | Adds a new object to the current database session |
| `model_dump()` | Converts a Pydantic model into a Python dictionary |
| `**` | Unpacks the dictionary into keyword arguments |
| `db.commit()` | Permanently saves all changes to the database |

---

# Update Product in Database

This API is used to update an existing product in the PostgreSQL database.

The product is searched using its **ID**. If it exists, its details are updated with the new values sent by the client.

---

## Updating a Product

```python
@app.put("/product/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()

    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity

        db.commit()

        return "Product Updated"

    return "No Product Found"
```

---

## 🧠 How it works

1. The client sends the product ID and updated product information.
2. FastAPI provides a database session using `Depends(get_db)`.
3. The database is searched for the product with the given ID.
4. If the product exists, its values are updated.
5. `db.commit()` permanently saves the changes.
6. If the product is not found, an error message is returned.

---

## Finding the Product

```python
db_product = db.query(database_models.Product)\
    .filter(database_models.Product.id == id)\
    .first()
```

### 🧠 What does this do?

- Searches the **Product** table.
- Finds the product whose ID matches the given ID.
- Returns the product if found.
- Returns `None` if no matching product exists.

---

## Updating Product Details

```python
db_product.name = product.name
db_product.description = product.description
db_product.price = product.price
db_product.quantity = product.quantity
```

### 🧠 What happens here?

Each field of the existing database record is replaced with the new values received from the client.

Only the selected product is updated.

---

## Saving Changes with `db.commit()`

```python
db.commit()
```

### 🧠 Why is `db.commit()` important?

`db.commit()` permanently saves the updated information to the database.

Without calling `db.commit()`:
- The values are changed only in memory.
- The database remains unchanged.
- The updates are lost after the request ends.

---

## 📌 Summary

| Function | Purpose |
|----------|---------|
| `db.query()` | Selects the database table |
| `filter()` | Finds the product using its ID |
| `first()` | Returns the matching product |
| `db.commit()` | Saves the updated data permanently |

---

# Delete Product from Database

This API is used to permanently delete a product from the PostgreSQL database.

The product is searched using its **ID**. If the product exists, it is removed from the database.

---

## Deleting a Product

```python
@app.delete("/product/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(
        database_models.Product.id == id
    ).first()

    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product Deleted Successfully"

    return "No Product Found"
```

---

## 🧠 How it works

1. The client sends the product ID.
2. FastAPI automatically provides a database session using `Depends(get_db)`.
3. The database is searched for the product with the given ID.
4. If the product exists:
   - It is deleted from the database session.
   - `db.commit()` permanently saves the deletion.
5. If the product does not exist, an error message is returned.

---

## Finding the Product

```python
db_product = db.query(database_models.Product)\
    .filter(database_models.Product.id == id)\
    .first()
```

### 🧠 What does this do?

- Searches the **Product** table.
- Finds the product whose ID matches the given ID.
- Returns the matching product.
- Returns `None` if no product is found.

---

## Using `db.delete()`

```python
db.delete(db_product)
```

### 🧠 What does `db.delete()` do?

- Marks the selected object for deletion.
- The record is **not removed immediately**.
- The deletion becomes permanent only after calling `db.commit()`.

---

## Saving Changes with `db.commit()`

```python
db.commit()
```

### 🧠 Why is `db.commit()` important?

`db.commit()` permanently saves the deletion in the database.

Without calling `db.commit()`:
- The product is only marked for deletion in the current session.
- The database remains unchanged.
- The deleted product will still exist in the database.

---

## 📌 Summary

| Function | Purpose |
|----------|---------|
| `db.query()` | Selects the database table |
| `filter()` | Finds the product using its ID |
| `first()` | Returns the matching product |
| `db.delete()` | Marks the product for deletion |
| `db.commit()` | Permanently deletes the product from the database |

---

# CORS Middleware

CORS (Cross-Origin Resource Sharing) is a security feature used by web browsers.

It controls **which frontend applications are allowed to communicate with your FastAPI backend**.

Without CORS, browsers block requests coming from different origins for security reasons.

---

## What is CORS?

An **Origin** is made up of:

- Protocol (`http` or `https`)
- Domain (`localhost`, `example.com`)
- Port (`3000`, `8000`, etc.)

Example:

Frontend:
```text
http://localhost:3000
```

Backend:
```text
http://localhost:8000
```

Since the ports are different, these are considered **different origins**.

By default, the browser blocks communication between them.

---

## Adding CORS Middleware

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)
```

---

## Understanding the Configuration

### `CORSMiddleware`

Adds CORS support to your FastAPI application.

---

### `allow_origins`

```python
allow_origins=["http://localhost:3000"]
```

Specifies which frontend applications are allowed to access the backend.

In this example:

✔ Allowed:

```text
http://localhost:3000
```

❌ Not Allowed:

```text
http://localhost:5173
http://example.com
```

---

### `allow_methods`

```python
allow_methods=["*"]
```

Allows all HTTP methods.

This includes:

- GET
- POST
- PUT
- DELETE
- PATCH
- OPTIONS

You can also allow only specific methods:

```python
allow_methods=["GET", "POST"]
```

---

## Why is CORS Needed?

Suppose you have:

Frontend:
```text
http://localhost:3000
```

Backend:
```text
http://localhost:8000
```

When the frontend tries to call:

```text
GET http://localhost:8000/products
```

The browser first checks whether the backend allows requests from `localhost:3000`.

If CORS is not configured, the browser blocks the request and shows a **CORS error**.

By adding `CORSMiddleware`, you tell the browser that the frontend is allowed to access your API.

---

## 📌 Summary

| Configuration | Purpose |
|--------------|---------|
| `CORSMiddleware` | Enables Cross-Origin Resource Sharing |
| `allow_origins` | Specifies which frontend URLs can access the backend |
| `allow_methods` | Specifies which HTTP methods are allowed |

---

# Installing JWT Dependencies

Before implementing JWT Authentication in FastAPI, install the required libraries.

```bash
pip install "python-jose[cryptography]"
pip install "passlib[bcrypt]"
pip install python-multipart
```

These libraries provide everything needed to create secure authentication using JWT.

---

## python-jose

```bash
pip install "python-jose[cryptography]"
```

### 🧠 Purpose

`python-jose` is used to **create, sign, verify, and decode JWT (JSON Web Tokens).**

It helps FastAPI:

- Generate JWT access tokens
- Verify whether a token is valid
- Decode the information stored inside a token
- Detect expired or invalid tokens

Without this library, FastAPI cannot work with JWT authentication.

---

## passlib

```bash
pip install "passlib[bcrypt]"
```

### 🧠 Purpose

`passlib` is used to **hash passwords** before storing them in the database.

Instead of saving:

```text
password123
```

it stores something like:

```text
$2b$12$R2x7r...
```

This protects user passwords if the database is ever leaked.

It is also used to verify a user's password during login.

---

## python-multipart

```bash
pip install python-multipart
```

### 🧠 Purpose

`python-multipart` allows FastAPI to receive data submitted through HTML forms.

It is commonly used when implementing a login endpoint where the username and password are sent as form data.

Without this package, FastAPI cannot process form submissions using `Form()` or `OAuth2PasswordRequestForm`.

---

## 📌 Summary

| Library | Purpose |
|---------|---------|
| `python-jose` | Create, verify and decode JWT tokens |
| `passlib` | Hash and verify passwords securely |
| `python-multipart` | Receive form data (login forms, HTML forms) |

---

# JWT Authentication Setup

To keep the authentication code separate from the main application, create a new file named:

```text
auth.py
```

This file will contain all authentication-related code such as:

- User Registration
- User Login
- JWT Token Generation
- Token Verification
- Password Hashing

Keeping authentication in a separate file makes the project clean and easier to maintain.

---

## Create `auth.py`

Import the following modules:

```python
from datetime import timedelta, datetime
from typing import Annotated
from warnings import deprecated

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status

from database import session
from models import Users

from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
```

### 🧠 Why are these imports needed?

| Import | Purpose |
|---------|---------|
| `datetime` | Used to set token expiration time |
| `timedelta` | Adds time to the current date for token expiry |
| `APIRouter` | Creates a separate router for authentication APIs |
| `Depends` | Injects dependencies like database sessions |
| `HTTPException` | Returns API errors such as invalid login |
| `BaseModel` | Creates request and response models |
| `Session` | Performs database operations |
| `CryptContext` | Hashes and verifies passwords |
| `OAuth2PasswordBearer` | Extracts JWT tokens from requests |
| `OAuth2PasswordRequestForm` | Receives username and password from login forms |
| `jwt` | Creates and verifies JWT tokens |
| `JWTError` | Handles invalid or expired tokens |

---

## Create APIRouter

```python
router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)
```

### 🧠 What is APIRouter?

`APIRouter` is used to organize related API endpoints into separate files.

Instead of writing every API inside `main.py`, authentication APIs are moved into `auth.py`.

The `prefix="/auth"` automatically adds `/auth` before every endpoint.

Example:

```python
@router.post("/register")
```

becomes

```text
/auth/register
```

The `tags=["auth"]` groups all authentication APIs together inside Swagger Docs (`/docs`).

---

## JWT Secret Key

```python
SECRET_KEY = "197b2c37c391bed93fe80344fe73b806947a65e36206e05a1a23c2fa12702fe3"

ALGORITHM = "HS256"
```

### 🧠 What is `SECRET_KEY`?

The secret key is used to digitally sign JWT tokens.

It ensures that:

- Tokens cannot be modified by users.
- The server can verify that a token was created by your application.

Keep this key secret.

In real-world projects, it is stored in an environment variable (`.env`) instead of writing it directly in the code.

---

### 🧠 What is `HS256`?

`HS256` is the hashing algorithm used to sign and verify JWT tokens.

When a token is created, this algorithm uses the `SECRET_KEY` to generate a secure digital signature.

---

## Password Hashing with `CryptContext`

```python
bcrypt_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
```

### 🧠 What does this do?

Passwords should **never** be stored as plain text.

`CryptContext` automatically hashes passwords using the **bcrypt** algorithm.

Example:

Instead of storing:

```text
password123
```

It stores something similar to:

```text
$2b$12$7KJk8L...
```

During login, it compares the entered password with the hashed password stored in the database.

---

## OAuth2 Bearer Authentication

```python
oauth2_bearer = OAuth2PasswordBearer(
    tokenUrl="auth/token"
)
```

### 🧠 What is this?

`OAuth2PasswordBearer` tells FastAPI where users will obtain their JWT token.

Later, a login endpoint like:

```text
POST /auth/token
```

will generate a JWT token.

Whenever a protected API is accessed, FastAPI automatically reads the token from the request's **Authorization** header.

---

## Request Models

### Create User Request

```python
class CreateUserRequest(BaseModel):
    username: str
    password: str
```

### 🧠 Purpose

This Pydantic model validates the data received while creating a new user.

Example request:

```json
{
  "username": "piyush",
  "password": "mypassword123"
}
```

---

### Token Response

```python
class Token(BaseModel):
    access_token: str
    token_type: str
```

### 🧠 Purpose

This model defines the response returned after successful login.

Example response:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

---

## Database Dependency

```python
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
```

### 🧠 What does this do?

This function creates a database session for every API request.

FastAPI automatically:

1. Creates a new database session.
2. Passes it to the API.
3. Closes it after the request finishes.

Using `yield` ensures that the database connection is always closed, even if an error occurs.

---

## 📌 Summary

| Component | Purpose |
|-----------|---------|
| `APIRouter` | Groups authentication APIs into a separate router |
| `SECRET_KEY` | Signs and verifies JWT tokens |
| `ALGORITHM` | Hashing algorithm used for JWT |
| `CryptContext` | Hashes and verifies passwords |
| `OAuth2PasswordBearer` | Reads JWT tokens from incoming requests |
| `CreateUserRequest` | Validates user registration data |
| `Token` | Defines the login response format |
| `get_db()` | Creates and closes a database session automatically |

---

# Create User API

This API is used to register a new user in the database.

Instead of storing the user's password directly, the password is first **hashed** using **bcrypt** and then saved in the database.

---

## Creating a New User

```python
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    db: db_dependency,
    create_user_request: CreateUserRequest
):
    create_user_model = Users(
        username=create_user_request.username,
        hashed_password=bcrypt_context.hash(create_user_request.password)
    )

    db.add(create_user_model)
    db.commit()
```

---

## 🧠 How it works

1. Client sends the username and password.
2. FastAPI validates the request using `CreateUserRequest`.
3. The password is hashed using **bcrypt**.
4. A new `Users` object is created.
5. The user is added to the database session.
6. `db.commit()` permanently saves the user in the database.

---

## Hashing the Password

```python
hashed_password = bcrypt_context.hash(create_user_request.password)
```

### 🧠 Why hash the password?

Passwords should **never** be stored as plain text.

For example, instead of storing:

```text
password123
```

the database stores something like:

```text
$2b$12$L8nM4rP2...
```

This protects users even if the database is leaked.

During login, the entered password is hashed and compared with the stored hash.

---

## Saving User to Database

### Add the object to the session

```python
db.add(create_user_model)
```

`db.add()` adds the new user to the current database session.

At this point, the user is **not yet stored permanently**.

---

### Save the changes

```python
db.commit()
```

`db.commit()` permanently saves the new user in the PostgreSQL database.

Without calling `db.commit()`:

- The user is added only to the current session.
- The database remains unchanged.
- The new user will not be saved.

---

## 📌 Summary

| Function | Purpose |
|----------|---------|
| `CreateUserRequest` | Validates the incoming user data |
| `bcrypt_context.hash()` | Converts the password into a secure hash |
| `Users()` | Creates a new database object |
| `db.add()` | Adds the object to the current database session |
| `db.commit()` | Permanently saves the user in the database |

---

# JWT Login & Authentication

JWT authentication works in four main steps:

1. User enters their username and password.
2. The server verifies the credentials.
3. If the credentials are correct, a JWT Access Token is generated.
4. The client uses this token to access protected APIs.

---

## Login API

```python
@router.post("/token", response_model=Token)
async def login_For_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency
):
    user = authenticate_user(
        form_data.username,
        form_data.password,
        db
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate user."
        )

    token = create_access_token(
        user.username,
        user.id,
        timedelta(minutes=20)
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
```

### 🧠 How it works

1. User sends username and password.
2. `OAuth2PasswordRequestForm` receives the login data.
3. `authenticate_user()` verifies the credentials.
4. If authentication fails, a **401 Unauthorized** error is returned.
5. If authentication succeeds, a JWT token is created.
6. The token is returned to the client.

---

## Authenticating the User

```python
def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(
        Users.username == username
    ).first()

    if not user:
        return False

    if not bcrypt_context.verify(
        password,
        user.hashed_password
    ):
        return False

    return user
```

### 🧠 What does this function do?

This function verifies whether the username and password entered by the user are correct.

---

### Step 1 - Find the user

```python
user = db.query(Users).filter(
    Users.username == username
).first()
```

Searches the database for the entered username.

If no user exists, authentication fails.

---

### Step 2 - Verify the password

```python
bcrypt_context.verify(
    password,
    user.hashed_password
)
```

The entered password is compared with the hashed password stored in the database.

If they match, authentication is successful.

---

## Creating an Access Token

```python
def create_access_token(
    username: str,
    user_id: int,
    expires_delta: timedelta
):
    encode = {
        "sub": username,
        "id": user_id
    }

    expires = datetime.utcnow() + expires_delta

    encode.update({
        "exp": expires
    })

    return jwt.encode(
        encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
```

### 🧠 What is an Access Token?

An Access Token is a secure JWT that proves the user has successfully logged in.

Instead of sending the username and password with every request, the client sends this token.

---

### JWT Payload

```python
encode = {
    "sub": username,
    "id": user_id
}
```

The payload stores information that will be saved inside the JWT.

In this example:

- `sub` → Username (Subject)
- `id` → User ID

---

### Token Expiration

```python
expires = datetime.utcnow() + expires_delta
```

Sets the expiration time of the token.

Example:

```python
timedelta(minutes=20)
```

means the token will expire after **20 minutes**.

---

### Adding Expiration

```python
encode.update({
    "exp": expires
})
```

Adds the expiration time to the JWT payload.

Once the expiration time is reached, the token becomes invalid.

---

### Generating the JWT

```python
jwt.encode(
    encode,
    SECRET_KEY,
    algorithm=ALGORITHM
)
```

Creates a signed JWT using:

- Payload
- Secret Key
- Hashing Algorithm

The generated token is returned to the client.

---

## Getting the Current User

```python
async def get_current_user(
    token: Annotated[
        str,
        Depends(oauth2_bearer)
    ]
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username: str = payload.get("sub")
        user_id: int = payload.get("id")

        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate user."
            )

        return {
            "username": username,
            "id": user_id
        }

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate user."
        )
```

### 🧠 What does this function do?

This function checks whether the JWT token sent by the client is valid.

If the token is valid, it extracts the user's information from the token.

---

### Step 1 - Receive the Token

```python
token: Annotated[
    str,
    Depends(oauth2_bearer)
]
```

FastAPI automatically reads the JWT from the request's **Authorization** header.

Example:

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

---

### Step 2 - Decode the Token

```python
payload = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=[ALGORITHM]
)
```

The token is decoded using the same Secret Key and Algorithm that were used while creating it.

If the token has been modified or expired, decoding fails.

---

### Step 3 - Extract User Information

```python
username = payload.get("sub")
user_id = payload.get("id")
```

Reads the stored user information from the JWT payload.

---

### Step 4 - Return Current User

If the token is valid:

```python
return {
    "username": username,
    "id": user_id
}
```

The authenticated user's information is returned.

---

## 📌 JWT Authentication Flow

```text
User Login
     │
     ▼
Username + Password
     │
     ▼
authenticate_user()
     │
     ▼
Password Verified
     │
     ▼
create_access_token()
     │
     ▼
JWT Token Generated
     │
     ▼
Client Stores Token
     │
     ▼
Protected API Request
     │
     ▼
get_current_user()
     │
     ▼
JWT Verified
     │
     ▼
Access Granted
```

---

## 📌 Summary

| Function | Purpose |
|----------|---------|
| `login_For_access_token()` | Logs in the user and returns a JWT token |
| `authenticate_user()` | Verifies the username and password |
| `bcrypt_context.verify()` | Compares the entered password with the stored hashed password |
| `create_access_token()` | Creates a signed JWT with user information |
| `jwt.encode()` | Generates the JWT token |
| `jwt.decode()` | Verifies and decodes the JWT token |
| `get_current_user()` | Retrieves the currently authenticated user from the JWT |

---

# Protecting Routes with JWT

After creating the authentication system in `auth.py`, we need to connect it with our main FastAPI application.

This allows us to:

- Register authentication routes.
- Verify JWT tokens before accessing protected APIs.
- Get details of the currently logged-in user.

---

## Register Authentication Router

```python
app.include_router(auth.router)
```

### 🧠 What does this do?

This line registers all the routes defined in `auth.py`.

For example, if `auth.py` contains:

```python
@router.post("/token")
```

and the router has:

```python
prefix="/auth"
```

The final endpoint becomes:

```text
POST /auth/token
```

Without `app.include_router()`, the routes inside `auth.py` would never become part of the FastAPI application.

---

## Creating Dependencies

### Database Dependency

```python
db_dependency = Annotated[
    Session,
    Depends(get_db)
]
```

### 🧠 Purpose

Instead of writing:

```python
db: Session = Depends(get_db)
```

inside every API, we create a reusable dependency.

Now we can simply write:

```python
db: db_dependency
```

This makes the code shorter and easier to read.

---

### User Dependency

```python
user_dependency = Annotated[
    dict,
    Depends(get_current_user)
]
```

### 🧠 Purpose

This dependency automatically:

- Reads the JWT token from the request.
- Verifies whether the token is valid.
- Decodes the token.
- Returns the authenticated user's information.

Any API using this dependency becomes a **protected API**.

---

## Creating a Protected API

```python
@app.get("/", status_code=status.HTTP_200_OK)
async def user(
    user: user_dependency,
    db: db_dependency
):
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Authentication Failed"
        )

    return {
        "User": user
    }
```

---

## 🧠 How it works

1. Client sends a request to the API.
2. FastAPI checks `user_dependency`.
3. `get_current_user()` is called automatically.
4. The JWT token is extracted from the **Authorization** header.
5. The token is verified.
6. If valid, the user information is returned.
7. If invalid or expired, a **401 Unauthorized** error is returned.
8. If authentication succeeds, the protected API executes normally.

---

## JWT Authentication Flow

```text
Client
   │
   ▼
Authorization: Bearer <JWT Token>
   │
   ▼
Depends(get_current_user)
   │
   ▼
JWT Verification
   │
   ▼
Token Valid?
 ┌─────────────┐
 │             │
Yes           No
 │             │
 ▼             ▼
Return User   401 Unauthorized
 │
 ▼
Protected API Executes
```

---

## Why use `Annotated`?

`Annotated` combines:

- The data type (`Session`, `dict`)
- The dependency (`Depends()`)

into a single reusable type.

Instead of repeating:

```python
db: Session = Depends(get_db)
```

in every endpoint, you can simply write:

```python
db: db_dependency
```

This improves code readability and reduces repetition.

---

## 📌 Summary

| Component | Purpose |
|----------|---------|
| `app.include_router()` | Registers all authentication routes from `auth.py` |
| `db_dependency` | Provides a reusable database session |
| `user_dependency` | Provides the authenticated user's information |
| `Depends(get_current_user)` | Verifies the JWT token before executing the API |
| Protected API | Allows access only to authenticated users |
