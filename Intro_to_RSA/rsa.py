e_hex, N_hex = ('0x3', '0x64ac4671cb4401e906cd273a2ecbc679f55b879f0ecb25eefcb377ac724ee3b1')

d_hex = '0x431d844bdcd801460488c4d17487d9a5ccc95698301d6ab2e218e4b575d52ea3'
c_hex = '0x599f55a1b0520a19233c169b8c339f10695f9e61c92bd8fd3c17c8bba0d5677e'

e = int(e_hex, 16)
N = int(N_hex, 16)

d = int(d_hex, 16)
c = int(c_hex, 16)

m = pow(c, d, N)
print(hex(m))
