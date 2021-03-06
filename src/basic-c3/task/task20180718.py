# 辞書型のデータ(メインメニューと値段)を変数に代入
main_menus = {
    "DripCoffee": 280, "ColdBrewCoffee": 320,
    "CafeLatte": 330, "SoyLatte": 380,
    "Cappuccino": 330, "CaramelFrappuccino": 470,
    "MacchaCreamFrappuccino": 470
}

# 辞書型のデータ(オブションメニューと値段)を変数に代入
option_menus = {
    "LowFatMilk": 0, "NonFatMilk": 0, "SoyMilk": 50,
    "DeepCoffee": 60, "WhipCream": 70, "CaramelShrup": 60,
    "ChocoSource": 0, "DeCafe": 50
}
while True:
    customer = input("メインメニューを選んでください")
    if customer == "" or customer == "q":
        break
    elif customer in main_menus:
        print(main_menus[customer])
        break
    else:
        print("そのような商品はありません")
