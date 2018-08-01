print("四則計算プログラムです。")
argu1 = input("第1パラメータを入力してください>>>")
argu2 = input("第2パラメータを入力してください>>>")
while True:
    ope = input("演算方法を入力してください")
    ope_dict = {'+': 0, '-': 1, '*': 2, '/': 3}
    if ope in ope_dict:
        break
    else:
        print("error:再入力してください")
if ope == "+":
    def add(argu1, argu2):
        """
        足し算を行う

        Parameters
        ----------
        argu1 : int
            第一引数
        argu2 : int
            第二引数

        Returns
        -------
        add : int
            足し算の値
        """
        return int(argu1) + int(argu2)
    v = add(argu1, argu2)
    print("結果は", v, "です。")
    help(add)
elif ope == "-":
    def sub(argu1, argu2):
        """
        引き算を行う

        Parameters
        ----------
        argu1 : int
            第一引数
        argu2 : int
            第二引数

        Returns
        -------
        sub : int
            引き算の値
        """
        return int(argu1) - int(argu2)
    v = sub(argu1, argu2)
    print("結果は", v, "です。")
    help(sub)
if ope == "*":
    def mul(argu1, argu2):
        """
        かけ算を行う

        Parameters
        ----------
        argu1 : int
            第一引数
        argu2 : int
            第二引数

        Returns
        -------
        mul : int
            かけ算の値
        """
        return int(argu1) * int(argu2)
    v = mul(argu1, argu2)
    print("結果は", v, "です。")
    help(mul)
if ope == "/":
    def div(argu1, argu2):
        """
        割り算を行う

        Parameters
        ----------
        argu1 : int
            第一引数
        argu2 : int
            第二引数

        Returns
        -------
        div : int
            割り算の値
        """
        return int(argu1) / int(argu2)
    v = div(argu1, argu2)
    print("結果は", v, "です。")
    help(div)
