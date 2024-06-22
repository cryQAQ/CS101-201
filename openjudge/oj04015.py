while True:
    try:
        m = input()
        if m.count('@') == 1 and m[0]!='@' and m[0]!='.' and m[-1]!='.' and m[-1]!='@' and m.find('@') < m.rfind('.')-1 and m[m.find('@')+1] != '.' and m[m.find('@')-1]!='.':
            print('YES'); continue
        else:
            print('NO'); continue
    except EOFError:
        break
