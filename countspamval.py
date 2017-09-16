# Use the file name mbox-short.txt as the file name
def getspamval(inline):
    spos = inline.find(":") + 1;
    spamval = float(inline[spos:]);
    return spamval;
    

fname = input("Enter file name: ")
fh = open(fname)
i = 0
s = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
	
    i = i + 1
    s = s + getspamval(line)
    
        
print("Average spam confidence:", s / i)
