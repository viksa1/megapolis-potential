import csv
with open('game.csv', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='$', quotechar='"')



