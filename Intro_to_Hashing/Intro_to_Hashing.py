import hashlib

s = 'id0-rsa.pub'

sha256_hash = hashlib.sha256(s.encode()).hexdigest()
md5_hash = hashlib.md5(sha256_hash.encode()).hexdigest()

print(md5_hash)
