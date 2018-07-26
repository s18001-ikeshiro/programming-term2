print("四則計算プログラムです。")
argument1 = input("第1パラメータを入力してください>>>")
argument2 = input("第2パラメータを入力してください>>>")
operator = input("演算方法を入力してください>>>")
while True:
    if operator == "+" or "-" or "*" or "/":
        break
    else:
