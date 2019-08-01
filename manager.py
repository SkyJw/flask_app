# -*- coding: utf-8 -*-
#flask scripte 脚本命令处理文件

from app import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand

app = create_app()

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
   manager.run()