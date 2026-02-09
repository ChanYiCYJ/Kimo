<div align="center">

# Kimo

![Python](https://img.shields.io/badge/Python-3.7+-blue)
![Flask](https://img.shields.io/badge/Flask-Latest-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**A Lightweight Flask-Based Backend Blog System**
**Not prefect**

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

4. Create `config.json`:
```json
{
  "app": {
    "config": {
      "title": "Hello World",
      "introduction": "Hello World",
      "theme": "Default"
    }
  },
  "database": {
    "host": "your-db-host",
    "port": 3306,
    "user": "your-username",
    "password": "your-password",
    "name": "your-sql-name",
    "charset": "utf8mb4"
  }
}

```

5. 安装说明
配置并创建config.json后，使用
```bash
python manage.py
```
创建数据表和创建管理员账户，最后运行
```bash
python app.py
```
建议将项目克隆至电脑运行manage.py再将项目配置至云端
Application will start at: `http://localhost:80`

## 📄 License

This project is licensed under the **MIT License**.


---

Made with ❤️ by ChanYiCYJ
