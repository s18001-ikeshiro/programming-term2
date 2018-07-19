# 再起関数を定義
def say_hello(i):
    """
    ハローと10回表示されるか

    Parameters
    ----------
    i : int
        回数

    Returns
    -------
    なし
    """
    if i <= 0:
        return
    print("ハロー", i)
    say_hello(i-1)


# 実行
say_hello(10)
