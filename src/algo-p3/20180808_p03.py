
def print_hand(hand, name):
    """
    誰がジャンケンで何を出したか

    Parameters
    ----------
    hand : str
        じゃんけんでの手
    name : str
        誰が

    Returns
    -------
    なし
    """
    print(name + "は" + hand + "を出しました")



print_hand("グー", "ななしのたろう")


print_hand("パー", "コンピュータ")

help(print_hand)
