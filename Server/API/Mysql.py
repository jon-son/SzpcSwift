# -*- coding: utf-8 -*-
# by jonson 2018/10/27
from config import mysqlConf
import pymysql



class SelectMySQL(object):
    def select_data(self, sql):

        try:
            conn = pymysql.connect(host=mysqlConf['ip'], port=mysqlConf['port'], user=mysqlConf['username'],
                                   password=mysqlConf['passwd'], database=mysqlConf['DB'])
            cur = conn.cursor()
            cur.execute(sql)
            cur.close()
            conn.close()
            alldata = cur.fetchall()
        except Exception as e:
            print('Error msg: ' + str(e))
            return "E"
        if len(alldata) == 1:
            return "T"
        else:
            return "F"