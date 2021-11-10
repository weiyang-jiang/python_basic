import pymysql
import json
# 路由列表
route_list = []
# 数据库连接信息
code_list = []
database_conn = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"root",
    "database":"stock_db",
    "charset":"utf8"
}
# 数据库上下文管理器（里面需要传入 连接数据库的连接信息，sql语句，选填执行sql语句时插入的变量）
class database_open(object):
    def __init__(self,database_conn,sql,data_code=None):
        self.database_conn = database_conn
        self.sql = sql
        self.data_code = data_code
        # 当调用with开始时执行的代码
    def __enter__(self):
        self.conn = pymysql.connect(**self.database_conn)
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(self.sql,self.data_code)
            # 判断是否是查询sql语句
            if self.sql.startswith("select"):
                data = self.cursor.fetchall()
            else:
                data = None
            self.conn.commit()
            return data
        except Exception as e:
            self.conn.rollback()
            return "sql语句出错了"
    # 当with跳出时执行的函数，关闭数据库和游标的连接
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.close()


# 把所有的股票信息的代号插入到路由列表，方便之后建立起添加和删除的网页
def code_load():
    sql = "select code from info;"
    with database_open(database_conn,sql) as data:
        codes = data
    for code in codes:
        route_list.append((f"/add/{code[0]}.html",code[0]))
        route_list.append((f"/del/{code[0]}.html",code[0]))
code_load()

# 避免重复插入数据，首先把已经插入的数据全部查找出来放到一个数据列表中
def aviod_repeat():
    sql = "select i.code from info i inner join focus f on i.id = f.info_id;"
    with database_open(database_conn,sql) as data:
        ids = data

    for id in ids:
        code_list.append(id[0])
aviod_repeat()

# 定义一个装饰器，用于把访问指定页面的所执行的函数插入到路由列表之中
def route_path(path):
    def route_list_dec(func,*args,**kwargs):
        route_list.append((f"/{path}.html", func))
        def inner(*args,**kwargs):
            result = func(*args,**kwargs)
            return result
        return inner
    return route_list_dec

# 访问主页的时候执行的函数
@route_path("index")
def index():
    response_line = "HTTP/1.1 200 OK\r\n"
    with open("template/index.html", "rb") as file:
        file_data = file.read()
    file_data = file_data.decode("utf8")
    data = index_data()
    file_data = file_data.replace("{%content%}",data)
    file_data = file_data.encode("utf8")
    print("框架：请求成功！")
    return response_line, file_data

# 访问个人中心时执行的代码
@route_path("center")
def center():
    response_line = "HTTP/1.1 200 OK\r\n"
    with open("template/center.html", "rb") as file:
        file_data = file.read()
    file_data = file_data.decode("utf8")
    file_data = file_data.encode("utf8")
    print("框架：请求成功！")
    return response_line, file_data

# 没有找到资源时执行的代码
def not_found():
    data_path = "/error.html"
    with open("static" + data_path, "rb") as file:
        file_data = file.read()
    response_line = "HTTP/1.1 404 Not Found\r\n"
    print("框架：资源找不到了")
    return response_line, file_data

# 服务器内部出现错误时执行的代码
def error():
    response_line = "HTTP/1.1 500 Error\r\n"
    print("出错了")
    file_data = "服务器内部出错了".encode("utf8")
    return response_line, file_data

# 创建一个个人数据中心的接口api
@route_path("center_data")
def center_data_socket():
    response_line = "HTTP/1.1 200 OK\r\n"
    sql = "select i.code, i.short, i.chg, i.turnover,i.price, f.note_info, i.highs from info i inner join focus f on i.id = f.info_id;"
    with database_open(database_conn,sql) as data:
        rows = data
    dict_data = [{"code": row[0], "short": row[1], "chg": row[2], "turnover": row[3], "price": str(row[4]),
                  "note_info": row[5], "highs": str(row[6])} for row in rows]
    json_data = json.dumps(dict_data, ensure_ascii=False)
    json_data = json_data.encode("utf8")
    return response_line,json_data

# 将主页的股票信息从数据库中拿出来，之后调用插入到主页的html文件当中
def index_data():
    sql = "select id,code,short,chg,turnover,price,highs,time,code from info;"
    with database_open(database_conn,sql) as data:
        rows = data
    datas = ""
    for row in rows:
        datas += """<tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule=%s></td>
               </tr>""" % row
    return datas



# 通过股票代号，把指定的股票插入到个人中心的数据库中去
def add_data(data_code):
    sql = "insert into focus(info_id) select id from info where code = %s group by id;"
    with database_open(database_conn,sql,(data_code,)) as data:
        pass

