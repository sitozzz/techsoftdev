
inn = open("p022_names.txt","r")
out = open("sorted_names.txt","w")

spisok_end =[]
spisok_buf = []
string_buf = ' '
counter = 1
summ_of_name = 0
summ_all = 0
name = ''
string_buf = inn.read()
spisok_buf = string_buf.split('"')


for i in spisok_buf:
        if i != ' ' and i != ',':
                spisok_end.append(i+' ' )
#Задаем массив букв для начисления очков
letters = []
for i in range(65,91):
        letters.append(chr(i))
        
spisok_end.sort()
spisok_end.pop(0)
out.writelines(spisok_end)


for i in spisok_end:
#Берем имя как строку
        for j in i:
                name += j
#Делаем из него набор символов
        for k in name:
                if k.isalpha() == True:
                        summ_of_name += ord(k) - 64
                else:
                        summ_of_name *= counter
                        summ_all += summ_of_name
                        summ_of_name = 0
                        counter += 1
                        name = ''
        
        #print("summ = ",summ_all)
        #print("counter = ", counter)
        #input()

print(summ_all)

inn.close()
out.close()
