# -*- coding: utf-8 -*-
# by jonson 2018/10/27

from flask import Flask,send_file
from API import Mysql,Swift
from config import swiftConf
from flask_restful import reqparse, abort, Api, Resource,request
from io import BytesIO

app = Flask(__name__)
api = Api(app)


# # 操作（post / get）资源列表TodoList
class LoginRoute(Resource):
    def get(self):
        account = request.args.get('account')
        passwd = request.args.get('passwd')
        select = Mysql.SelectMySQL()
        sql = 'select * from user_list where account="'+account+'" and passwd="'+ passwd+'"'
        result = select.select_data(sql)
        return result


class SwiftRoute(Resource):
    def get(self):
        filename = request.args.get('filename')
        path = request.args.get('path')
        swift = Swift.swiftFunsion()
        file = swift.download(swiftConf['container'],path, filename)
        byte_io = BytesIO(file)
        x = send_file(filename_or_fp=byte_io, mimetype='audio/x-mpeg')
        return x


# 设置路由
api.add_resource(LoginRoute, '/login')
api.add_resource(SwiftRoute, '/swift/download')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
