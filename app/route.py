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
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, login_required, current_user, logout_user
from app import app, bcrypt, db
from app.forms import RegisterForm, LoginForm, PasswordResetRequestForm, ResetPasswordForm, PortTweetForm, UploadPhotoForm
from app.models import User, Post
from app.email import send_reset_password_mail
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg', 'gif'}


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])  # 指定路由
# 需要登录
@login_required
def index():
	form = PortTweetForm()
	if form.validate_on_submit():
		body = form.text.data
		post = Post(body=body)
		current_user.posts.append(post)
		db.session.commit()
		flash('You have post a new tweet.', category='success')
	n_followers = len(current_user.followers)
	n_followed = len(current_user.followed)
	# 取得 发布的内容 以时间倒序来排列显示
	page = request.args.get('page', 1, type=int)
	# paginate(page, 2, False): 返回页数，每页两个推文，默认超出后不会报错
	posts = Post.query.order_by(Post.timestamp.desc()).paginate(page, 2, False)
	return render_template('index.html', form=form, posts=posts, n_followers=n_followers, n_followed=n_followed)


@app.route('/user_page/<username>')
@login_required
def user_page(username):
	user = User.query.filter_by(username=username).first()
	if user:
		page = request.args.get('page', 1, type=int)
		posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestamp.desc()).paginate(page, 2, False)
		return render_template('user_page.html', user=user, posts=posts)
	else:
		return '404'


@app.route('/follow/<username>', methods=['GET', 'POST'])
@login_required
def follow(username):
	user = User.query.filter_by(username=username).first()
	if user:
		current_user.follow(user)
		db.session.commit()
		page = request.args.get('page', 1, type=int)
		posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestamp.desc()).paginate(page, 2, False)
		return render_template('user_page.html', user=user, posts=posts)
	else:
		return '404'


@app.route('/unfollow/<username>', methods=['GET', 'POST'])
@login_required
def unfollow(username):
	user = User.query.filter_by(username=username).first()
	if user:
		current_user.unfollow(user)
		db.session.commit()
		page = request.args.get('page', 1, type=int)
		posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestamp.desc()).paginate(page, 2, False)
		return render_template('user_page.html', user=user, posts=posts)
	else:
		return '404'


@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
	form = UploadPhotoForm()
	if form.validate_on_submit():
		f = form.photo.data
		# secure_filename 对用户上传的 软件名 进行再次包装，防止入侵
		filename = secure_filename(f.filename)
		if f.filename == "":
			flash("No selected file", category="danger")
			return render_template("edit_profile.html", form=form)
		# 如果文件名是允许的后缀，可以进行操作
		if f and allowed_file(f.filename):
			# secure_filename 对用户上传的 软件名 进行再次包装，防止入侵
			filename = secure_filename(f.filename)
			f.save(os.path.join('app', 'static', 'asset', filename))
			current_user.avatar_img = "/static/asset/" + filename
			db.session.commit()
			return redirect(url_for("user_page", username=current_user.username))
	return render_template("edit_profile.html", form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegisterForm()
	# 获取提交上来的注册数据，进行处理
	if form.validate_on_submit():
		username = form.username.data
		email = form.email.data
		# 变种hash加密,相同密码生成值也不同
		password = bcrypt.generate_password_hash(form.password.data)
		user = User(username=username, email=email, password=password)
		db.session.add(user)
		db.session.commit()
		flash('Congrats registration success', category='success')
		return redirect(url_for('login'))
	# 检查产生密码与hash 是否对应正确
	# bcrypt.check_password_hash(hash, password)
	return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
	# 是否是已经处于登录状态,如果是回到登录界面
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		username = form.username.data
		# 获取密码，检查密码是否与数据库中匹配
		password = form.password.data
		remember = form.remember.data
		# 根据输入用户名找到数据库中用户信息
		user = User.query.filter_by(username=username).first()
		# 如果用户存在且密码对应正确
		if user and bcrypt.check_password_hash(user.password, password):
			login_user(user, remember=remember)
			flash("login success", category='info')
			if request.args.get('next'):
				next_page = request.args.get('next')
				return redirect(next_page)
			return redirect(url_for('index'))
		# 如果用户不岑在或者密码错误，flash 出错误
		flash("User not exists or password not match", category='danger')
	return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))


@app.route('/send_password_reset_request', methods=["GET", "POST"])
def send_password_reset_request():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = PasswordResetRequestForm()
	if form.validate_on_submit():
		email = form.email.data
		user = User.query.filter_by(email=email).first()
		# token 作为参数放入链接发送给用户
		token = user.generate_reset_password_token()
		# 创建 email.py 发送给用户 加密 token
		send_reset_password_mail(user, token)
		flash('Password reset requests mail is send, please check your mail.', category='info')
	return render_template('send_password_reset_request.html', form=form)


@app.route('/reset_password/<token>', methods=["GET", "POST"])
def reset_password(token):
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = ResetPasswordForm()
	if form.validate_on_submit():
		user = User.check_reset_password_token(token=token)
		if user:
			user.password = bcrypt.generate_password_hash(form.password.data)
			db.session.commit()
			flash('Your Password reset is done, You can login now use new Password.', category='info')
		else:
			flash("The user is not exist", category='info')
		return redirect(url_for('login'))
	return render_template('reset_password.html', form=form)