ab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

c = 'ZNKIGKYGXIOVNKXOYGXKGRREURJIOVNKXCNOINOYXKGRRECKGQOSTUZYAXKNUCURJHKIGAYKOSZUURGFEZURUUQGZZNKCOQOVGMKGZZNKSUSKTZHAZOLOMAXKOZYMUZZUHKGZRKGYZROQKLOLZEEKGXYURJUXCNGZKBKXBGPJADLIVBAYKZNUYKRGYZZKTINGXGIZKXYGYZNKYURAZOUT'

for i in range(26):
    m = ''
    for x in c:
        i2 = (ab.index(x) + i) % 26
        c2 = ab[i2]
        m += c2
    print(f'{ab[i]}: {m}\n\n')
