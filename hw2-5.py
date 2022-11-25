# Реализуйте алгоритм перемешивания списка. 
# разобрала 3 способа


import random
 

list = [1, 2, 3, 4, 5]
 
print ("Изначальный" + str(list))

list2 = random.sample(list, len(list))
print ("Мешаем sample, но при этом сохраняем оригинал : " +  str(list2)) 


random.shuffle(list)
print ("Просто мешаем shuffle: " +  str(list))


 

for i in range(len(list)):
    j = random.randint(0, len(list)-1)

    element=list.pop(j)

    list.append(element)
print("Shuffled List: ",list)
