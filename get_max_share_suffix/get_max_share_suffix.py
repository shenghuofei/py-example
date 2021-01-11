def find_sufix(l):
    i = 1
    if len(l[0]) == 0:
        return ""
    for c in range(0, len(l[0])):
        ch = l[0][len(l[0]) - i]
        flag = True
        for s in range(1,len(l)):
            if len(l[s]) < i:
                flag = False
                break
            if l[s][len(l[s])-i] == ch:
                continue
            else:
                flag = False
                break
        if not flag:
            return l[0][len(l[0])-i+1:len(l[0])]
        i += 1

l = ['abcabc', 'dbc', 'asfsdfbc', 'qfdsbc']
print find_sufix(l)
