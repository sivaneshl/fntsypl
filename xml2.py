import xml.etree.ElementTree as ET

data = '''<stuff>
    <users>
        <user x='2'>
            <id>001</id>
            <name>Rooney</name>
        </user>
        <user x='4'>
            <id>002</id>
            <name>Ozil</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(data)
lst = stuff.findall('users/user')
print('User count:',len(lst))
for item in lst:
    print(item.get('x'), item.find('id').text, item.find('name').text)
