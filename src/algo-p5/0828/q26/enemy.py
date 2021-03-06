import random


class Enemy:
    def __init__(self, name):
        """
        コンストラクタ

        Parameters
        ----------
        name : str
            プレイヤーの名前

        Returns
        -------
            自分自身のインスタンス
        """
        self.name = name
        self.hp = 10
        # 相手に与えるダメージの最小値の初期値
        self.min_damage = 2
        # 相手に与えるダメージの最大値の初期値
        self.max_damage = 4
        # 「つうこんのいちげき！」が出る頻度の初期値
        self.freq = 20

    def attack(self, player):
        """
        敵を攻撃する

        Parameters
        ----------
        player : Player
            プレイヤーのオブジェクト

        Returns
        -------
        bool
            True:プレイヤーがまだ生きている、False:プレイヤーが死んでしまった
        """
        damage = random.randint(self.min_damage, self.max_damage)

        is_critical = False

        rand_num = random.randint(1, self.freq)

        if rand_num % self.freq == 0:
            is_critical = True
        # 敵のターンのメッセージ表示
        print(self.name + "のこうげき！")

        if True:
            print("つうこんのいちげき！")
            damage = damage * 2
        # プレイヤーにダメージを与える
        player.hp -= damage

        if player.hp > 0:
            print(player.name + "は" + str(damage) + "のダメージを受けた！" + player.name + "のHPは" + str(player.hp) + "です。")
            return True
        else:
            print(player.name + "は" + str(damage) + "のダメージを受けた！" + player.name + "のHPは0です。")
            return False
