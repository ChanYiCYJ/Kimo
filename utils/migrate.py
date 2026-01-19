# utils/migrate.py
import os

from utils.db import get_db_connection,implement,fetch_one
from utils.hash import hash_password
TABLES_SQL = [

# 1️⃣ 分类表
"""
CREATE TABLE IF NOT EXISTS categories (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  slug VARCHAR(50) NOT NULL,
  description VARCHAR(200),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uk_slug (slug)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""",

# 2️⃣ 用户表
"""
CREATE TABLE IF NOT EXISTS userInfo (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  user_name VARCHAR(255),
  role TINYINT NOT NULL DEFAULT 1,
  PRIMARY KEY (id),
  UNIQUE KEY uk_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""",
"""
CREATE TABLE IF NOT EXISTS page (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `type` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  UNIQUE KEY `page_unique` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""",
"""
CREATE TABLE IF NOT EXISTS tags (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  tag_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY uk_tag_name (tag_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""",

# 4️⃣ 文章表
"""
CREATE TABLE IF NOT EXISTS articles (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  title LONGTEXT NOT NULL,
  content LONGTEXT NOT NULL,
  category_id INT UNSIGNED DEFAULT NULL,
  description TEXT,
  cover_image TEXT,
  PRIMARY KEY (id),
  KEY idx_category (category_id),
  CONSTRAINT fk_articles_category
    FOREIGN KEY (category_id)
    REFERENCES categories (id)
    ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
""",

# 5️⃣ 文章-标签关联表
"""
CREATE TABLE IF NOT EXISTS article_tags (
  article_id INT UNSIGNED NOT NULL,
  tag_id INT UNSIGNED NOT NULL,
  PRIMARY KEY (article_id, tag_id),
  CONSTRAINT fk_at_article
    FOREIGN KEY (article_id)
    REFERENCES articles (id)
    ON DELETE CASCADE,
  CONSTRAINT fk_at_tag
    FOREIGN KEY (tag_id)
    REFERENCES tags (id)
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""
]



def init_db():
    conn = get_db_connection()
    if not conn:
        print("❌ 数据库未配置或无法连接")
        return

    cursor = conn.cursor()
    try:
        for sql in TABLES_SQL:
            cursor.execute(sql)
        conn.commit()
        print("✅ 数据表初始化完成-请使用运行app.py")
    except Exception as e:
        conn.rollback()
        print("❌ 初始化失败:", e)
    finally:
        cursor.close()
        conn.close()

def create_admin():
    try:
        # 1️⃣ 测试数据库连接
        conn = get_db_connection()
        if not conn:
            print("❌ 数据库未配置或无法连接")
            return

        # 2️⃣ 检查 admin 是否存在
        check = fetch_one(
            "SELECT id FROM userinfo WHERE user_name=%s LIMIT 1",
            ["admin"]
        )
        if check:
            print("⚠️ 管理员账户已存在，如需重建请手动删除")
            return

        # 3️⃣ 输入信息
        email = input("输入你的邮箱: ").strip()
        password = input("输入密码: ").strip()

        if not email or not password:
            print("❌ 邮箱或密码不能为空")
            return

        # 4️⃣ 密码加密
        hash_pwd = hash_password(password)

        # 5️⃣ 创建管理员（role=0 表示管理员）
        ok = implement(
            """
            INSERT INTO userinfo (email, password, user_name, role)
            VALUES (%s, %s, %s, %s)
            """,
            [email, hash_pwd, "admin", 0]
        )

        if ok:
            print("✅ 管理员账户创建成功")
        else:
            print("❌ 创建失败（SQL 未影响行数）")

    except KeyboardInterrupt:
        print("\n❌ 已取消创建管理员")
    except Exception as e:
        print("❌ 创建管理员异常：", e)
