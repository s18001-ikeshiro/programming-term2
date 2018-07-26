# 関数の外側でvalueに100を代入
value = 100


def changeValue():
    """
    変数valueの値を変更

    Parameters
    ----------
    なし

    Returns
    -------
    なし
    """
    # 関数の内側でvalueを変更
    value = 20


changeValue()
print("value=", value)
