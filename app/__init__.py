"""
                                _ooOoo_
                               o8888888o
                               88" . "88
                               (| -_- |)
                               O\  =  /O
                            ____/`---'\____
                          .'  \\|     |//  `.
                         /  \\|||  :  |||//  \
                        /  _||||| -:- |||||-  \
                        |   | \\\  -  /// |   |
                        | \_|  ''\---/''  |   |
                        \  .-\__  `-`  ___/-. /
                      ___`. .'  /--.--\  `. . __
                   ."" '<  `.___\_<|>_/___.'  >'"".
                  | | :  `- \`.;`\ _ /`;.`/ - ` : | |
                  \  \ `-.   \_ __\ /__ _/   .-` /  /
             ======`-.____`-.___\_____/___.-`____.-'======
                                `=---='
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                       佛祖保佑        永无BUG
"""
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_login import LoginManager

from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# mail 需要很多配置 可以百度 flask mail config
mail = Mail(app)
bcrypt = Bcrypt(app)
login = LoginManager(app)
# 登录界面的位置
login.login_view = 'login'
login.login_message = "You must login to access the page"
login.login_message_category = "info"
bootstrap = Bootstrap(app)


from app.route import *

