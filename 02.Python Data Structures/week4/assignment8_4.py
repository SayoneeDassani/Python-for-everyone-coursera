fname = input("Enter file name: ")
fh = open(fname)
text=list()
lst = list()
for line in fh:
    line =line.rstrip()
    line=line.split()
    for i in line:
        
     if i in text:
        continue
     else:
        text.append(i)
text.sort()
print(text)
#use romeo.txt as file
