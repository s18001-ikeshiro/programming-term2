# グー、チョキ、パーを変数に入れる
rock = "グー"
paper = "パー"
scissors = "チョキ"
# CPUが必ず勝つように仕向ける
zyanken = input("何を出しますか？1:グー、2:チョキ、3:パー")
if zyanken == rock:
    result = paper
elif zyanken == paper:
    result = scissors
elif zyanken == scissors:
    result = rock
else:
    print("入力が不正です。終了します")
print("CPUが", result, "を出しました。あなたの負けです。")
