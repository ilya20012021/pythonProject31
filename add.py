import pandas as pd
import json
def add():
    s = open("1.txt", "r").readlines()
    v = "".join(s)
    u = v.split()
    f = set(u)
    q = list(f)
    for i in q:
        print(i)
    h = str(input("Введите название файла для работы:"))
    if (h in u):
        df = pd.read_json(f"{h}.json")
        new_row1 = {'id': int(input('Введите индентификатор:')), 'Start': str(input('Пункт отправления:')),
                    'End': str(input('Пункт назначения:')), 'Class': str(input('Введите класс поезда:')), 'Time': int(input('Время отправления:'))}
        df = df.append(new_row1, ignore_index=True)
        k = df.to_json(orient="records")
        kk = json.loads(k)
        kkk = json.dumps(kk, indent=len(kk))
        with open(f"{h}.json", "a+") as f:
            f.write(kkk)

        r = open(f"{h}.json", "r")
        print(*r)

    else:
        print("Такого файла нет!")