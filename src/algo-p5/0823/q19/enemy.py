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
