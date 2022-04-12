_d={}
text=input("Text: ")
text=text.split()
for i in text:
    if i in _d:
        _d[i]=_d[i]+1
    else:
        _d[i]=1
print(_d)