from config import server
import hashlib
import requests

class validateLogin():
    def MD5(self,passwd):
        passwd = hashlib.md5(passwd.encode(encoding='UTF-8')).hexdigest()
        return passwd

    def verification(self,account,passwd):
        try:
            url = 'http://'+server['ip']+':5000/login?account='+account+'&passwd='+self.MD5(passwd)
            f = requests.get(url).content
            result = f.decode('utf-8')
            return result
        except Exception as e:
            return "E"



