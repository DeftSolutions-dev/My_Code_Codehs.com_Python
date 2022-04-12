_d={}
text=input("Text: ")
text=text.split(" ")
for i in range(len(text)):
    _d[text[i]]=0
for i in range(len(text)):
    _d[text[i]]=int(_d[text[i]])+1
print(_d)
def update_counts(count_dictionary, word):
    _d={}
update_counts(_d,text)