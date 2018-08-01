try:
    val1 = float(input("分子を入力してください"))
    val2 = float(input("分母を入力してください"))
    result = val1 / val2
    print("結果は{0}です。".format(result))
except:
    print("エラーが発生しました")
finally:
    print("finally句で実行されます")
