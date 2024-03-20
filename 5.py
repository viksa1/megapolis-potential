import csv
import string
def generate_hash(s):
    alp = string.ascii_letters + string.digits + ':' + '-'
    d = {a: i for i, i in enumerate(alp, 1)}
    p = 65
    m = 10 ** 9 + 9
    hash_value = 0
    p_pow = 1
    for chr in s:
        hash_value = (hash_value + d[chr] * p_pow)%m
        p_pow = (p_pow * p) % m
        return int(hash_value)
game_with_hash = []
with open('game.csv') as file:
    reader = list(csv.DictReader(file, delimiter='$', quotechar='"'))
    for row in reader:
        new_row = generate_hash(row['GameName'] + row['characters'])
        game_with_hash.append(new_row)

with open('game_with_hash.csv', 'w', encoding='utf-8', newline='') as new_file:
    w = csv.DictWriter(new_file, fieldnames=['GameName','characters', 'nameError', 'date'])
    w.writeheader()
    w.writerows(game_with_hash)
