m1 = 'Deposit amount: 5 dollars'
c1 = '0x5797791557579e322e619f12b0ccdee8802015ee0467c419e7a38bd0a254da54'
m2 = 'One million dolls is quite the collection'
c2 = '0xb1e952572d6b8e00b626be86552376e2d529a1b9cafaeb3ba7533d2699636323e7e433c10a9dcdab2ed4bee54da684ca'
m3 = 'Hey nice binoculars'
c3 = '0x35d0c02036354fdf6082285e0f7bd6d2fdf526bd557b045bce65a3b3e300b55e'

c1 = c1[2:]
c2 = c2[2:]
c3 = c3[2:]

block_size_bytes = 16
block_size_bits = block_size_bytes*8
block_size_hex = block_size_bits//16  # 8
block_size_chars = block_size_hex//2  # 4

m_attack = ''
c_attack = ''

m_attack += m1[:4*block_size_chars]
c_attack += c1[:4*block_size_hex]

m_attack += m2[:4*block_size_chars]
c_attack += c2[:4*block_size_hex]

m_attack += m3[4*block_size_chars:]
c_attack += c3[4*block_size_hex:]

print(m_attack)
print(c_attack)
