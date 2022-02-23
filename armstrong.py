number=input("Enter a number: ")
basamak=len(number)
toplam=0
rakam=0
s=int(number)

for i in range(0,basamak):
    rakam=int(number[i])
    toplam=toplam+rakam**basamak
if toplam==s:
    print(number,"is an Armstrong number")
else:
    print(number,"is not an Armstrong number")