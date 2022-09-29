import math

# values copied from
#  openssl rsa -in key_[12].pub -pubin -noout -text

# modulus
N_s = '''00:ac:e5:e5:58:20:49:76:ff:26:6d:a8:aa:43:de:
    45:0c:2d:a6:61:a5:2e:72:53:36:b7:b8:2c:ac:77:
    55:49:63:b4:bc:d8:5a:3e:31:a0:6f:9a:1c:1a:2e:
    c0:94:fb:0f:27:a2:6e:96:ac:08:7f:18:75:ea:eb:
    e3:32:06:4c:d5'''

N2_s = '''00:fb:2b:a7:0c:79:e8:e4:e5:2a:d1:80:5a:7d:b8:
    6e:8e:47:52:0d:f1:62:d9:f3:9d:38:f5:5f:ff:07:
    ab:ba:4b:60:d2:15:13:9e:d8:c6:8c:ab:df:34:ce:
    38:12:6e:7e:04:cd:cd:d2:92:d1:17:39:4e:2e:33:
    65:49:02:91:0b:e9'''

e = 65537

c_hex = '0xf5ed9da29d8d260f22657e091f34eb930bc42f26f1e023f863ba13bee39071d1ea988ca62b9ad59d4f234fa7d682e22ce3194bbe5b801df3bd976db06b944da'


N = int(N_s.replace(" ", "").replace("\n", "").replace(":", ""), 16)
N2 = int(N2_s.replace(" ", "").replace("\n", "").replace(":", ""), 16)

p = math.gcd(N, N2)
q = N//p

totient = (p - 1)*(q - 1)
d = pow(e, -1, totient)

c = int(c_hex[2:], 16)
m = pow(c, d, N)

print(hex(m)[2:])
