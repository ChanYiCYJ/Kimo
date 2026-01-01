# manage.py
import sys
from utils.migrate import init_db,create_admin

def main():
    if len(sys.argv) < 2:
        print("可用命令:")
        print("  init-db    初始化数据库表")
        print(" create-admin 创建admin账户")
        return

    cmd = sys.argv[1]

    if cmd == 'init-db':
        init_db()
    if cmd == 'create-admin':
        create_admin()
    else:
        print("未知命令:", cmd)

if __name__ == '__main__':
    main()
