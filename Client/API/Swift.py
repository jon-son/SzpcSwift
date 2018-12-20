from config import server
import requests
class swiftFusion():
    def download(self,path,filename):

        try:
            url = 'http://'+server['ip']+':5000/swift/download'
            data = {
                'filename':filename,
                'path':path
            }
            r = requests.get(url=url,params=data)
            print(len(r.content))
            length = 0
            with open('E:/TEMP/邓丽君-小城故事.mp3', 'wb') as f:
                for chunk in r.iter_content(chunk_size=1000):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        length +=len(chunk)
                        print("%d/%d"% (length,len(r.content)))

                f.close()
            return "success"

        except  Exception as e:
            print(e)
            return "erro"

