# sets

#list of non-duplicate entries
print(set("my name is Eric and Eric is my name".split()))

a = set(["one","two","ten"])
b = set(["one","six"])

# intersection
print(a.intersection(b))
print(b.intersection(a))

# symetric difference -- not intersection
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# union
print(a.union(b))
print(b.union(a))

# difference
print(a.difference(b))
print(b.difference(a))
