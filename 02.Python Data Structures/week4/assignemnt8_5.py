fname = input("Enter file name: ")
#use mbox-short.txt

fh = open(fname)
count = 0

for line in fh:
    line=line.rstrip()
    if not line.startswith('From '): continue
   
    s=line.split()
    print(s[1])
    count=count+1

print("There were", count, "lines in the file with From as the first word")
