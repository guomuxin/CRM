import hashlib

def md5_encry(value,salt):
    md5 = hashlib.md5(salt.encode("utf-8"))
    md5.update(value.encode('utf-8'))
    return md5.hexdigest()