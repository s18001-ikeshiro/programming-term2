# 支払金額を求める
# 値段
biru_v = 200
tumami_v = 100
tori_v = 100
# 割引率
rate = 0.2
# セールの焼き鳥
tori_v2 = 100 * (1 - rate)
# 個数
biru_c = 2
tumami_c = 1
tori_c = 2
# ポイントカード
point = 150
# 計算
sum_v = (biru_v * biru_c) + (tumami_v * tumami_c) + (tori_v2 * tori_c)
payment = sum_v - point
# 結果を表示
print("買い物の合計は(焼き鳥はセール込)", sum_v, "円")
print("ポイントを使うと", payment, "円")
