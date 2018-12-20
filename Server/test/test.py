from API import Mysql
select = Mysql.SelectMySQL()
sql = 'select * from user_list where account=16240620 and passwd="e10adc3949ba59abbe56e057f20f883e"'
result = select.select_data(sql)
print(result)