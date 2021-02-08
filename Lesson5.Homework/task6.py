def sum_int_str(string):
    l = len(string)
    sum = 0
    i = 0
    while i < l:
        s_int = ''
        a = string[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = string[i]
            else:
                break
        i += 1
        if s_int != '':
            sum += int(s_int)
    return sum


with open('file6.txt', 'r', encoding='utf-8') as f:
    result = {}
    for line in f:
        result.update({line.split()[0]: sum_int_str(line)})
print(result)
