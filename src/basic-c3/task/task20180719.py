print("四則計算プログラムです。")
parameters1 = input("第1パラメータを入力してください>>>")
# 書いた後に気づいたのですが多分while使いませんね。
while parameters1.isnumeric():
    if False:
        print("error: 数値以外が入力されました。")
    else:
        break
parameters2 = input("第2パラメータを入力してください>>>")
while parameters2.isnumeric():
    if True:
        break
    elif False:
        print("error: 数値以外が入力されました。")
input("演算方法を入力してください>>>")
