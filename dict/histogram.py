hist = {}
file_name = input('Enter the filename: ')
with open(file_name) as fp:
    for data in fp.readlines(): 
        if(data.startswith('From ')):
            a = data.strip('From ')
            mail = a[:a.index(' ')]
            if mail in hist:
                hist[mail] += 1
            else:
                hist[mail] = 1
for key, value in hist.items():
    print(f'{key}: {value}')

max_email_sent = 0
mail = ''
for key, values in hist.items():
    if hist[key] > max_email_sent:
        mail = key
        max_email_sent = hist[key]
print(f'{mail} : {max_email_sent}')