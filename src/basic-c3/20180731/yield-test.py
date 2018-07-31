# yieldで値を返す関数を定義
def genlto3():
    yield 1;
    yield 2;
    yield 3;


# イテレータオブジェクトを得る
it = genlto3()
# for構文で繰り返し表示
for i in it:
    print(i)
