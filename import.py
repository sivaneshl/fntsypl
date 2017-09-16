import re

find_members = list()
for member in (re.__all__):
    if member.startswith('find'):
        find_members.append(member)

find_members.sort
print(find_members)
