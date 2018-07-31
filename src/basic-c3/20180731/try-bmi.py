# BMI判定（例外処理あり版）
# ユーザーから正しい値を得てBMIを計算
while True:
    try:    # breakするまで繰り返す
        # 入力
        weight = float(input("体重(kg)は?"))
        height = float(input("身長(cm)は?"))
        # BMIの計算
        height = height / 100   # mに直す
        bmi = weight / (height * height)
        break;
    except:
        print("入力ミスがあります。再度入力してください。")


# bmiの値から結果を表示
result = ""
if bmi < 18.5:
    result = "痩せ型"
elif bmi < 25:
    result = "標準体重"
