import hashlib

class MD5():
    def file_md5(filename):
        fd = open(filename, "rb")
        fstr = fd.read()
        fd.close()
        fmd5 = hashlib.md5(fstr)
        return fmd5.hexdigest()

    def str_md5(str):
        md5 = hashlib.md5()
        md5.update(str.encode("utf8"))
        return md5.hexdigest()