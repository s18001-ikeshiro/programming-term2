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
    global cur_pos

    cur_pos = 0

    # 引数のマス目だけ進む
    cur_pos += cells


# サイコロで出た目をdice_numに代入
dice_num = 1

# 出たサイコロの目を表示
print(str(dice_num) + "の目が出ました。")
# 出た目の分だけ進む
go_forward(dice_num)


# 現在位置を表示
print("現在位置は" + str(cur_pos) + "です。")
