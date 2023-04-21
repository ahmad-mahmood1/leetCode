def removeAdjacentDuplicates(str):
    if len(str) == 1:
        return str
    i = 0
    while i < len(str) - 1:
        if str[i] == str[i + 1]:
            char = str[i]
            str = str.replace(char + char, "")
            i = i - 1 if i != 0 else 0
        else:
            i += 1
    return str

print(removeAdjacentDuplicates("abzzby"))


### Can also be done with stack implementation -> stack element, before inserting check if head == element then pop otherwise insert. 