# 通过股票代号，查询出指定的股票信息，并返回一个json格式的api接口
def find_data(data_code):
    response_line = "HTTP/1.1 200 OK\r\n"
    sql = "select i.code, i.short, i.chg, i.turnover,i.price, f.note_info, i.highs from info i inner join focus f on i.id = f.info_id and i.code = %s;"
    with database_open(database_conn,sql,(data_code,)) as data:
        row = data[0]
    dict_data = [{"code": row[0], "short": row[1], "chg": row[2], "turnover": row[3], "price": str(row[4]),
                  "note_info": row[5], "highs": str(row[6])}]
    json_data = json.dumps(dict_data, ensure_ascii=False)
    json_data = json_data.encode("utf8")
    return response_line,json_data


# 要删除数据的时候执行的代码
def del_data(data_code):
    sql = "delete from focus where info_id = (select id from info where code = %s);"
    with database_open(database_conn,sql,(data_code,)) as data:
        pass


# 一个空函数，用于之后判断类型使用
def function_type():
    pass


# 主要的执行框架
def frame_work(env):
    try:
        data_path = env["data_path"] # 拿到浏览器传给服务器的网址
        referer = env["referer"] # 拿到浏览器传给服务器的referer
        for Route,func in route_list: # 遍历循环路由列表，用于判断一下该网址是否和路由列表里面的信息对应
            if data_path == Route and type(func) == type(function_type):  # 如果网址存在而且，func的类型为函数类型 说明该路由是一个要访问主页或个人中心网址的路由
                result = func() # 执行指定网址要执行的函数
                return result  # 返回一个响应头和网页数据
            elif data_path == Route and type(func) == type("字符串") and data_path.startswith("/add"): # 如果网址存在，但是func的类型是字符串，网址的开头是add说明浏览器要添加数据
                if referer == "站内访问" and func in code_list: # 如果referer是站内访问，而且指定数据在已经存在于这个个人中心数据库
                    response_line,file_data = find_data(func) # 执行查找指定数据的函数
                    file_data = (file_data.decode("utf8") + "此条数据已添加过").encode("utf8")  # 将api数据增加说明信息
                    return response_line,file_data # 返回一个响应头和网页数据
                elif referer == "站内访问" and func not in code_list: # 如果referer是站内访问但是指定数据不在个人中心数据库中
                    add_data(func)  # 向个人中心数据库添加指定信息
                    code_list.append(func)  # 再向数据列表中添加这一条数据，方便以后排除这条数据，避免了重复添加的操作
                    result = find_data(func)  # 执行查找指定数据的函数
                    return result  # 返回响应头和网页api数据
                elif referer == "站外访问" and func in code_list: # 如果referer是站外访问，而且这条数据已经在个人中心数据库中，不做添加操作
                    result = find_data(func)  # 执行查找指定数据的函数
                    return result  # 返回响应头和网页api数据
                elif referer == "站外访问" and func not in code_list:  # 如果referer是站外访问，但是这条数据不在个人中心数据库中，那么要告知用户这条数据不在
                    response_line = "HTTP/1.1 200 OK\r\n"
                    file_data = "该用户没有添加这条数据".encode("utf8") # 网页数据直接为没有添加数据
                    return response_line,file_data  # 返回响应头和网页数据
                else:
                    result = error() # 如果以上情况都不存在，那么说明服务器出问题了
                    return result # 返回响应头和出错时要给用户呈现的网页数据
            elif data_path == Route and type(func) == type("字符串") and data_path.startswith("/del"):# 如果网址存在，但是func的类型是字符串，网址的开头是del说明浏览器要删除数据
                if referer == "站内访问" and func in code_list: # 如果是站内访问，而且这条数据在个人中心数据库中，那么可以进行删除操作
                    response_line, file_data = find_data(func)
                    file_data = (file_data.decode("utf8") + "此条数据已删除").encode("utf8")
                    del_data(func) # 删除指定的数据
                    return response_line, file_data
                elif referer == "站外访问" and func in code_list:  # 如果是站外访问，数据还在个人中心数据库中，那么不允许删除操作，可以返回这条要删除的数据
                    response_line = "HTTP/1.1 200 OK\r\n"
                    file_data = "不允许进行删除操作".encode("utf8")
                    return response_line,file_data
                elif func not in code_list: # 如果数据库中不存在这条信息那么就告知用户没有这条信息
                    response_line = "HTTP/1.1 200 OK\r\n"
                    file_data = "该用户没有添加这条数据".encode("utf8")
                    return response_line, file_data
                else: # 以上情况都没有发生，说明了服务器内部出现了问题
                    result = error()
                    return result

        else: # 通过遍历路由列表没有找到和指定网页相同的信息，执行没有找到的函数
            result = not_found()
            return result
    except: # try里面的代码执行错误。返回服务器内部出现问题
        result = error()
        return result


if __name__ == '__main__':
    pass