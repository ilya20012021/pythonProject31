import pandas as pd
import json
def upd():
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

        x = len(df["Time"])

        class Creationn:
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

        res = Creationn(x)
        m = res.id()
        a = res.w()
        b = res.ww()
        c = res.www()
        d = res.wwww()

        df1 = pd.DataFrame({"id": m,
                           "Start": a,
                           "End": b,
                           "Class": c,
                           "Time": d})
        with open(f"{h}.json", "a+") as f:
            f.truncate(0)
        k = df1.to_json(orient="records")
        kk = json.loads(k)
        kkk = json.dumps(kk, indent=len(kk))

        with open(f"{h}.json", "a+") as f:
            f.write(kkk)

        r = open(f"{h}.json", "r")
        print(*r)