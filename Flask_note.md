### Flask 框架学习
#### 通过 Pycharm 创建新的工程，创建 Falsk 项目 
生成的 Falsk 项目中带有一个 app.py 文件

 ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/project_build.png)
 ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/First_img.png)
 ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/First_startapp.png)
 ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Flask_title1.png)
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')  # 指定路由: '/' 根路由
def hello_world():
	return 'Hello World!'

if __name__ == '__main__':
# debug 默认为 False, debug=True 让开发变得友好，在修改App 文件后，刷新立即可以在本地服务上看到变化
# windows 可能做不到
# port 默认端口 5000 ,port=6333 更改端口
# host 默认为本地 127.0.0.1, host='0.0.0.0'面向局域网都可以访问
    app.run(debug=True, port=6333, host='0.0.0.0')  
```
#### 进行简单修改，对页面进行布局，渲染
1. 基础：在 return 内增加 HTML 类型文件
   ```python
   from flask import Flask
    
   app = Flask(__name__)
    
   @app.route('/')  # 指定路由
   def hello_world():
        # 更改 return 内为 HTML 文件
        return '<h1>Hello</h1><p>Flask</p>'
   
   if __name__ == '__main__':
        app.run(debug=True)
    ```
2. 优化: 在工程下建立文件夹 "templates" (现在版本已经实现自建),"templates" 中建立 "index.html" 文件
   在 app.py 内引进  {{ title }} 渲染
   ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Flask_title3.png)
   ```python
   from flask import Flask, render_template
   app = Flask(__name__)
    
   @app.route('/')  # 指定路由
   def hello_world():
       # title=title 将 title 传入 index 作为标题
       # <title>{{ title }}</title>
       # 写在 <p>{{ title }}</p> 内，也可以调用 填入 'Flask Web test'
       title = 'Flask Web test'
       return render_template('index.html', title=title)
    
   if __name__ == '__main__':
       app.run(debug=True)
   ```
3. 更高级渲染 (条件判断、循环)
   + 条件判断：
     如果 title 为空则默认 标题为 'Falsk App' 
     ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Flask_title4.png)
     ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Flask_title5.png)
       
     ```
        {% if title %}
            <title>{{ title }}</title>
        {% else %}
            <title>Falsk App</title>
        {% endif %}
        ```
       ```
       def hello_world():
       # title = 'Flask Web test'
       return render_template('index.html',
                              # title=title
                              )
       ```
   + 循环 建立三个 <p></p>
     ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Flask_p.png)
       ```
        {% for p in data %}
        <p>{{ p }}</p>
        {% endfor %}
       ```  
       ```
       def hello_world():
            title = 'Flask Web test'
            paragraphs = [
                "Selection 1",
                "Selection 2",
                "Selection 3"
            ]
            return render_template('index.html',
                                    title=title,
                                    data=paragraphs)
       ```
#### 模板继承和引用
1. 模板的继承
    + 在 "templates" 下建立 "base.html" 作为模板
      ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Flask_extends.png)
         ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            {% if title %}
                <title>{{ title }}</title>
            {% else %}
               <title>Falsk App</title>
            {% endif %}
        </head>
        <body>
        <h3><a href="/">Flask App</a> </h3>
        <hr>
        </body>
        </html>
        ```
        在 "index.html" 中继承 "base.html" 模板
        ```html
        {% extends 'base.html' %}
        ```
    + 在 "index.html" 继承模板后，写入属于自己的东西
        在 "base.html" 文件相应位置写下 block 定义此自定义模块名称为 content
         ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            {% if title %}
                <title>{{ title }}</title>
            {% else %}
               <title>Falsk App</title>
            {% endif %}
        </head>
        <body>
        <h3><a href="/">Flask App</a> </h3>
        <hr>
        {% block content %}
            <p>Test</p>
        {% endblock %}
        </body>
        </html>
        ```
        在 "index.html" 文件中 引用并更改
        
        ```html
        {% block content%}
          <p>{{ title }}</p>
        {% endblock %}
        ```
2. 模板的引用 (导入，对于会在很多地方用到的文件引用)
模板模块中定义的会被，引用模板的模块重写掉,如果没有引用则会显示模板模块内的内容，常规情况下默认为空
可以把每一个模块(导航栏，报头)新建一个 html 文件 (一个个小组件) 并引入继承到模块
    "navbar.html" 自定义报头
    ```html
    <h3><a href="/">Flask App</a> </h3>
    <hr>
    ```
    "base.html" 引入
    ```html
    {% include 'navbar.html' %}
    ```
#### 了解 flask-bootstrap (框架中已经定义好许多 class 的命名、风格) 使界面布局更加好看，将布局封装到Flask的插件
可以通过定义 class 的值定义组件位于 页面中的位置
[Flask—bootstrap 重点学习官网](https://getbootstrap.com/)
   ```
   pip install flask-bootstrap
   from flask import Flask, render_template
   from flask_bootstrap import Bootstrap
    
   app = Flask(__name__)
   bootstrap = Bootstrap(app)
   ```
1. HTML 中引用 bootstrap 从 bootstrap 的 base.html 中的库内引用

    [Boot-straap 官方提供的模板](https://getbootstrap.com/docs/3.3/components/#navbar)
    ```html
    {% extends "bootstrap/base.html" %}
    {% block title %}This is an example page{% endblock %}
    {% block navbar %}
    {#    {% include 'navbar.html' %}#}
    {% endblock %}
    
    {% block content %}
        <h1>Hello, Bootstrap</h1>
    {% endblock %}
    ```
2. 重写 bootstrap 里面的类，使之满足自己的需求
在 **"External Libraries -> site-packages -> flask_bootstrap -> templates -> bootstrap"** 内修改内置的各种页面，或者，复制出来在自己的页面中引用修改
3. 创建新的页面 (以点击形式进入新的连接)
+ app.py
    ```
    @app.route('/register')
    def register():
        # 转到 regist.html 页面
	    return render_template('register.html')
    ```
+ register.html
    引用 "base.html" 模板 
    ```
    {% extends 'base.html' %}
    
    {% block app_content %}
        <h1>Register Now</h1>
    {%  endblock %}
  ```
+ base.html
    引用 navbar.html 页面
    ```
    {% block navbar %}
        {% include 'navbar.html' %}
    {% endblock %}
    
    {% block content %}
        <div class="container">
            {% block app_content %}
            {% endblock %}
        </div>
    {% endblock %}
  ```
+ navbar.html.html
    设置页面共有文件
    ```
    <ul class="nav navbar-nav navbar-right">
        {#  只有当 request.endpoint 是 register 时 才是 active,否则是其他  #}
        <li class="{% if request.endpoint == 'register' %}active{% endif %}">
            {# 当点击 Regist 时 ，转到 register() 函数 ，由 render_template(register.html) 转到 register.html #}
            <a href="{{ url_for('register') }}">Register</a>
        </li>
    </ul>
  ```  
#### Flask 连接数据库、 Flask mine 找回密码、Flask 登录 (采用关系数据库，Flask提供flask-sqlalchemy连接数据库)
[flask_sqlalchemy 重点学习官方文档地址](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
```python
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 给出的是本地的 SQLite 数据库链接地址，可以改为 MySQL 等，只需要改变app.config['SQLALCHEMY_DATABASE_URI'] 值
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
```
1. 为了方便管理，建议将 SQL 配置新建一个 config.py 用于整理配置文件
   ```python
   import os
    
   basedir = os.path.abspath(os.path.dirname(__file__))
  
    
   class Config(object):
       # 如果找到 SQLite 路径就是用，如果没有找到就新建一个
       SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "sqlite:///" + os.path.join(basedir, 'app.db')
       SQLALCHEMY_TRACK_MODIFICATIONS = False
   ```
2. 建立 models.py 存放构建数据库的结构
    ```python
   from app import db
    
    
   class User(db.Model):
       # nullable 非空 ; unique 不能重复,出现相同就报错
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(20), unique=True, nullable=False)
       password = db.Column(db.String(20), nullable=False)
       email = db.Column(db.String(120), unique=True, nullable=False)
    
       def __repr__(self):
           return '<User %r>' % self.username
    ```
3. 要创建初始数据库，需要在 "Python Console" (3、4、5都在 Python Console 中执行) 导入对象并运行 "SQLAlchemy.create_all" 方法
    ```python
   from app.models import db
   db.create_all()
    ```  
4. 创建用户用于测试
    ```python
   from app.models import User
   from app.models import db
   user1 = User(username="", password="", email="")
   # 添加进数据库，并运行指令
   db.session.add(user1)
   db.session.commit()
    ```
5. 访问数据库中数据 
    ```python
   from app.models import User
   u = User.query.all()
   # [<User 'Jack'>]
   U = u[0]
   U.password
   # 'pwd'
   ```
#### FlaskWTF 创建 Flask 中的表单，基本包含所有表单
```
下载:
1. pip install flask-WTF
2. pip install wtforms
```
[FlaskWTF 重点官网主页](https://flask-wtf.readthedocs.io/en/stable/)
[Flask Bootstrap 与 其他组件联系内容包括 WTF](https://pythonhosted.org/Flask-Bootstrap/)
1. 创建表单 forms.py (用于注册，规定注册页面的内容)
    ```python
   # FlaskForm 主要负责整合 wtforms 的内容、类型 以及包装
   from flask_wtf import FlaskForm
   # 定义数据类型字符串，密码，提交按钮
   from wtforms import StringField, PasswordField, SubmitField
   # validators 验证者：需要的数据、数据范围Length(min=6, max=20)、Email、验证密码 EqualTo('password')
   from wtforms.validators import DataRequired, Length, Email, EqualTo
    
    
   class RegisterForm(FlaskForm):
       username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
       email = StringField('Email', validators=[DataRequired(), Email()])
       password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
       confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
       submit = SubmitField('Register')
    ```
2. 使用 Email类型 时需要下载支持
    ```
    pip install email_validator
    ``` 
  使用 FlaskWTF 需要秘钥设置， CSRF token 验证 每次随机生成
   
  ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/csrf_token.png)
    
   + 在 config.py 内设置
        ```
     # SECRET_KEY 秘钥为路径内或者 字符串 'A-VERY-LONG-SECRET' 可以随意设置，主要为了防止跨网站攻击
	 SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECRET'
     ```
   + 在 app.py 主页设置
        ```
        app.secret_key = '123456'
     ```
3. 定义 app.py 内注册页面
    ```python
   from flask import Flask, render_template, request, url_for
   from flask_bootstrap import Bootstrap
   from flask_sqlalchemy import SQLAlchemy
    
   from config import Config
   # 引用 form 内的 注册表单 RegisterForm
   from app.forms import RegisterForm
    
   app = Flask(__name__)
   db = SQLAlchemy(app)
   bootstrap = Bootstrap(app)
    
   app.config.from_object(Config)
   # 设置 传递数据的方法为 "GET" 与 "POST"
   @app.route('/register', methods=['GET', 'POST'])
   def register():
       # 调用 RegisterForm 表单定义
       form = RegisterForm()
       # 定义如果点击后 pass
       if form.validate_on_submit():
           pass
       # 将表单传入 register,html
       return render_template('register.html', form=form)
   ```
4. 定义 "register.html" : 引用 bootstrap 内的 wtf.html 内容
    WTF 内部包含 表单提交的各种报错，验证等
    ```html
    {% extends 'base.html' %}
    
    {% block app_content %}
        <h1>Register Now</h1>
        <br>
        <div class="row">
            {# col-md-6 表单大小 #}
            <div class="col-md-6">
                {# 引用 bootstrap 内的 wtf.html 内容 #}
                {% import 'bootstrap/wtf.html' as wtf %}
                {# 重点 一句话获取表单 form.py 的设置,快速完成表单，而无需进行大量的微调 #}
                {{ wtf.quick_form(form) }}
            </div>
        </div>
    
    {%  endblock %}
    ```
5. 额外: 人机验证 RECAPTCHA PUBLIC KEY 验证秘钥，验证是否为机器
    ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/PUBLIC_KEY.png)
    1. forms.py 添加验证
        ```
       from flask_wtf import FlaskForm, RecaptchaField
       recaptcha = RecaptchaField()
       ```
    2. config.py 注册秘钥
        ```
       # RECAPTCHA PUBLIC KEY 验证秘钥，验证是否为机器人
	   RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or 'A-VERY-LONG-PUBLIC-KEY'
       RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY') or 'A-VERY-LONG-PRIVATE_KEY'
       ```
    3. 遇到报错 "需要网站所有者处理的错误：网站密钥无效",需要自行注册页面
#### Flask-Bcrypt 加密数据项 ，在服务端处理表单存入数据库
```
pip install flask-bcrypt
```
1. 加密数据项 "flask-bcrypy" 中的 "Bcrypy" 模块, 传入数据库
    
    为了避免与 congig.py 内的引用构成 bug 新建 名为"app" 的 package 将除了数据库、config.py移入, 将 app.py 分为 __init__.py 与 route.py，在外部创建与 config.py 同级的 run.py
    ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/get_data1.png)
    ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/get_data2.png)
    + __init__.py
        ```python
      from flask import Flask
      from flask_bootstrap import Bootstrap
      from flask_sqlalchemy import SQLAlchemy
      # 调用模块
      from flask_bcrypt import Bcrypt
        
      from config import Config
        
        
      app = Flask(__name__)
      db = SQLAlchemy(app)
      # 定义模块
      bcrypt = Bcrypt(app)
      bootstrap = Bootstrap(app)
        
      app.config.from_object(Config)
      from app.route import *
        ```
    + route.py
        ```python
      from flask import render_template, flash
        
      from app import app, bcrypt, db
      from app.forms import RegisterForm
      from app.models import User
        
        
      @app.route('/')  # 指定路由
      def index():
          return render_template('index.html')
        
        
      @app.route('/register', methods=['GET', 'POST'])
      def register():
          form = RegisterForm()
          # 获取提交上来的注册数据，进行处理
          if form.validate_on_submit():
              username = form.username.data
              email = form.email.data
              # 变种hash加密,相同密码生成值也不同
              password = bcrypt.generate_password_hash(form.password.data)
              # 传入数据库内
              user = User(username=username, email=email, password=password)
              db.session.add(user)
              db.session.commit()
          # 检查产生密码与hash 是否对应正确
          # bcrypt.check_password_hash(hash, password)
          return render_template('register.html', form=form)
        ```
    + run.py
        ```python
      from app import app
        
      if __name__ == '__main__':
          app.run(debug=True)
        ```
2. 在设置 "models.py" 数据库时，设置 "unique=True 不能重复"，遇见重复的就会报错，需要写函数来辅助判断用户名和密码是否在数据库中，然后给与提示
    + forms.py 判断是否在数据库中重复，如果在给与报错
        ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Username_taken.png)
        ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Email_token.png)
        ```
        from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
        class RegisterForm(FlaskForm):
            def validate_username(self, username):
                user = User.query.filter_by(username=username.data).first()
                if user:
                    raise ValidationError('Username already token, please choose another one.')
    
            def validate_email(self, email):
                email = User.query.filter_by(email=email.data).first()
                if email:
                    raise ValidationError('Email already token, please choose another one.')
      ```
    + route.py  (flash提示注册成功，并跳转页面)
        ```python
      from flask import render_template, flash, redirect, url_for
 
      from app import app, bcrypt, db  
      from app.forms import RegisterForm 
      from app.models import User
        
        
      @app.route('/')  # 指定路由
      def index():
          return render_template('index.html')
        
        
      @app.route('/register', methods=['GET', 'POST'])
      def register():
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
              # flash 提示 "用户注册成功"，提示信息为 "success" 样式
              flash('Congrats registration success', category='success')
              # 提示后转至 index.html 页面
              return redirect(url_for('index'))
          # 检查产生密码与hash 是否对应正确
          # bcrypt.check_password_hash(hash, password)
          return render_template('register.html', form=form)
        ```
    + base.html (修改 base.html 页面，确保 flash 成功显示在页面上)
        ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/flash_show.png)
        ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/flash_return.png)
        ```html
        {% block content %}
            <div class="container">
                {# 提示框 #}
                <div class="row">
                    {# 页面大小 #}
                    <div class="col-lg-6">
                        {# 判断与循环 #}
                        {% with messages = get_flashed_messages(with_categories=True) %}
                            {% if messages %}
                                {% for category, message in messages %}
                                    <div class="alert alert-{{ category }}">
                                        {{ message }}
                                    </div>
                                {% endfor %}
                            {% endif %}
                        {% endwith %}
      
                    </div>
                </div>
                {# 在 app_content 注册 上添加 注册成功 提示 #}
                {% block app_content %}
                {% endblock %}
            </div>
        {% endblock %}
        ```  
#### Flask-login 用户登录包，包含很多用于登录、登出的函数
```
pip install flask-login
```
1. 在 __init__.py 内引入 flask-login 包，并进行设置
    ```
    from flask_login import LoginManager
    
    # 登录界面的位置
    login.login_view = 'login'
    # 提示 "You must login to access the page" 提示框格式为 "info"
    login.login_message = "You must login to access the page"
    login.login_message_category = "info"
    ```
2. 新建 login.html 登录页面，在 forms.py 下 新建 Login 函数，构造 登录需要的部件
    ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/login.png)
    ```html
    {% extends 'base.html' %}
    
    {% block app_content %}
        <h1>Login In</h1>
        <br>
        <div class="row">
            <div class="col-md-6">
                {% import 'bootstrap/wtf.html' as wtf %}
                {{ wtf.quick_form(form) }}
            </div>
        </div>
    
    {%  endblock %}
    ```
   ```
   from wtforms import StringField, PasswordField, SubmitField, BooleanField
   class LoginForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
        password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
        remember = BooleanField('Remember')
        submit = SubmitField('Sign In')
   ```
3. 修改 navbar.html 在主页面新增 "Login" 、"Logout" 选项框，
   
   增加判断项，在登录后只显示 "Logout" 选项，未登录时显示 "Login" 与 "Register" 选项，
   
   修改 主页面 (index.html) 显示为 Hello, {{ current_user.username }} 
   ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/logout.png)
   ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/if_not_login.png)
   ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/if_login.png)
    ```
    <ul class="nav navbar-nav navbar-right">
      {# 判断是否处于登录状态，current_user.is_authenticated 获取登录状态 #}
      {% if not current_user.is_authenticated %}
        {#    登录界面    #}
        <li class="{% if request.endpoint == 'login' %}active{% endif %}">
            <a href="{{ url_for('login') }}">Login In</a>
        </li>
        {#  只有当 request.endpoint 是 index 时 才是 active,否则是其他  #}
        <li class="{% if request.endpoint == 'register' %}active{% endif %}">
            <a href="{{ url_for('register') }}">Register</a>
        </li>
      {% else %}
        {#    登出界面    #}
        <li class="{% if request.endpoint == 'logout' %}active{% endif %}">
            <a href="{{ url_for('logout') }}">Logout</a>
        </li>
      {% endif %}
      </ul>
   ```
   ```html
    {% extends "base.html" %}
    
    {% block app_content %}
    <h1>Hello, {{ current_user.username }}</h1>
    {% endblock %}
    ```
4. 修改数据库设置 model.py，删除数据库重新构建数据库结构
    ```python
   # 引用 UserMinxin
   from flask_login import UserMixin
   # 从 app 包的 __init__.py 引用 login 
   from app import db, login
    
    
   @login.user_loader
   # 获取登录用户的 id
   def load_user(user_id):
       return User.query.filter_by(id=user_id).first()
    
    
   class User(db.Model, UserMixin):
       # nullable 非空 ; unique 不能重复
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(20), unique=True, nullable=False)
       password = db.Column(db.String(20), nullable=False)
       email = db.Column(db.String(120), unique=True, nullable=False)
    
    
       def __repr__(self):
           return '<User %r>' % self.username
    ```
   重构数据库:
        在 "Python Console" 内重置数据库
    ```
    from app.models import db
    db.create_all()
    ```
5. 设置 **route.py** 为登录方法进行实现
    ```python
   from flask import render_template, flash, redirect, url_for, request
   # 从登录模块引入所需的方法
   from flask_login import login_user, login_required, current_user, logout_user
   from app import app, bcrypt, db
   # 从 form.py 内引入 注册表格与登录表格
   from app.forms import RegisterForm, LoginForm
   from app.models import User
    
    
   @app.route('/')  # 指定路由
   # 需要登录
   @login_required
   def index():
       return render_template('index.html')
    
    
   @app.route('/register', methods=['GET', 'POST'])
   def register():
       # 判断是否是已经处于登录状态,如果是回到主界面
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
           # 注册成功后进入登录页面
           return redirect(url_for('login'))
       # 检查产生密码与hash 是否对应正确
       # bcrypt.check_password_hash(hash, password)
       return render_template('register.html', form=form)
    
   # 设置登录函数、登录页面、登录方法
   @app.route('/login', methods=['GET', 'POST'])
   def login():
       # 判断是否是已经处于登录状态,如果是回到主界面
       if current_user.is_authenticated:
           return redirect(url_for('index'))
       # 获取 登录表格 
       form = LoginForm()
       # 如果调交上来的数据不为空
       if form.validate_on_submit():
           username = form.username.data
           # 获取密码，检查密码是否与数据库中匹配
           password = form.password.data
           remember = form.remember.data
           # 根据输入用户名找到数据库中用户信息
           user = User.query.filter_by(username=username).first()
           # 如果用户存在且密码对应正确
           if user and bcrypt.check_password_hash(user.password, password):
               # 设置是否记住登录信息单选框
               login_user(user, remember=remember)
               # 返回登录成功信息
               flash("login success", category='info')
               # http://127.0.0.1:5000/login?next=%2F 由 next 决定接下来进入的页面
               if request.args.get('next'):
                   next_page = request.args.get('next')
                   return redirect(next_page)
               return redirect(url_for('index'))
           # 如果用户不岑在或者密码错误，flash 出错误
           flash("User not exists or password not match", category='danger')
       return render_template('login.html', form=form)
    
   # 设置登出函数、页面
   @app.route('/logout')
   # 只有在登录情况下才可以登出
   @login_required
   def logout():
       # 直接引用 flask_login 模块中的 logout_user()
       logout_user()
       # 登出后返回登录页面
       return redirect(url_for('login'))
    ```
***
#### 利用邮箱重置密码   
1. 在登录界面 (login.html) 创建 "忘记密码，找回选项"

![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Forget_Password.png)
    ```html
    <div class="row">
        <div class="col-md-6">
            <hr>
            {# 创建 找回密码界面 "send_password_reset_request.html" #}
            Password forget? <a href="{{ url_for('send_password_reset_request') }}">
            Click here to reset your password.</a>
        </div>
      </div>
    ```
2. 创建 找回密码界面 "send_password_reset_request.html" 界面配置与 注册界面类似
    ```html
    {% extends 'base.html' %}
    
    {% block app_content %}
        # 重置密码标题
        <h1>Send Reset Password Email</h1>
        <br>
        <div class="row">
            <div class="col-md-6">
                {% import 'bootstrap/wtf.html' as wtf %}
                {{ wtf.quick_form(form) }}
            </div>
        </div>
    
    {%  endblock %}
    ```
3. 在 forms.py 内创建 重置密码表单，

    ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Email_not_exists.png)
    ```python
   class PasswordResetRequestForm(FlaskForm):
       # 输入 Email 表格
       email = StringField('Email', validators=[DataRequired(), Email()])
       # 发送邮件按钮
       submit = SubmitField('Send')
    
       def validate_email(self, email):
           # 获取 Email
           email = User.query.filter_by(email=email.data).first()
           # 判断 邮箱是否存在 如果不存在 报错
           if not email:
               raise ValidationError('Email not exists.')
    ```
4. 在 route.py 页面设置 发用邮件验证界面
    ```
   @app.route('/send_password_reset_request', methods=["GET", "POST"])
   def send_password_reset_request():
       # 判断是否是已经处于登录状态,如果是回到主界面
       if current_user.is_authenticated:
           return redirect(url_for('index'))
       form = PasswordResetRequestForm()
       return render_template('send_password_reset_request.html', form=form)
   ```
#### 通过加密发送邮件给用户，安全实现密码更改 (PyJWT 加密，flask-mail 发送邮件验证)
```
pip install PyJWT
pip install flask-mail
```
1. 在 model.py 下创建加密规则与解密验证规则
![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Token.png)
![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Check_Token.png)
    ```python
   import jwt
   def generate_reset_password_token(self):
       # 将 token 与用户名 作为验证信息加密 传输
       return jwt.encode({'id': self.id}, current_app.config['SECRET_KEY'], algorithm="HS256")
    
   def check_reset_password_token(self, token):
       # 验证是加密的 验证信息 是否正确，是否遭到篡改
       try:
           data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithm=["HS256"])
           return User.query.filter_by(id=data['id']).first()
       except:
           return
    ```
2. 在 \_\_init\_\_.py 内部导入 flask-mail
    ```
   from flask_mail import Mail
   # mail 需要很多配置 可以百度 flask mail config
   mail = Mail(app)
   ```
3. 配置 mail 设置 config (在 config.py内配置)

    ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/error_smtplib.png)
    ```
   # Flask Gmail Config
   # 服务器 也可以用 qq 邮箱 smtp.qq.com (国内最好使用qq邮箱)
   MAIL_SERVER = 'smtp.gmail.com'
   # 端口 (不要使用默认端口 465 ，使用其他端口 25 或者其他的，否则会报错 smtplib.SMTPServerDisconnected: Connection unexpectedly closed)
   MAIL_PORT = 25
   MAIL_USER_SSL = True
   # 将 MAIL_USERNAME/qq 写入环境变量,放入自己的 GMAIL/qq 账号与 令牌 (GMAIL_PASSWORD，需要填入令牌)
   MAIL_USERNAME = os.environ.get('GMAIL_USERNAME') or 'GMAIL_USERNAME'
   MAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD') or 'GMAIL_PASSWORD'
   ```
4. 新建 email.py 页面 定义发送邮件
    ```python
   from flask import current_app, render_template
   from flask_mail import Message
   from app import mail
    
    
   def send_reset_password_mail(user, token):
       msg = Message("[Flask App] Reset Your Password!",
                   # 发送者邮箱，在 config.py 内定义的 邮箱
                   sender=current_app.config["MAIL_USERNAME"],
                   # 接受者邮箱
                   recipients=[user.email],
                   html=render_template('reset_password_mail.html',user=user, token=token))
       mail.send(message=msg)
    ```
5. 在 route.py 内配置重设密码页面以及补全发送邮箱验证界面
    ```
   def send_password_reset_request():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = PasswordResetRequestForm()
        # 获取提交上来的注册数据，进行处理
        if form.validate_on_submit():
            email = form.email.data
            user = User.query.filter_by(email=email).first()
            # token 作为参数加密放入链接发送给用户
            token = user.generate_reset_password_token()
            # 创建 email.py 发送给用户 加密 token
            send_reset_password_mail(user, token)
            # 建立 flash 提醒用户发送重设密码邮件成功
            flash('Password reset requests mail is send, please check your mail.', category='info')
        return render_template('send_password_reset_request.html', form=form)
    
    
   @app.route('/reset_password', methods=["GET", "POST"])
   # 重设密码界面 
   def reset_password():
        # 判断用户登录状态
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = ResetPasswordForm()
        # 根据表单渲染 reset_password.html 页面
        return render_template('reset_password.html', form=form)
   ```
6. 创建发送给用户的 重设密码邮件 界面 "reset_password_mail.html"
    ```html
    <p>Dear {{ user.username }}</p>
    <p>
        To reset your password
        <a href="{{ url_for('reset_password', token=token, _external=True) }}">
            click here!
        </a>
    </p>
    <p>Alternatively, you can paste the following link in your browser's address bar:</p>
    <p>{{ url_for('reset_password', token=token, _external=True) }}</p>
    <p>If you have not requested a password reset simply ignore this message.</p>
    <p>Sincerely,</p>
    <p>Flask App</p>
    ```
7. 创建重置密码页面 (reset_password.html) 与注册页面类似 
    ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/e_mail.png)
    ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/reset_password.png)
    ```html
    {% extends 'base.html' %}l>
    
    {% block app_content %}
        <h1>Reset Your Password</h1>
        <br>
        <div class="row">
            <div class="col-md-6">
                {% import 'bootstrap/wtf.html' as wtf %}
                {{ wtf.quick_form(form) }}
            </div>
        </div>
    
    {%  endblock %}
    ```
8. 完善 更改用户密码功能 。(route.py)
    ```
    # 将 '/reset_password' 改为 '/reset_password/<token>' 获取传递过去的 token
    @app.route('/reset_password/<token>', methods=["GET", "POST"])
    def reset_password(token):
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = ResetPasswordForm()
        # 获取表单数据
        if form.validate_on_submit():
            # 解密 token 获得用户名
            user = User.check_reset_password_token(token=token)
            # 如果用户存在
            if user:
                # 获取用户新更改的密码，传入数据库进行更新操作
                user.password = bcrypt.generate_password_hash(form.password.data)
                db.session.commit()
                flash('Your Password reset is done, You can login now use new Password.', category='info')
            else:
                flash("The user is not exist", category='info')
            return redirect(url_for('login'))
        return render_template('reset_password.html', form=form)
   ```
   为了方便，将 models.py 中的 验证密码改为 返回函数的静态方法，不需要实例化直接传参使用
   ```
   @staticmethod
   def check_reset_password_token(token):
   # 验证是加密的 验证信息 是否正确，是否遭到篡改
   try:
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithm=["HS256"])
			return User.query.filter_by(id=data['id']).first()
		except:
			return
   ```
9. 优化: 运用线程对发送邮件进行加速，使发送在后端进行，前端快速返回 (修改 email.py)
    ```python
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
    ```
#### 对 index 主页进行修改，实现一对多表格 (一个用户发送多个 Post Tweet)
![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Index1.png)
1. 修改 index.html，引入 form 表格
    ```html
    {% extends "base.html" %}
    
    {% block app_content %}
        <h1>Hello, {{ current_user.username }}</h1>
        <div class="row">
            <div class="col-md-6">
                {% import 'bootstrap/wtf.html' as wtf %}
                {{ wtf.quick_form(form) }}
            </div>
        </div>
    {% endblock %}
    ```
2. 在 form.py 内增加 表单数据
    ```
   from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
   class PortTweetForm(FlaskForm):
        # 文本框
        text = TextAreaField('Say Something  ....', validators=[DataRequired(), Length(min=1, max=40)])
        submit = SubmitField('Post Text')
   ```
3. 删除旧的 app.db ，在 model.py 内 新建 Post 类用于存储发布的文本，并与 User 类中的数据库链接

   ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Post_form.png)
   ```
    from datetime import datetime
    class User(db.Model, UserMixin):
        ...
        # 第一个 'Post' 对于 class Post ; backref 返回的信息;'author' 数据库中存储 Post 进入数据的名称; lazy=True 如果不用就不连接
        posts = db.relationship('Post', backref=db.backref('author', lazy=True))
        ...
    
    class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        body = db.Column(db.String(140), nullable=False)
        # 显示发布时间
        timestamp = db.Column(db.DateTime, default=datetime.utcnow)
        # 连接数据库中得到 user.id
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
        def __repr__(self):
            return '<Post {}>'.format(self.body)
    ```
4. 在 route.py 内 对 index 页面进行构造

    ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/Post1.png)
    ```
    from app.models import User, Post
    @app.route('/', methods=['GET', 'POST'])  # 指定路由
    # 需要登录
    @login_required
    def index():
        form = PortTweetForm()
        if form.validate_on_submit():
            body = form.text.data
            # 将 post 发送到数据库
            post = Post(body=body)
            current_user.posts.append(post)
            db.session.commit()
            flash('You have post a new tweet.', category='success')
        return render_template('index.html', form=form)
   ```
#### 数据库的多对多关系 (用户关注与取关)
1. 先定义 数据库中的 关注/取关 与 User 联系 (models.py)
    ```
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
        
        # 定义关注
        def follow(self, user):
            if not self.is_following(user):
                self.followed.append(user)
        
        # 定义取关
        def unfollow(self, user):
            if self.is_following(user):
                self.followed.remove(user)
        
        # 判断是否关注
        def is_following(self, user):
            # 从 followed 找到当前已经关注的，如果 >0 则已经关注
            return self.followed.count(user) > 0
    ```
2. 对主页 index.html 进行修改
    ```html
    <div class="align-right">
        <div class="thumbnail text-center">
            <br>
            <img src="{{ current_user.avatar_img }}" alt="avatar" width="100px" >
            <div class="caption">
                <h3>{{ current_user.username }}</h3>
                <p>
                    <a href="#" class="btn btn-primary" role="button">{{ n_followers }} followers</a>
                    <a href="#" class="btn btn-default" role="button">{{ n_followed }} followed</a>
                </p>
            </div>
        </div>
   </div>
    ```
3. 在 models.py User 数据库中加入默认头像
    ```
   class User(db.Model, UserMixin):
        ...
        avatar_img = db.Column(db.String(120), default='./static/asset/test.jpg', nullable=False)
        ...
   ```
4. 在 route.py 中定义 index.html 中的 followers 与 followed 
    ```
    @app.route('/', methods=['GET', 'POST'])  # 指定路由
    # 需要登录
    @login_required
    def index():
        ...
        n_followers = len(current_user.followers)
        n_followed = len(current_user.followed)
        return render_template('index.html', form=form, n_followers=n_followers, n_followed=n_followed)
   ```
   ![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/follower.png)
#### 在主页显示用户的发帖 (使用 bootstrap 的 Media heading)
![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/index_post.png)
1. 在 index.html 中设置 Media heading 模块
    ```html
    {% for post in posts %}
        <div class="media">
            <div class="media-left">
                <a href="#">
                    # 头像
                    <img src="{{ post.author,avatar_img }}" alt="avatar" width="64px">
                </a>
            </div>
            <div class="media-body">
                <h4 class="media-heading">{{ post.author.username }}</h4>
                <small class="text-muted">{{ post.timestamp }}</small>
                <p>{{ post.body }}</p>
            </div>
        </div>
     {% endfor %}
    ```
2. 在 route.py 中设置将 以倒序排列的 推文传入 index
    ```
   # 取得 发布的内容 以时间倒序来排列显示
   posts = Post.query.order_by(Post.timestamp.desc()).all()
   ```
#### 分页操作 (主要在 index.html 内进行修改判断，在 route.py 内稍微修改)
![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/page_2.png)
1. route.py 定义 posts 便于 index.html 调用 
    ```
   # 取得 发布的内容 以时间倒序来排列显示
    page = request.args.get('page', 1, type=int)
    # paginate(page, 2, False): 返回页数，每页两个推文，默认超出后不会报错
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page, 2, False)
    return render_template('index.html', form=form, posts=posts, n_followers=n_followers, n_followed=n_followed)
   ```
2. index.html 内定义 页面页数的变换 (Flask request 库的学习)
    ```html
    <nav aria-label="Page navigation">
        <center>
            <ul class="pagination">
                    # 添加判断 
                    <li class="{% if not posts.has_prev %}disabled{% endif %}">
                        <a href="{{ url_for('index', page=posts.prev_num) }}" aria-label="Previous">
                            <span aria-hidden="true">&laquo; Prev</span>
                        </a>
                    </li>
                    {# posts.iter_page() 以当前页为中心显示左右页数 #}
                    {% for i in posts.iter_pages(right_current=3) %}
                        {% if i %}
                            {# 判断是当前页面然后颜色不同 为 active 样式 #}
                            <li class="{% if i == posts.page %}active{% endif %}"><a href="{{ url_for("index", page=i) }}">{{ i }}</a> </li>
                        {% else %}
                            <li class="disabled"><a href="#">...</a> </li>
                        {% endif %}
                    {% endfor %}
                    <li class="{% if not posts.has_next %}disabled{% endif %}">
                        <a href="{{ url_for('index', page=posts.next_num) }}" aria-label="Next">
                            <span aria-hidden="true">&raquo; Next</span>
                        </a>
                    </li>
            </ul>
        </center>

    </nav>
    ```
#### 编辑用户个人界面和关注取关操作
![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/unfollow.png)
![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/follow.png)
1. 由于考虑到用户界面可能与主界面有 图片等部分重叠，从 index.html 内截取 Post 部分放入新建的 post_content.html 内，在 index.html 内引用
    ```html
    {#   运用函数后返回的不是列表，需要 .Item 转换为列表   #}
    {% for post in posts.items %}
        <div class="media">
            <div class="media-left">
                <a href="{{ url_for('user_page', username=post.author.username) }}">
                    <img src="{{ post.author.avatar_img }}" alt="avatar" width="64px">
                </a>
            </div>
            <div class="media-body">
                <h4 class="media-heading">{{ post.author.username }}</h4>
                <small class="text-muted">{{ post.timestamp }}</small>
                <p>{{ post.body }}</p>
            </div>
        </div>
    {% endfor %}
    {# 页面跳转#}
    <nav aria-label="Page navigation">
        <center>
            <ul class="pagination">
                    <li class="{% if not posts.has_prev %}disabled{% endif %}">
                        <a href="{{ url_for('index', page=posts.prev_num) }}" aria-label="Previous">
                            <span aria-hidden="true">&laquo; Prev</span>
                        </a>
                    </li>
                    {# posts.iter_page() 以当前页为中心显示左右页数 #}
                    {% for i in posts.iter_pages(right_current=3) %}
                        {% if i %}
                            {# 判断是当前页面然后颜色不同 为 active 样式 #}
                            <li class="{% if i == posts.page %}active{% endif %}"><a href="{{ url_for("index", page=i) }}">{{ i }}</a> </li>
                        {% else %}
                            <li class="disabled"><a href="#">...</a> </li>
                        {% endif %}
                    {% endfor %}
                    <li class="{% if not posts.has_next %}disabled{% endif %}">
                        <a href="{{ url_for('index', page=posts.next_num) }}" aria-label="Next">
                            <span aria-hidden="true">&raquo; Next</span>
                        </a>
                    </li>
            </ul>
        </center>
    
    </nav>
    ```
2. 在 route.py 内建立 个人信息，关注与取关 页面，并赋予功能
    ```
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
   ```
3. 建立个人信息界面 user_page.html
    ```html
    {% extends 'base.html' %}
    {% block app_content %}
        <div class="row">
            <div class="col-md-6">
                <h1>Hello, {{ current_user.username }}</h1>
                # 如果是用户正在观看自己的 个人信息，增加 填写信息 按钮
                {% if current_user == user %}
                    <a href="#">Edit Profile</a>
                # 如果用户正在看其他人的页面，添加 关注与取关 按钮
                {% else %}
                    {% if current_user.is_following(user) %}
                        <a href="{{ url_for("unfollow", username=user.username) }}">Unfollow</a>
                    {% else %}
                        <a href="{{ url_for("follow", username=user.username) }}">Follow</a>
                    {% endif %}
                {% endif %}
                <hr>
                {% include "post_content.html" %}
            </div>
        </div>
    {% endblock %}
    ```
#### Flask 上传文件 (用来修改头像)
![](https://cdn.jsdelivr.net/gh/Forgotten-Forever/BlogImages/images/upload_img.png)
1. 编写 上传文件 页面 edit_profile.html
    ```html
    {% extends 'base.html' %}
    
    {% block app_content %}
        <h1>Upload Your Avatar Image</h1>
        <br>
        <div class="row">
            <div class="col-md-6">
                {% import 'bootstrap/wtf.html' as wtf %}
                {{ wtf.quick_form(form) }}
            </div>
        </div>
    
    {%  endblock %}
    ```
2. 建立 上传表单
    ```
   # 上传文件使用 库
   from flask_wtf.file import FileField, FileRequired
   class UploadPhotoForm(FlaskForm):
        photo =FileField(validators=[FileRequired()])
        submit = SubmitField('Upload')
   ```
3. 在用户信息界面将 Edit Profile 链接到 上传页面
    ```
   <a href="{{ url_for("edit_profile") }}">Edit Profile</a>
   ```
4. 在 route.py 完善 上传页面配置
    ```
    import os
    from werkzeug.utils import secure_filename
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
                # 定义上传图片保存位置
                f.save(os.path.join('app', 'static', 'asset', filename))
                # 将数据库中默认的头像转变为用户自定义头像
                current_user.avatar_img = "/static/asset/" + filename
                db.session.commit()
                return redirect(url_for("user_page", username=current_user.username))
        return render_template("edit_profile.html", form=form)

   ```