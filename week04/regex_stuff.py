import re

datestring = "06/18/85 Primary Care Doctor, 12/13/2022 another date"

# date -> 2 digits / 2 digits / 2 digits
pattern = r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{2,4}"
#pattern = r"12/13/2022"

result = re.findall(pattern, datestring)

print(result)

