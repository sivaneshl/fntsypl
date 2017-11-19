def FirstFactorial(num):
    num = int(num)
    s = num
    for i in range(num - 1):
        s = s * (i + 1)
    return s

# keep this function call here
print (FirstFactorial(input()))
