n = input()
s = input()
if s.count('D') > s.count('A'):
    print('Danik')
elif s.count('A') > s.count('D'):
    print('Anton')
else:
    print('Friendship')