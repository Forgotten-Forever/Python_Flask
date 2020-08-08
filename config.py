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
import os

basedir = os.path.abspath(os.path.dirname(__file__))
# print("sqlite:///" + os.path.join(basedir, 'app.db'))


class Config(object):

	# SECRET KEY
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECRET'

	# RECAPTCHA PUBLIC KEY 验证秘钥，验证是否为机器人
	# RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or 'A-VERY-LONG-SECRET'
	# RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY') or 'A-VERY-LONG-PRIVATE_KEY'
	# 如果找到 SQLite 路径就是用，如果没有找到就新建一个
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "sqlite:///" + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	# Flask Gmail Config
	MAIL_SERVER = 'smtp.qq.com'
	MAIL_PORT = 25
	MAIL_USER_SSL = True
	# 将 MAIL_USERNAME 写入环境变量,放入自己的 GMAIL aviezzlxegagggdc QMAIL yzqvbmtxflbwddgf 2985374516@qq.com
	MAIL_USERNAME = os.environ.get('GMAIL_USERNAME') or '2985374516@qq.com'
	MAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD') or 'yzqvbmtxflbwddgf'