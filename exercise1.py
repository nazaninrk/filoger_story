text = input("Please enter the text: ")
mydict = {}

for char in text:
    if char.isalnum():
        if char in mydict:
            mydict[char] += 1
        else:
            mydict[char] = 1

max_key_length = max(len(str(key)) for key in mydict.keys()) +2
max_value_length = max(len(str(value)) for value in mydict.values()) +2


print("+" + "-"*12 + "+" + "-"*12 + "+")
print("| {:^10} | {:^10} |".format("Name", "Frequency"))
print("+" + "="*12 + "+"+"=" + "="*11 + "+")

for key, value in mydict.items():
    print("| {:^10} | {:^10} |".format(key, value))
    print("+" + "-"*12 + "+" + "-"*12 + "+")