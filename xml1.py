import xml.etree.ElementTree as ET

data = '''<person>
    <name>Rooney</name>
    <phone type='intl'>
        +1 234 567 8910
    </phone>
    <email hide='true'/>
    </person>'''
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Phone:', tree.find('phone').text, tree.find('phone').get('type'))
emailtag = tree.find('email')
print('Email:', emailtag.text, emailtag.get('hide'))

if emailtag.text == None:
    print(True)
else:
    print(False)
