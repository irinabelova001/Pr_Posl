print('Исходный список:')
lst_is=list(map(int, input().split(','))) # формирование списка при вводе элементов через запятую
lst_preob=list(set(lst_is)) # преобразование списка во множество для исключения повторяющихся элементов и обратно в список
print('Преобразованный список:')
for i in range(len(lst_preob)): # вывод списка поэлементно
    if i!=0 and i!=len(lst_preob):
        print(',',lst_preob[i],end='') # вывод элементов преобразованного списка
    else:
        print(lst_preob[i],end='')
# Дополнительно
ch=input('Введите разделитель списка:')
print('Исходный список:')
lst_is=list(map(int, input().split(ch))) # формирование списка при вводе элементов через указанный разделитель
lst_preob=list(set(lst_is)) # преобразование списка во множество для исключения повторяющихся элементов и обратно в список
print('Преобразованный список:')
for i in range(len(lst_preob)): # вывод списка поэлементно
    if i!=0 and i!=len(lst_preob):
        print(ch,lst_preob[i],end='') # вывод элементов преобразованного списка
    else:
        print(lst_preob[i],end='')