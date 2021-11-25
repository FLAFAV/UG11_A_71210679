def ambildanbalik(Sentence,Start,Stop,Boolean):
    if Boolean == True:
        Result = Sentence[Stop-1:Start-2:-1]
    else:
        Result = Sentence[Start-1:Stop]
    return Result

print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))