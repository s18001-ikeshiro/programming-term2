import random

# 定数定義部
goal_pos = 100


# 関数定義部
def shake_dice():
    """
    サイコロを降る

    Parameters
    ----------
    なし

    Returns
    -------
    int
        サイコロを振って出た目
    """
    input("サイコロを振ります。Enterキーを押してください。")

    # サイコロで出た目をdice_numに代入
    dice_num = random.randint(1, 6)

    # 出たサイコロの目を表示
    print(str(dice_num) + "の目が出ました。")
    return dice_num
