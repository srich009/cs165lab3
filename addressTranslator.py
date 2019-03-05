import pyperclip
import sys

address = sys.argv[1][2:]
result = ""
l = [address[i:i + 2] for i in range(0, len(address), 2)]
l.reverse()
for i in l:
    result += '\\x' + i
pyperclip.copy(result)
spam = pyperclip.paste()
print('translated address is on your clipboard')