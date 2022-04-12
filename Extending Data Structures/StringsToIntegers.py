# Write your function here...


list_of_strings = ["a", "2", "7", "zebra"]


# Your code here...
def safe_int(string):
    return int(string) if string.isdigit() else 0
list_of_number = [safe_int(num)for num in list_of_strings]
print(list_of_number)