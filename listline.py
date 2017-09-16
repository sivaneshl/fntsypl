fname = input("Enter a file name: ")

try:
    fhand = open(fname)
except:
    print("Enter a valid file name!!!")
    quit()

count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    print(line.split()[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
