def print_hand(hand, name="ゲスト"):
    """
    名前に初期値を入れておく

    Parameters
    ----------
    hand : str
        じゃんけんでの手
    name : str
        誰か

    Returns
    -------
    なし
    """
    print(name + "は" + hand + "を出しました")


print_hand("グー")

help(print_hand)
