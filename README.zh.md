<div align=center>

# Kimo

![Python](https://img.shields.io/badge/Python-3.7+-blue)
![Flask](https://img.shields.io/badge/Flask-Latest-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**一个轻量化的 Flask 后端博客系统**

[English](./README.md) | 简体中文

</div>

---

## ✨ 项目简介

Kimo 是一个基于 Flask 框架的轻量级博客后端系统。它提供了简单易用的博客内容管理、用户账户管理等功能，适合个人博客、团队知识库等应用场景。

## 🎯 核心功能

- ✅ **博客管理**：发布、浏览和管理博客文章
- ✅ **用户认证**：用户注册和登录功能
- ✅ **数据持久化**：基于 MySQL 数据库存储
- ✅ **模块化架构**：采用蓝图（Blueprint）模式组织代码
- ✅ **数据库连接池**：使用 DBUtils 实现高效的数据库连接管理

## 🛠️ 技术栈

| 技术 | 说明 |
|------|------|
| **Backend** | Flask 2.x |
| **Database** | MySQL 5.7+ |
| **ORM/Query** | 原生 SQL + PyMySQL |
| **Connection Pool** | DBUtils |
| **Python Version** | 3.7+ |

## 📦 开源依赖

本项目使用了以下优秀的开源项目：

- **[Flask](https://github.com/pallets/flask)** - 轻量级 Python Web 框架，用于构建后端 API
- **[PyMySQL](https://github.com/PyMySQL/PyMySQL)** - 纯 Python 实现的 MySQL 客户端库
- **[DBUtils](https://github.com/Cito/DBUtils)** - 数据库连接池实现，提高数据库访问性能

## 🚀 快速开始

### 环境要求

- Python 3.7 或更高版本
- MySQL 5.7 或更高版本

### 安装步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/ChanYiCYJ/Kimo.git
   cd Kimo
   ```

2. **创建虚拟环境**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   venv\Scripts\activate  # Windows
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **配置数据库**
   编辑 `config.json` 文件，配置数据库连接信息：
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

5. **创建数据库**
   ```sql
   CREATE DATABASE kimoServer CHARACTER SET utf8;
   
   -- 创建用户表
   CREATE TABLE userInfo (
     id INT PRIMARY KEY AUTO_INCREMENT,
     user_name VARCHAR(100) NOT NULL,
     email VARCHAR(100) NOT NULL UNIQUE,
     password VARCHAR(255) NOT NULL,
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   
   -- 创建博客表
   CREATE TABLE blog (
     id INT PRIMARY KEY AUTO_INCREMENT,
     title VARCHAR(255) NOT NULL UNIQUE,
     content LONGTEXT NOT NULL,
     author_id INT,
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
     FOREIGN KEY (author_id) REFERENCES userInfo(id)
   );
   ```

6. **运行应用**
   ```bash
   python app.py
   ```
   应用将在 `http://localhost:5000` 启动

## 📖 API 文档

### 博客模块 (`/blog`)

#### 获取所有博客
- **URL**: `/`
- **Method**: `GET`
- **Response**: 返回所有博客列表

#### 获取单篇博客
- **URL**:  `/archives/<string:post_title>`
- **Method**: `GET`
- **Params**: `post_title` - 博客标题
- **Response**: 返回对应博客的详细信息

### 账户模块 (`/account`)

#### 用户登录
- **URL**: `/login`
- **Method**: `GET/POST`
- **POST Params**: 
  - `email` - 邮箱
  - `password` - 密码
- **Response**: 成功跳转首页，失败返回错误提示

#### 用户注册
- **URL**: `/register`
- **Method**: `GET/POST`
- **POST Params**:
  - `username` - 用户名
  - `email` - 邮箱
  - `password` - 密码
- **Response**: 注册结果提示

#### 用户登出
- **URL**: `/logout`
- **Method**: `GET`

#### 用户仪表板
- **URL**:  `/dashboard`
- **Method**: `GET/POST`

## 🔍 项目结构

```
Kimo/
├── kimo/                    # 主应用包
│   ├── __init__.py         # 应用工厂和蓝图注册
│   └── views/              # 视图层
│       ├── account.py      # 账户管理（登录、注册等）
│       └── blog.py         # 博客管理（发布、浏览等）
├── utils/                  # 工具函数
│   └── db. py              # 数据库连接和查询函数
├── templates/              # HTML 模板（前端）
├── app.py                  # 应用入口
├── config.json            # 配置文件
├── requirements.txt       # 项目依赖
├── LICENSE                # MIT 许可证
└── README.md             # 项目文档
```

## ⚠️ 已知不足与改进方向

### 当前存在的问题

1. **安全性问题**
   - 密码以明文存储，应该使用密码哈希（bcrypt/argon2）
   - 硬编码的数据库凭证应使用环境变量
   - 缺少 CSRF 防护
   - 缺少 SQL 注入防护的全面检查

2. **代码质量**
   - 缺少单元测试和集成测试
   - 代码文档和注释不够完善
   - 错误处理机制不够健全
   - 没有实现日志记录

3. **功能完整性**
   - 缺少用户权限管理（认证与授权）
   - 博客功能不完整（缺少编辑、删除功能）
   - 没有分页功能
   - 缺少搜索和分类功能

4. **性能优化**
   - 没有实现缓存机制
   - 数据库查询未优化
   - 缺少索引优化建议

5. **前端与部署**
   - 前端页面（HTML 模板）功能不完整
   - 没有 CORS 配置
   - 缺少 Docker 部署支持
   - 没有 CI/CD 流程

### 计划改进

- [ ] 实现密码加密存储和身份验证
- [ ] 添加全面的单元测试
- [ ] 完善 API 文档和代码注释
- [ ] 实现用户权限管理系统
- [ ] 优化数据库性能
- [ ] 添加 Docker 支持
- [ ] 实现前端 UI 界面
- [ ] 集成 CI/CD 流程

## 🤝 贡献指南

我们欢迎任何形式的贡献！如果你想帮助改进这个项目，可以：

1. **提交 Issue** - 报告 Bug 或提出功能建议
2. **提交 Pull Request** - 提交代码改进
3. **改进文档** - 完善项目文档和示例

### 开发流程

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改动 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 📄 许可证

本项目采用 **MIT License** 进行开源。这意味着你可以自由地使用、修改和分发本项目，但需要保留原始的版权声明和许可证文本。

详见 [LICENSE](./LICENSE) 文件。

### MIT License 的主要权利和义务

✅ **你可以**：
- 自由使用本软件
- 修改源代码
- 分发本软件
- 用于商业用途

⚠️ **你需要**：
- 保留原始的版权声明和许可证
- 在源代码副本或文件中包含许可证

## 🙋 获取帮助

- 📖 查看 [Wiki](https://github.com/ChanYiCYJ/Kimo/wiki)
- 💬 提交 [Issue](https://github.com/ChanYiCYJ/Kimo/issues)
- 📧 联系维护者

## 👤 作者

- **ChanYiCYJ** - 项目创建者和维护者

## ⭐ 致谢

感谢所有开源社区的贡献者和使用者的支持！
And Github copilot,Chatgpt

---

<div align="center">

Made with ❤️ by ChanYiCYJ

[⬆ back to top](#kimo)

</div>
