# 素数を返すイテレータ
def genPrime(maxnum):
    num = 2
    while(num <= maxnum):
        is_prime = True     # 素数かどうかを管理する変数を定義
        for i in range(2, num):     # 　numが2のときは範囲に含まれる値がなく実行されない
            if(num % i) == 0:       # 素数ではない
                is_prime = False
                break
        if(is_prime):
            yield num
        num += 1


# イテレータを得る
it = genPrime(50)


# 画面に出力
for i in it:
    print(i, end=",")
