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
    print (all_users[i])
    i=i+1