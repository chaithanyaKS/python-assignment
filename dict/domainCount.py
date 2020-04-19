import re

regex = r'\S+\.\S+'
domains = {}
input_file = input('Enter the filename: ')
with open(input_file) as fp:
    for data in fp.readlines():
        if data.startswith('From'):
            a = data[data.index('@')+1: ]
            domain = re.findall(regex, a)
            if domain[0] in domains:
                domains[domain[0]] +=1
            else:
                domains[domain[0]] = 1
                
for key, value in domains.items():
    print(f'{key} : {value}')
            