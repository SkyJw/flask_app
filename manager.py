# -*- coding: utf-8 -*-
#flask scripte 脚本命令处理文件

from app import create_app
from flask_script import Manager

app = create_app()

manager = Manager(app)

if __name__ == '__main__':
   manager.run()