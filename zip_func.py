#zip()

x = [1,2,3]
y = [4,5,6]
zipped_list = list(zip(x,y))
print(zipped_list)

#unzip
x1,y1 = zip(*zipped_list)
print(x1,y1)
