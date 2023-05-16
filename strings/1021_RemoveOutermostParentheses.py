o=0
c=0
out = ""
s = "(()())(())(()(()))"
for i in s:
    if i == "(":
        o += 1
    else:
         c += 1
    if o == c:
        out = out + "()"*(o//2)
print(out)
#not reaching the ans still :(
