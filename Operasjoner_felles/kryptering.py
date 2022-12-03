from hashlib import sha256

def krypter (string):
    kryptert = sha256(string.encode("utf-8")).hexdigest()
    return kryptert
