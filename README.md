<div align="center">

# Kimo

![Python](https://img.shields.io/badge/Python-3.7+-blue)
![Flask](https://img.shields.io/badge/Flask-Latest-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**A Lightweight Flask-Based Backend Blog System**

English | [简体中文](./README.zh.md)

</div>

---

## ✨ Project Overview

Kimo is a lightweight blog backend system built with the Flask framework. It provides simple and easy-to-use blog content management and user account management features, making it suitable for personal blogs, team knowledge bases, and similar use cases.

## 🎯 Core Features

- ✅ **Blog Management**: Publish, browse, and manage blog posts
- ✅ **User Authentication**: User registration and login
- ✅ **Data Persistence**: MySQL-based data storage
- ✅ **Modular Architecture**: Code organized using Flask Blueprints
- ✅ **Database Connection Pool**: Efficient database connection management via DBUtils

## 🛠️ Tech Stack

| Technology | Description |
|-----------|-------------|
| **Backend** | Flask 2.x |
| **Database** | MySQL 5.7+ |
| **ORM / Query** | Raw SQL + PyMySQL |
| **Connection Pool** | DBUtils |
| **Python Version** | 3.7+ |

## 📦 Open Source Dependencies

- **Flask** – A lightweight Python web framework for backend APIs  
- **PyMySQL** – A pure-Python MySQL client library  
- **DBUtils** – Database connection pooling for improved performance  

## 🚀 Quick Start

### Requirements

- Python 3.7 or higher
- MySQL 5.7 or higher

### Installation

1. Clone the repository
```bash
git clone https://github.com/ChanYiCYJ/Kimo.git
cd Kimo
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate    # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure the database

Edit `config.json`:
```json
{
  "database": {
    "host": "your-db-host",
    "port": 3306,
    "user": "your-username",
    "password": "your-password",
    "name": "kimoServer",
    "charset": "utf8"
  }
}
```

5. Run the application
```bash
python app.py
```

Application will start at: `http://localhost:5000`

## 📄 License

This project is licensed under the **MIT License**.

## 👤 Author

**ChanYiCYJ**

---

Made with ❤️ by ChanYiCYJ
