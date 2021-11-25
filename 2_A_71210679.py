def ambil_tengah (x,n = None):
    if n == None:
        Length = len(x)
        Count = (round(Length/2))
        return(x[Count])
    else:
        Length = len(x)
        Count = (round(Length/2))
        return (x[Count+n-1])

print(ambil_tengah("abcdefg",1))
print(ambil_tengah("abcdefg",2))
print(ambil_tengah("abcd"))