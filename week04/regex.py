import re

def find_name(line):
    # print(line)
    
    # pattern = r'([A-Z][a-z]+ [A-Z][a-z]+)'
    # result = re.findall(pattern,line)
    
    title = r"(?:(?:Mrs|Mr|Ms|Dr|Rev)[. ])?"
    first = r"[A-Z][a-z]+,?[ ]+"
    mid = r"(?:[A-Z][a-z]*[.]?[ ]*)?"
    last = r"[A-Z][a-z]+"

    result = re.findall(title + first + mid + mid + last, line)

    return result


file = open(r'week04/names.txt')
lines = file.readlines()
print("\nLooking for Names...\n")
#print(file)
#print(lines)
i=0

for line in lines:
    
    #print("line",i,":", line)
    result = find_name(line)
    if (len(result)>0):
        print(result)
    i += 1

print('\n...',i,"total lines processed\n")

