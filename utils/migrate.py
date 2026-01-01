# utils/migrate.py
import os

from utils.db import get_db_connection,implement,fetch_one,hash_password

TABLES_SQL = [
    """
    CREATE TABLE  IF NOT EXISTS `userinfo` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `user_name` varchar(255) DEFAULT NULL,
  `role` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `userInfo_unique` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """,

    """
    CREATE TABLE  IF NOT EXISTS `archive_tags` (
  `archive_id` int unsigned NOT NULL,
  `tag_id` int unsigned NOT NULL,
  PRIMARY KEY (`archive_id`,`tag_id`),
  KEY `tag_id` (`tag_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """,

    """
    CREATE TABLE IF NOT EXISTS  `archives` (
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `title` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `tagId` int NOT NULL,
  `category_id` int DEFAULT NULL,
  UNIQUE KEY `blog_unique` (`id`),
  KEY `fk_archives_category` (`category_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """,

    """
    CREATE TABLE IF NOT EXISTS `categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `slug` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `description` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """,

"""
CREATE TABLE  IF NOT EXISTS `tags` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `tagName` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  UNIQUE KEY `tag_unique` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
    # 1️⃣ 先测试数据库是否可用
    if not get_db_connection():
        print("❌ 数据库未配置或无法连接")
        return

    try:
        # 2️⃣ 检查 admin 是否存在
        check = fetch_one(
            "SELECT * FROM userInfo WHERE user_name=%s",
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

        hash_pwd = hash_password(password)

        # 4️⃣ 创建管理员
        ok = implement(
            "INSERT INTO userInfo(email,password,user_name,role) VALUES(%s,%s,%s,%s)",
            [email, hash_pwd, "admin", 0]
        )

        if ok:
            print("✅ 管理员账户创建成功")
        else:
            print("❌ 创建失败")

    except KeyboardInterrupt:
        print("\n❌ 已取消创建管理员")
