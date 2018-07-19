# 掛け算を行うだけの関数を定義
def mul(a, b):
    '''
    掛け算を行う

    Parameters
    ------------
    a : int or float
        掛ける数
    b : int or float
        掛けられる数
    Returns
    -------
    mul : int
        掛け算の結果
    '''                 # docstringを設定
    return a * b


# 定義した関数を使う
print(mul(2, 3))
print(mul(10, 3))

help(mul)   # docstringを設定
