fhand = open('while2.py');
print(fhand);

for eachline in fhand:
    print(eachline.rstrip());
    
fhand = open('while2.py');    
x = fhand.read();
print(len(x));

