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
from datetime import datetime
from flask_login import UserMixin
from app import db, login
from flask import current_app
import jwt


@login.user_loader
def load_user(user_id):
	return User.query.filter_by(id=user_id).first()


# 简单的示范性的 关注关系 (只包含关注者与被关注着)，复杂的需要建立 class
followers = db.Table("followers",
                     db.Column("follower_id", db.Integer, db.ForeignKey('user.id')),
                     db.Column("followed_id", db.Integer, db.ForeignKey('user.id'))
                     )


class User(db.Model, UserMixin):
	# nullable 非空 ; unique 不能重复
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	password = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)

	avatar_img = db.Column(db.String(120), default='./static/asset/test.jpg', nullable=False)
	# 第一个 'Post' 对于 class Post ; backref 返回的信息;'author' 数据库中存储 Post 进入数据的名称; lazy=True 如果不用就不连接
	posts = db.relationship('Post', backref=db.backref('author', lazy=True))
	# 'User': 关注者与被关注着链接是用户之间的连接; primaryjoin=(followers.c.follower_id==id) 左边的关注着与右边的关注者通过 id 相互连接
	# 先正向连接，然后 backref 反向链接
	followed = db.relationship(
		'User', secondary=followers,
		primaryjoin=(followers.c.follower_id == id),
		secondaryjoin=(followers.c.followed_id == id),
		backref=db.backref('followers', lazy=True), lazy=True
	)

	def __repr__(self):
		return '<User %r>' % self.username

	def generate_reset_password_token(self):
		# 将 token 与用户名 作为验证信息加密 传输
		return jwt.encode({'id': self.id}, current_app.config['SECRET_KEY'], algorithm="HS256")

	@staticmethod
	def check_reset_password_token(token):
		# 验证是加密的 验证信息 是否正确，是否遭到篡改
		try:
			data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithm=["HS256"])
			return User.query.filter_by(id=data['id']).first()
		except:
			return

	def follow(self, user):
		if not self.is_following(user):
			self.followed.append(user)

	def unfollow(self, user):
		if self.is_following(user):
			self.followed.remove(user)

	def is_following(self, user):
		# 从 followed 找到当前已经关注的，如果 >0 则已经关注
		return self.followed.count(user) > 0


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140), nullable=False)
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return '<Post {}>'.format(self.body)
