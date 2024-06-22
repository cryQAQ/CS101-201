s = input()
ans = str()
for i in range(len(s)):
    if ord(s[i])>=ord('A') and ord(s[i])<= ord('Z'):
        ans += s[i].lower()
    elif ord(s[i])>=ord('a') and ord(s[i])<= ord('z'):
        ans += s[i].upper()
    else:
        ans += s[i]
print(ans)
