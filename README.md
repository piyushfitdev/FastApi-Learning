# Python Virtual Environment (`venv`)

## 📌 Table of Contents
- [What is Virtual Environment?](#what-is-virtual-environment)
- [Creating a Virtual Environment](#creating-a-virtual-environment)
- [Activating (PowerShell)](#activating-powershell)
- [Deactivating](#deactivating)
- [Installing FastAPI and Uvicorn](#installing-fastapi-and-uvicorn)
- [Basic FastAPI Code](#basic-fastapi-code)
- [Running the Server](#running-the-server)
- [What is CRUD?](#what-is-crud)
  - [GET - Read Data](#get---read-data)
    - [What is models.py and why we use it](#what-is-modelspy-and-why-we-use-it)
      - [Product Class (models.py)](#product-class-modelspy)
      - [Main FastAPI Code](#main-fastapi-code)

  - [POST - Create Data](#post---create-data)
  - [PUT - Update Data](#put---update-data)
  - [DELETE - Delete Data](#delete---delete-data)




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
