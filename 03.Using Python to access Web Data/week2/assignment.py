import re

sample_file = open('re.txt')


handle = sample_file.read()

total=0
number_regex = '[0-9]+'
numbers = re.findall(number_regex, handle) 
#total = sum(int(num) for num in numbers)

for num in numbers:
	total=total+int(num)

print(total)


sample_file.close()


