# Python Virtual Environment (`venv`)

## 📌 Table of Contents
- [What is Virtual Environment?](#what-is-virtual-environment)
- [Creating a Virtual Environment](#creating-a-virtual-environment)
- [Activating (PowerShell)](#activating-powershell)
- [Deactivating](#deactivating)
- [Installing FastAPI and Uvicorn](#installing-fastapi-and-uvicorn)


---

## What is this?

A virtual environment is a **separate isolated space** for a Python project.

It allows you to install libraries **only for that project**, without affecting other projects or your system Python.

This keeps your projects clean and avoids version conflicts.

---

## Command to create a virtual environment

```bash
python -m venv myvenv
```
# Activating Python Virtual Environment (PowerShell)

## What is this?

When you create a virtual environment using:

```bash
python -m venv myvenv
```

# Deactivating Python Virtual Environment

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
