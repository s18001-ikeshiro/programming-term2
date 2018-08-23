import field_map
from player import Player


# 開始メッセージを表示
print("すごろくゲーム、　Start!!")

p_name = input("プレイヤーの名前を教えてください>>")

hero = Player(p_name)

print("やあ、" + hero.name + "！旅をはじめよう！")

while hero.cur_pos < field_map.goal_pos:
    dice_num = field_map.shake_dice()
    # 出た目の分だけ進む
    hero.go_forward(dice_num)

# 結果を表示 print("ゴールしました。おめでとうございます！")
