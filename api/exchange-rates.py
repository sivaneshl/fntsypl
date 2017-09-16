# Exchange rates app using fixer.io

import urllib.request, urllib.parse, urllib.error
import json

service_url = 'http://api.fixer.io/latest?'
retry = True
while retry == True:
    try:
        amount = int(input('Enter Amount: '))
        retry = False
    except:
        print('ERROR: Not A Valid Amount!!!')
        retry = True

retry = True
while retry == True:
    try:

        base_currency = input('Convert From Currency: ').upper()
        to_currency = input('Convert To Currency: ').upper()

        url = service_url + urllib.parse.urlencode({'base':base_currency,'symbols':to_currency})
        # print(url)

        url_handle = urllib.request.urlopen(url)
        output_data = url_handle.read().decode()
        retry = False
    except:
        print('ERROR: Invalid Currency!!!')
        retry = True

try:
    js = json.loads(output_data)
except:
    js = None
    print('ERROR: Failure to retrieve data from fixer.io')
    exit()

# print(js)
if 'rates' in js and len(js['rates']) > 0:
    if to_currency in js['rates']:
        exch_rate = float(js['rates'][to_currency])
        print('Exchange Rate:', exch_rate)
        print('Exchange Amount:', exch_rate * amount)
        exit()
print('ERROR: Cannot Convert From ', base_currency, 'To', to_currency, '!!!')
exit()
