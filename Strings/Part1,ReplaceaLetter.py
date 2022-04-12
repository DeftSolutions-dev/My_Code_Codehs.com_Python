# update the function body to return the input `string` 
# with the character at `index` replaced with a dash (-)
def replace_at_index(string, index):
    new_txt = ""
    for x in range(len(string)):
        if x == index:
            new_txt+="-"
        else:
            new_txt+=string[x]
    return new_txt
print(replace_at_index("eggplant",3))