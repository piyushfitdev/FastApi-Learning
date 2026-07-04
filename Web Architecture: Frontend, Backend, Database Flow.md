# Web Architecture: Frontend, Backend, Database Flow

## 📌 Overview
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
