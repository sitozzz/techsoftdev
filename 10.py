from math import *
summ = 0

for n in range(1000000,2000000):
        print(n)
        f = True 
        for i in range(2, round(sqrt(n))+1):
                if n % i == 0:
                        f = False
                if f:
                        summ += n
	
print("Сумма простых чисел = ", summ)
