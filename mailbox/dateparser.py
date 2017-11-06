from datetime import datetime

def dateparser(md):
    pieces = md.split()
    notz = " ".join(pieces[:4]).strip()
    print(notz)

    dnotz = datetime.strptime(notz,'%d %b %Y %H:%M:%S')
    print(dnotz)

dateparser('09 Dec 2005 15:23:09 -0600')
