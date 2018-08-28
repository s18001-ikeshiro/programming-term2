import field_map
from player import Player


if __name__ == '__main__':
    # 開始メッセージを表示
    print("すごろくゲーム、　Start!!")

    p_name = input("プレイヤーの名前を教えてください>>")

    hero = Player(p_name)

    print("やあ、" + hero.name + "！旅をはじめよう！")

    while hero.cur_pos < field_map.goal_pos:
        hero.choose_action_in_field()

    # 結果を表示
    print("ゴールしました。おめでとうございます！")
