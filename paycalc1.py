hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Input is not a number!!!")
    quit()
    
if h <= 40:
    p = h * r
else:
    p = (40 * r * 1) + ((h - 40) * r * 1.6)
print(p)
