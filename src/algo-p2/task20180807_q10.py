items = {"apple": 100, "banana": 200, "orange": 400}


for name in items.keys():
        print("---------------------------------------------")
        price = items[name]
        s = "{0}は1個{1}円です".format(name, price)
        print(s)
