from django.shortcuts import render

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello django. I am comming.")

# Create your views here.

from django.shortcuts import render, redirect

from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello django. I am comming.")


def login(request):
    if request.method == "GET":
        username = request.GET.get("username")
        password = request.GET.get("password")
        
        import pymysql
        #连接数据库
        db=pymysql.connect(host = '127.0.0.1' # 连接名称，默认127.0.0.1
        ,user = 'root' # 用户名
        ,passwd='qq2576729985' # 密码
        ,port= 3306 # 端口，默认为3306
        ,db='testwork' # 数据库名称
        ,charset='utf8' # 字符编码
        )

        sql="select * from user " # SQL语句
        cursor = db.cursor() # 生成游标对象
        cursor.execute(sql)
        all_users=cursor.fetchall()
        cursor.close()
        db.close()
        i=0
        while i<len(all_users):
            if all_users[i][2]==username and all_users[i][3]==password :
                return redirect("/come_in")
            i=i+1
    return render(request,"login.html")

def come_in(request):
    return render(request,"come_in.html")

from django.http import JsonResponse
