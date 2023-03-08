
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
s=0
for i in range(start,end + 1):
    if i % 3 == 0 and i % 10 == 4:
        s+=1
        print(i)