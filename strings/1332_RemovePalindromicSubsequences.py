s = "baabb"

count = 0
def pal(s):
    list = []
    for i in s:
        list.append(i)
    list.reverse()
    if s == "".join(list):
        return True
for i in range(len(s)):
    if pal(s) == True:
        count += 1
        break
    elif pal(s[i:])==True:
        s = s[i:]
        count +=1
    elif pal(s.lstrip()) == True:
        s = s[:i]
        count += 1
print(count)


