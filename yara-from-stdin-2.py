import sys
import re

data = sys.stdin.readlines()

hexregex = re.compile(r'[a-z0-9]{2} ([a-z0-9]{2})( ([a-z0-9]{2}))*')

print("\n")

a = 1

print("rule r{")
print("strings:")

for line in data:
    line = line.strip()
    matched_hexregex = hexregex.match(line) 
    if matched_hexregex:
        newline = '$a'+ str(a) + ' = {' + line + '}'
    else:
        line = line.replace('\\',"\\\\")
        line = line.replace('\"',"\\\"")
        newline = '$a' + str(a) + ' = \"' + line + '\"' 
    
    print(newline)
    a += 1

print("condition: any of them")
print("}")