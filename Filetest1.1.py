from encrypt import encrypt_file
from decrypt import decrypt_file
from random import randint



file1 = open("file1.txt","r+")
lines = file1.readlines()
cipher = ''
encrypted_lines=[]
file1.truncate(0)
for line in lines:
    if len(line.strip())>9:
        key=randint(2,9)
    elif(len(line.strip())<3):
        key=1
    else:
        key=randint(2,len(line.strip())-1)
    L = encrypt_file(key,line.strip()) + "\n"
    encrypted_lines.append(L)
    cipher += str(key)
file1.writelines(encrypted_lines)