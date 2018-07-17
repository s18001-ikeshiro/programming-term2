import random

# リストに代入
constella = ["おひつじ座", "おうし座", "ふたご座"]
evalua = ["良い", "悪い", "普通"]
luckyitem = ["葉っぱ", "ペットボトル", "タオル"]
luckycolor = ["赤", "青", "黃"]

# ランダムに代入して一つだけ選ぶようにする
i = random.randint(0, len(constella)-1)
j = random.randint(0, len(evalua)-1)
k = random.randint(0, len(luckyitem)-1)
m = random.randint(0, len(luckycolor)-1)

# 文が長いので変数に代入
fmt = """今日の{0}座の運勢は{1}。ラッキーアイテムは{2}。ラッキーカラーは{3}。"""

# 結果を表示
desc = input(fmt.format(constella[i], evalua[j], luckyitem[k], luckycolor[m]))
print(desc)
