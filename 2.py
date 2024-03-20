import csv

def fast_sort(sp):
    if len(sp) > 1:
        pivot = sp.pop()
        g_lst, eq_lst, sm_lst = [], [pivot], []
        for i in sp:
            if i == pivot:
                eq_lst.append(i)
            elif i > pivot:
                g_lst.append(i)
            else:
                sm_lst.append(i)
        return (fast_sort(sm_lst) + eq_lst + fast_sort(g_lst))
    else:
        return sp
with open('game.csv') as file:
    reader = csv.reader(file, delimiter='$', quotechar='"')





with open('game.csv', encoding = 'utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='$', quotechar='"'))
    fast_sort(reader)
    cnt = 1
    for el in reader:

