import hashlib
import base58

private_key = 94176137926187438630526725483965175646602324181311814940191841477114099191175

# Bitcoin secp256k1 curve parameters (p, a, b, G) obtained from:
#  http://www.secg.org/sec2-v2.pdf

secp256k1_p = int('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F', 16)
secp256k1_a = 0
secp256k1_b = 7
secp256k1_G = '0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798'

p = secp256k1_p
a = secp256k1_a
b = secp256k1_b

Gx = int(secp256k1_G[2:], 16)
G_parity = int(secp256k1_G[:2])

z = Gx**3 + a*Gx + b
mod_sqrt_pow = (p+1)//4
y1 = pow(z, mod_sqrt_pow, p)
y2 = p - y1

if G_parity == 2:
    if y1 % 2 == 0:
        Gy = y1
    else:
        Gy = y2

else:
    if y1 % 2 == 1:
        Gy = y1
    else:
        Gy = y2

G = (Gx, Gy)


def point_add(P, Q):
    l = (Q[1] - P[1]) * pow(Q[0] - P[0], p-2, p)
    xr = (l*l - P[0] - Q[0]) % p
    yr = (l*(P[0] - xr) - P[1]) % p

    return (xr, yr)


def point_dbl(P):
    l = (3*P[0]*P[0] + a)*pow(2*P[1], p-2, p)
    xr = (l*l - P[0] - P[0]) % p
    yr = (l*(P[0] - xr) - P[1]) % p

    return (xr, yr)


def double_and_add(P, k):
    if k == 0:
        return (0, 0)
    elif k == 1:
        return P
    elif k % 2 == 1:
        return point_add(P, double_and_add(P, k-1))
    else:
        return double_and_add(point_dbl(P), k//2)



public_key = double_and_add(G, private_key)
public_key_hex = f'04{hex(public_key[0])[2:]}{hex(public_key[1])[2:]}'
#public_key_hex = f'02{hex(public_key[0])[2:]}'

public_key_bytes = int(public_key_hex, 16).to_bytes(65, 'big')

pk_sha256 = hashlib.sha256(public_key_bytes).digest()
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(pk_sha256)
pk_ripemd160 = ripemd160.hexdigest()

extended_hex = f'00{pk_ripemd160}'
i = int(extended_hex, 16)
num_bytes = (i.bit_length()+7)//8 + 1
extended_bytes = i.to_bytes(num_bytes, 'big')

checksum = hashlib.sha256(hashlib.sha256(extended_bytes).digest()).hexdigest()[:8]
address_hex = f'00{pk_ripemd160}{checksum}'

i = int(address_hex, 16)
num_bytes = (i.bit_length()+7)//8 + 1
b = i.to_bytes(num_bytes, 'big')

bitcoin_address = base58.b58encode(b).decode()

import cryptos
assert cryptos.privtoaddr(private_key) == bitcoin_address

print(bitcoin_address)
