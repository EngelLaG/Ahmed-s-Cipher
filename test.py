def pkey(text, key):
    pdkey = ''
    i=0
    for char in text:
        if char.isalpha():
            pdkey += key[i % len(key)]
            i += 1
        else:
            pdkey += ''
    return pdkey

def encryptchar(ptext,key2,mode ='encrypt'):
    if ptext.isalpha():
        First_chain = 'a'
        if ptext.isupper():
            First_chain = 'A'
        
        old_position = ord(ptext) - ord(First_chain)
        key2position = ord(key2.lower()) - ord('a')

        if mode == 'encrypt':
            new_position = (old_position + key2position) % 26
        else:
            new_position = (old_position - key2position +26) % 26
        return chr(new_position + ord(First_chain))
    return ptext

def encrypt(text, key):
    cipheredtext= ''
    pdkey = pkey(text, key)
    for ptext, key2 in zip(text, pdkey):
        cipheredtext += encryptchar(ptext, key2)
    return cipheredtext

def decrypt(cipheredtext, key):
    text = ''
    pdkey = pkey(cipheredtext, key)
    for cipheredtext2, key2 in zip(cipheredtext, pdkey):
        text+= encryptchar(cipheredtext2, key2, mode='decrtypt')
    return text




text = input('Messge to be Decrypted: ')
key = input('your Decryption Key: ')
cipheredtext= encrypt(text,key)
decryptedtext = decrypt(cipheredtext, key)
print(f'Cipheredtext: {cipheredtext}')
print(f'Decryptedtext: {decryptedtext}')