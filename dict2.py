
names = ['rooney', 'ronaldo', 'ronaldo', 'figo', 'adebayor', 'figo']

counts = dict()
for name in names:
    if name in counts:
        counts[name] = counts[name] + 1
    else:
        counts[name] = 1
print(counts)

counts1 = dict()
for name in names:
    counts1[name] = counts1.get(name, 0) + 1
print(counts1)
