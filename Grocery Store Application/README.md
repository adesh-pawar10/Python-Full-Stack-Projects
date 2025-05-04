# Grocery Store Management System

A full-stack Grocery Store Management System developed using a Flask backend and React frontend. It allows users to manage products, orders, and units of measure, with full CRUD functionality and database integration.

## 🗂️ Project Structure

```
grocery-store-management-system/
├── Database/                  # SQL scripts or database schema
├── grocery-store-backend/    # Flask backend application
├── grocery-store-frontend/   # React frontend application
```

---

## 🚀 Features

- 🧾 Product, Order, and UOM management
- 🔍 CRUD operations for each entity
- ⚙️ RESTful API built with Flask
- 💻 Modern UI built with React
- 🗃️ Integrated relational database (likely MySQL or SQLite)

---

## 🔧 Installation

### 1. Backend Setup (`grocery-store-backend`)

```bash
cd grocery-store-backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### 2. Frontend Setup (`grocery-store-frontend`)

```bash
cd grocery-store-frontend
npm install
npm start
```

---

## 🛢️ Database

- Navigate to the `Database` folder to find SQL scripts for creating and populating the database.

---

## 📦 Dependencies

### Backend

- Flask
- Flask-CORS
- MySQL Connector / SQLite (as used)
- Other dependencies listed in `requirements.txt`

### Frontend

- React
- Axios
- React Router

---

## 📌 Notes

- Make sure the backend server is running before launching the frontend.
- The backend runs by default on `http://localhost:5000`
- The frontend runs by default on `http://localhost:3000`

---

## 📥 Clone the Repository

```bash
git clone https://github.com/adesh-pawar10/Python-Full-Stack-Projects.git
cd Python-Full-Stack-Projects/Grocery\ Store\ Application

---

## 🧑‍💻 Author

[Adesh Pawar](https://github.com/adesh-pawar10)

---

## 📃 License

This project is licensed under the MIT License.
