def hitung_hapus():
    Sentence = input("Masukkan kalimat: ")
    Start = int(input("Index Start: "))
    Stop = int(input("Index Stop: "))
    a = Stop - Start + 1
    b = len(Sentence)
    Result = (a/b)*100
    
    if Result < 0:
        return 0.0
    else:
        return Result


print(hitung_hapus())