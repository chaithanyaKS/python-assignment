nums = []
while True:
    num = input('Enter a number or done to finish: ')
    if num == 'done':
        break
    nums.append(int(num))

print(f'Max: {max(nums)}, Min: {min(nums)}')