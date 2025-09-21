s = input()
subs = set()
for i in range(len(s)):
    for j in range(1, len(s)+1):
        subs.add(s[i:i+j])
print(len(subs))