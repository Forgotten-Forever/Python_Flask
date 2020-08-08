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
from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from app import mail, app


def send_async_mail(app, msg):
	with app.app_context():
		mail.send(msg)


def send_reset_password_mail(user, token):
    msg = Message("[Flask App] Reset Your Password!",
	              sender=current_app.config["MAIL_USERNAME"],
	              recipients=[user.email],
	              html=render_template('reset_password_mail.html',user=user, token=token))
    # print(user.email, current_app.config["MAIL_USERNAME"])
    # mail.send(message=msg)
    # 调用线程在后端进行发送，前端快速进行页面更改
    Thread(target=send_async_mail, args=(app, msg, )).start()