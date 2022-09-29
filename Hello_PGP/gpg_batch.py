import gnupg

gpg = gnupg.GPG(gnupghome='/Users/brian/')

d = '''-----BEGIN PGP MESSAGE-----
Version: GnuPG v1

jA0ECQMC8YL5GvIZ2m5g0ksB9aj386dbfatZ28jsaLEKtUcRLVjjHHIBmHvCIrxf
RIeH7NLMcfQ+3Z+/ktIu3Drocg9zoiP1eaJ6aUUpa6fLy0OPjIIpG9tM/Mo=
=S+SO
-----END PGP MESSAGE-----
'''

f_words = open('/usr/share/dict/words', 'r')
word_list = f_words.readlines()
f_words.close()

for i in range(len(word_list)):
    word = word_list[i].split()[0]
    if i % 100 == 0:
        print(i)
    a = gpg.decrypt(d, passphrase=word)
    if a.ok:
        print(word)
        print(a.data)
        break
