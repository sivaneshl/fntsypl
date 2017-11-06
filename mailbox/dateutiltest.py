import dateutil.parser

tdate = '09 Dec xx 15:23:09 -0600'

print(dateutil.parser.parse(tdate).isoformat())
