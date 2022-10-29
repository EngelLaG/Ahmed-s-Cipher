from encrypt import encrypt_file
from decrypt import decrypt_file
from random import randint


def encrypt_tff(file_name):
    file1 = open(file_name,"r+")
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
    file1.close()
    file1 = open(file_name,"w")    
    file1.writelines(encrypted_lines)
    file1.close()
    file2 = open("ciphercodes.txt","w")
    file2.write(cipher)
    file2.close()


def decrypt_tff(file_name):
    file2 = open("ciphercodes.txt","r")

    cipher = file2.readlines()
    cipher = str(cipher)[2:-2]
    file2.close()


    file1 = open(file_name,"r+")
    lines = file1.readlines()
    temp=0
    decrypt_lines=[]
    file1.truncate(0)
    for line in lines:
        L = decrypt_file(int(cipher[temp]),line.strip()) + "\n"
        temp += 1
        decrypt_lines.append(L)
    file1.close()
    file1 = open(file_name,"w")    
    file1.writelines(decrypt_lines)
    file1.close()

encrypt_tff("file1.txt")
decrypt_tff("file1.txt")