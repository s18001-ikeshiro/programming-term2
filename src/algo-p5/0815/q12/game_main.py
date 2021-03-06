import field_map


# 変数定義部
cur_pos = 0     # 現在の位置


# 関数定義部
def go_forward(cells):
    """
    前に進む

    Parameters
    ----------
    cells : int
        進むマス目の数

    Returns
    -------
    なし
    """
    # 現在位置をグローバル参照する
    global cur_pos

    # 引数のマス目だけ進む
    cur_pos += cells

    # 現在位置を表示
    print("現在位置は" + str(cur_pos) + "です。")

    event_nm = field_map.get_event(cur_pos)
    print(event_nm)


# 開始メッセージを表示
print("すごろくゲーム、　Start!!")

while cur_pos < field_map.goal_pos:
    dice_num = field_map.shake_dice()
    # 出た目の分だけ進む
    go_forward(dice_num)

# 結果を表示
print("ゴールしました。おめでとうございます！")
