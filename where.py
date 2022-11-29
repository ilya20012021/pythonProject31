import pandas as pd
import json
def condition():
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
        ti = int(input("Введите час:"))
        df1 = df[df["Time"] >= ti]
        k = df1.to_json(orient="records")
        kk = json.loads(k)
        kkk = json.dumps(kk, indent=len(kk))
        name = str(input("Введите название файла:"))
        with open("1.txt", "a+") as f:
            f.write(f'{name}\n')
        with open(f"{name}.json", "a+") as f:
            f.write(kkk)

        r = open(f"{name}.json", "r")
        print(*r)

    else:
        print("Такого файла нет!")