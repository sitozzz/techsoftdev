value1=value2=1
length = ""
i = 2
counter = 2
t = True
while t:
        value_sum = value2 + value1
        value1 = value2
        value2 = value_sum
        length = str(value_sum)
        if len(length) == 1000:
                t = False
        i += 1
        counter += 1
        
print(counter)
