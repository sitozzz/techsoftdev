import math

n = 11

result = 0
while n < 10000000000000000000000000000000:
    
    b = list(str(n))
    #print(b)

    c = [int(x) for x in b]

    suma = 0
    for i in range(len(c)):
        
        k = b.pop()
        fac = math.factorial(int(k))
        suma += fac
        i += 1
        
    if suma == n:
        print( n,": одно из чисел")
        result += n
        print ('Ответ: ', result)
    
   
    n += 1
