#Пользователь вводит количество элементов будущего списка
n=int(input("Введите количество элементов списка:"))
list=[] # инициализация списка
for i in range(n): # цикл по работе с элементамии списка
    # После этого по очереди по одной вводит любые цифры
    # Сохранить цифры в список
    print("Введите ", i+1," элемент:", end='')
    list.append(int(input()))
#Отсортировать список по возрастанию и вывести на экран
list.sort()
print("Отсортированный список:", list)




