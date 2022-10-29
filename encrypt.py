def encrypt_file(key, temp_string):
    temp = []
    temp_num = 0
    ende = ""

    for i in range(key):
        temp.append([])
    for j in temp_string:
        temp[temp_num].append(j)
        temp_num += 1
        if temp_num == key: temp_num = 0
    for i in range(key):
        for j in temp[i]:
            ende += j

    return ende
