# グー、チョキ、パーを変数に入れる
rock = "グー"
paper = "パー"
scissors = "チョキ"
# CPUが必ず勝つように仕向ける
zyanken = input("何を出しますか？1:グー、2:チョキ、3:パー")
if zyanken == str(1):
    print("CPUが", paper, "を出しました。あなたの負けです。")
elif zyanken == str(2):
    print("CPUが", rock, "を出しました。あなたの負けです。")
elif zyanken == str(3):
    print("CPUが", scissors, "を出しました。あなたの負けです。")
else:
    print("入力が不正です。終了します。")
