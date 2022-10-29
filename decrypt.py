def decrypt_file(key, temp_string):
    ende = ""
    temp2 = []
    temp_num2 = 0

    for i in range(key):
        temp2.append([])
    for j in temp_string:
        temp2[temp_num2].append(" ")
        temp_num2 += 1
        if temp_num2 == key: temp_num2 = 0
    for i in range(len(temp2)):
        for j in range(len(temp2[i])):
            temp2[i][j] = temp_string[0]
            temp_string = temp_string[1:]
    for i in range(len(temp2[0])):
        for j in range(key):
            if i < len(temp2[j]):
                ende += temp2[j][i]

    return ende