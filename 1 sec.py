import csv
with open('game.csv', encoding = 'utf-8') as file:
    reader = csv.reader(file, delimiter='$', quotechar='"')
    answer = list(reader)[1:]
    for GameName, characters, nameError, date in answer:
        if '55' in nameError:
            print(f"У персонажа {characters} в игре {GameName} нашлась ошибка с кодом: {nameError}. Дата фиксации: {date}.")
            nameError = 'Done'
            date = '0000-00-00'
with open('game_new.csv', 'w', encoding='utf-8', newline='') as new_file:
    w = csv.writer(new_file)
    w.writerow(['GameName','characters', 'nameError', 'date'])
    w.writerow(answer)
