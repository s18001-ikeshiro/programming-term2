items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')

    input_count = input("何個購入されますか？")

    print("購入する{0}の個数は{1}個です".format(item_name, input_count))

    count = int(input_count)

    total_price = items[item_name] * count

    print("支払金額は" + str(total_price) + "円です。")
