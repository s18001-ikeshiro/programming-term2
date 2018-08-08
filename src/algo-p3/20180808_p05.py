def print_hand(hand, name="ゲスト"):
    """
    nameを入力してもらい反映する

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


print("じゃんけんを始めます")

player_name = input("名前を入力してください")


print_hand(player_name)

if player_name == "":
    print_hand("グー")
else:
    print_hand("グー", player_name)

help(print_hand)
