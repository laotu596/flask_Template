模板引擎
模板文件就是按照特定规则书写得一个负责展示效果得html文件
模板引擎就是提供了特定规则得解释和替换得功能

1、目录结构
project/
manage.py                     #项目得启动控制文件
     templates/               #所有得模板文件



2、渲染模板文件

在templates 下面创建一个模板文件(hello.html)
<h1>渲染字符串</h1>

模板渲染

@app_route('/')
def index():
    #return '模板引擎测试'

    #return render_template('hello.html')   #渲染模板文件

    #return render_template_string('<h1>渲染字符串</h1>')   #渲染字符串

3、 模板中使用变量
{#...#} 表示注释
在templates 下创建一个模板文件(hello.html)
比如字符串、变量、函数调用
<h1>Nice,{{  g.name }}</h1>
Jinja2 支持使用"." 获取变量得属性，比如g.name

模板渲染
@app.route('/var/')
def va():
     g.name = 'Mian'
     return render_template_string('<h1>{{ g.name }}</h1>')

4、流程控制
分支语句（if-else）
{% if name %}
     <h1>{{ name }}</h1>
 {% else %}
      <h1>Stranger</h1>
 {% endif %}

循环语句
<ol>
    {% for i in range(1,5) %}
           <li>{{ i }}</li>
     {% endfor %}
</ol>

5、文件包含

include.html
<h1>Include</h1>
{% include 'include2.html'%}

include2.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>被包含</title>
</head>
<body>
    include 2
</body>
</html>

6、宏得使用
{# 定义宏 #}
{% macro show_name(name) %}
     <h1>Hello,{{ name }}</h1>
{% endmacro %}

{# 调用宏 #}
{{ show_name(name) }}


# 宏的使用
@app.route('/macro/')
    def macro():
        # return render_template('macro.html', name = 'Nian')
        return render_template('macro2.html', name = 'dandan')

7、错误页面定制

错误页面定制
@app.errorhandler(404)
    def error(e):
         return render_template('404.html')


404.html

{% extends 'base.html' %}

{% block title %}
    出错了
{% endblock %}

{% block content %}
    <h1>找不见了吧@_@</h1>
{% endblock %}

--------------------------------------------------------------------------------------------------------------------------------------------------
静态文件
要引用静态文件，就要给它生成一个url地址 使用url_for 函数

url_for() 可以使用程序url映射中保存的信息生成URL 它最简单的用法就是以视图函数名作为参数 返回对用的url

如下
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

在模板目录下面的基模板给程序增加一个小图标
{% block head %}
{{ super() }}                                                          #使用super()获取（bootstrap/base.html的内容）
<link rel="icon" href="{{ url_for('static',filename='icon.jpg') }}"    #url_for()函数有两个参数，第一个参数是'static',第二参数就是给/static/里的filename参数传入值
      type="image/x-icon">                                             #这里的url_for()函数返回的地址就是'/static/icon.jpg'
{% endblock %}

路由
1、动态路由(url传参)

@app.route('/<name>')         #设置url传参数http://127.0.0.1:5000/lishurong
def first_flask(name):        # 视图必须有对应接受参数
    print(name)
    return 'Hello World'

2、接受整形数字参数

@app.route('/<int:age>/')       #设置url参数 http://127.0.0.1:5000/18/
def first_flask(age):           # 视图必须有对应接受参数
    print(age)
    return 'Hello World'

3、接受浮点型数字参数等

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#404错误页面 404.html

{% extends 'base.html'%}                              #模板继承,使用基础模板
{% block title %}404 - Page Not Found{% endblock %}   #title块,表示页面标题
{% block content %}                                   #content块  表示页面主体内容
<h1>Page Not Found</h1>
<p>You are lost...</p>
{% endblock %}




#505错误页面 505.html

{% extends 'base.html' %}
{% block title %}500 - Internal Server Error{% endblock %}
{% block content %}
<h1>Internal Server Error</h1>
<p>Something was wrong...</p>
{% endblock %}

-----------------------------------------------------------------------------------------------------------------------------------------------------
静态文件
要引用静态文件，就要给它生成一个url地址 使用url_for 函数

url_for() 可以使用程序url映射中保存的信息生成URL 它最简单的用法就是以视图函数名作为参数 返回对用的url

如下
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

在模板目录下面的基模板给程序增加一个小图标
{% block head %}
{{ super() }}                                                          #使用super()获取（bootstrap/base.html的内容）
<link rel="icon" href="{{ url_for('static',filename='icon.jpg') }}"    #url_for()函数有两个参数，第一个参数是'static',第二参数就是给/static/里的filename参数传入值
      type="image/x-icon">                                             #这里的url_for()函数返回的地址就是'/static/icon.jpg'
{% endblock %}

---------------------------------------------------------------------------------------------------------------------------------------------------