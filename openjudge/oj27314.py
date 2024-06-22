L = list(input().split())
replace = list(input().split())
ans = []
for i in range(len(L)):
    if L[i][-1] in ':.,':
        if L[i][:-1].lower() == replace[0].lower():
            if i == 0 or L[i - 1][-1] == '.':
                ans.append(replace[1].title() + L[i][-1])
            else:
                ans.append(replace[1].lower() + L[i][-1])
        else:
            if i == 0 or L[i - 1][-1] == '.':
                ans.append(L[i].title())
            else:
                ans.append(L[i].lower())
    else:
        if L[i].lower() == replace[0].lower():
            if i == 0 or L[i - 1][-1] == '.':
                ans.append(replace[1].title())
            else:
                ans.append(replace[1].lower())
        else:
            if i == 0 or L[i - 1][-1] == '.':
                ans.append(L[i].title())
            else:
                ans.append(L[i].lower())
print(' '.join(ans))