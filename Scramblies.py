def scramble(s1, s2):
    s1_condition = ''
    s1_list = []
    for i in s1:
        s1_list.append(i)
    for letter in s1_list:
        if letter in s2:
            s1_condition += letter
            s2 = s2.replace(letter, '')
            print(s2)
            if s2 == '':
                return True
    if len(s1) < len(s2):
        return False
    elif s1_condition == s2:
        return True