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
    # サイコロで出た目をdice_numに代入
    cells = 1

    # 出たサイコロの目を表示
    print(str(cells) + "の目が出ました。")

    cur_pos = 0
    cur_pos += cells

    go_forward(cells)


# 現在位置を表示
print("現在位置は" + str(cur_pos) + "です。")
