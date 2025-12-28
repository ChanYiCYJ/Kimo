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

| Technology          | Description       |
|---------------------|-------------------|
| **Backend**         | Flask 2.x         |
| **Database**        | MySQL 5.7+        |
| **ORM / Query**     | Raw SQL + PyMySQL |
| **Connection Pool** | DBUtils           |
| **Python Version**  | 3.7+              |

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

4. Create and configure the database
   Run the SQL statements below in your database

```bash
-- kimoserver.blog definition

CREATE TABLE `blog` (
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `title` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  UNIQUE KEY `blog_unique` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- kimoserver.userinfo definition

CREATE TABLE `userinfo` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `user_name` varchar(255) DEFAULT NULL,
  `role` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `userInfo_unique` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

Edit `config.json`:

```json
{
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
