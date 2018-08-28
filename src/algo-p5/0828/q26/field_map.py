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

    # 1~6の任意の数をdice_numに代入
    dice_num = random.randint(1, 6)

    # 出たサイコロの目を表示
    print(str(dice_num) + "の目が出ました。")
    return dice_num


def get_event(target_cell):
    """
    止まったセルのイベントを取得する

    Parameters
    ----------
    target_cell : int
        止まったセル

    Returns
    -------
    str
        イベントの名称
    """
    if target_cell % 5 == 0:
        return "BattleVsZako"

    # if target_cell % 10 == 3:
    elif target_cell % 10 == 3:
        return "GoMoreForward"
    elif target_cell % 20 == 17:
        return "GoBack"
    elif target_cell % 100 == 49:
        return "GoBackToStart"
    else:
        return ""


if __name__ == "__main__":
    print(get_event(1))
    print(get_event(13))
    print(get_event(37))
    print(get_event(49))
