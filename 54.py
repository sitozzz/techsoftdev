
def RoyalFlash(x):
        if (x[1:10:2] == 'CCCC' or 'SSSS' or 'HHHH' or 'DDDD') and x[0:9:2] == 'TJQKA':
                return True
def StreatFlash(x):
        if (x[1:10:2] == 'CCCC' or 'SSSS' or 'HHHH' or 'DDDD') and (x[0:9:2] == '23456' or '34567' or '45678' or '56789' or '6789T' or '789TJ' or '89TJQ' or '9TJQK'):        
                return True
def Care(x):
        if x[0:9:2] == '2222' or '3333' or '4444' or '5555' or '6666' or '7777' or '8888' or '9999' or 'TTTT' or 'JJJJ' or 'QQQQ' or 'KKKK' or 'AAAA':
                return True
def FullHouse(x):
        
        
file = open("p054_poker.txt","r")

pl1 = []
pl2 = []
str0 = ''
str1 = ''
str2 = ''
sp = []
score = 0


str0 = file.read()
str0
sp = str0.split('" "')

for i in sp:
        for j in i:
                if (j.isalpha() == True or j.isdigit() == True ) and len(str1) != 10:
                        str1 += j
                     
                        count += 1
                if (j.isalpha() == True or j.isdigit() == True) and (len(str1) == 10 and len(str2) != 10):
                        str2 += j
                        if str2[0] == str1[9]:
                                str2 =''
                       
                # Начинаем сравнивать руки игроков
                if len(str1) == 10 and len(str2) == 10:
                        if RoyalFlash(str1) == True:
                       
                                print("Royal Flash")
                                score += 1
                        #if 
                        str1 = ''
                        str2 = ''
                
                                               



        
        
        
print(str1)
print(str2)
