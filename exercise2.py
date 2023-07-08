from collections import Counter as C
from tabulate import tabulate as T
print(T(C(filter(str.isalnum, input("Please enter the text: "))).most_common(), headers=[" Name ", "Frequency"], tablefmt="pretty"))