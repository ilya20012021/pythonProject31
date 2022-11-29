import pandas as pd
import json
def create():
    x = int(input("Введите количество записей:"))

    class Creation:
        def __init__(self, x):
            self.x = x

        def id(self):
            y = []
            for i in range(self.x):
                k = int(input('Введите идентификатор:'))
                y.append(k)
            return y

        def w(self):
            a = []
            for i in range(self.x):
                k = str(input('Пункт отправления:'))
                a.append(k)
            return a


        def ww(self):
            b = []
            for i in range(self.x):
                k = str(input('Пункт назначения:'))
                b.append(k)
            return b


        def www(self):
            c = []
            for i in range(self.x):
                k = str(input('Введите класс поезда:'))
                c.append(k)
            return c

        def wwww(self):
            d = []
            for i in range(self.x):
                k = int(input('Время отправления:'))
                d.append(k)
            return d


    res = Creation(x)
    m = res.id()
    a = res.w()
    b = res.ww()
    c = res.www()
    d = res.wwww()

    df = pd.DataFrame({"id":m,
                      "Start":a,
                       "End":b,
                       "Class":c,
                       "Time":d})

    k = df.to_json(orient="records")
    kk = json.loads(k)
    kkk = json.dumps(kk,indent=len(kk))
    name = str(input("Введите название файла:"))
    with open("1.txt", "a+") as f:
        f.write(f'{name}\n')
    with open(f"{name}.json","a+") as f:
        f.write(kkk)

    r = open(f"{name}.json","r")
    print(*r)
