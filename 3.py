import csv
def search(sp, first, key):
    last = len(sp) - 1
    while first <= last:
        middle = first + (last - first) // 2
        if sp[middle] == key:
            return middle
        elif sp[middle] < key:
            first = middle + 1
        else:
            last = middle - 1

with open('game.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='$', quotechar='"')
    data = sorted(reader, key=lambda x :x[''])

