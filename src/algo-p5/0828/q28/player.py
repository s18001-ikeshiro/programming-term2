import field_map
import sys
import random
from enemy import Enemy


class Player:
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
        self.cur_pos = 0
        self.hp = 100
        self.max_hp = 100
        self.min_damage = 4
        self.max_damage = 7
        self.freq = 20
        self.plant_nums = 10
        self.exp = 0
        self.level = 1

    def choose_action_in_field(self):
        """
        フィールド中での操作を選択する

        Parameters
        ----------
        なし

        Returns
        -------
        なし
        """
        # 見やすさのために、空白行を表示
        print()

        # 「何をしますか？」を表示
        print("何をしますか？")

        # 「1:サイコロを振る、2:現在の状態を確認する、3:薬草を使う、9:ゲームを終了する>>」を表示し入力待ち
        cmd_num = input("1:サイコロを振る、2:現在の状態を確認する、3:薬草を使う、9:ゲームを終了する>>")

        # cmd_numの値によって条件分岐
        if cmd_num == "1":
            # その場から動く
            self.move()
        elif cmd_num == "2":
            # 状態を表示する
            self.show_status()
        elif cmd_num == "3":
            # 薬草をつかう
            self.use_plants()
        elif cmd_num == "9":
            # ゲームを終了する
            self.quit_game()

    def move(self):
        """
        動く(サイコロを振る行為を含む)

        Parameters
        ----------
        なし

        Returns
        -------
        なし
        """
        # サイコロを振る
        dice_num = field_map.shake_dice()

        # 出た目の数だけ前に進む
        self.go_forward(dice_num)

    def go_forward(self, cells):
        """
        前に進む

        Parameters
        ----------
        cells : int
            進むマス目の数

        Returns
        -------
        なし
        """
        # 引数のマス目だけ進む
        self.cur_pos += cells

        # 現在位置を表示
        print("現在位置は" + str(self.cur_pos) + "です。")

        # 止まったマス目のイベントを取得する
        event_nm = field_map.get_event(self.cur_pos)

        if event_nm == "BattleVsZako":
            zako = Enemy("スラスラ")
            self.battle(zako)
        if event_nm == "GoMoreFofward":
            # 2マスさらに前に進む
            self.go_more_forward(2)
        elif event_nm == "GoBack":
            # 3マス戻る
            self.go_back(3)
        elif event_nm == "GoBackToStart":
            # 振り出しに戻る
            self.go_back_to_start()
        elif event_nm == "HealingLake":
            self.healed_in_lake()
        elif event_nm == "PoisonSwamp":
            self.poisoned_in_swamp()

    def go_more_forward(self, cells):
        """
        出た目の分さらに前に進む

        Parameters
        ----------
        cells : int
            進むマス目の数

        Returns
        -------
        なし
        """
        print("イベント発生！" + str(self.cells) + "マスさらに進みます。")

        # 引数で渡された目の分だけ前に進む
        self.go_forward(self.cells)

    def go_back(self, cells):
        """
        出た目の分後ろに戻る

        Parameters
        ----------
        cells : int
            戻るマス目の数

        Returns
        -------
        なし
        """
        print("イベント発生！" + str(cells) + "マス後ろに戻ります。")

        # 引数で出た目の分だけ前に戻る(引数に-1を掛けることで戻る動作をしている)
        self.go_forward(cells * -1)

    def go_back_to_start(self):
        """
        出た目の分後ろに戻る

        Parameters
        ----------
        なし

        Returns
        -------
        なし
        """

        print("イベント発生！振り出しに戻ってしまいます！")
        # 引数で出た目の分だけ前に戻る(引数に-1を掛けることで戻る動作をしている)
        self.go_forward((self.cur_pos * -1))

    def show_status(self):
        """
        現在の状態を表示する

        Parameters
        ----------
        なし

        Returns
        -------
        なし
        """
        # 状態を表示する
        print("{0}の現在位置は{1}です。HPは{2}です。".format(self.name, self.cur_pos, self.hp))
        print("薬草を" + str(self.plant_nums) + "枚持っています。")

    def battle(self, enemy):
        """
        敵と戦う

        Parameters
        ----------
        enemy : Enemy
            敵のオブジェクト

        Returns
        -------
        なし
        """
        # イベント発生メッセージ
        print("イベント発生！" + enemy.name + "があらわれた！")

        # 敵が倒されるまで戦い続ける
        while enemy.hp > 0:
            print()

            print("どうする？")

            # 「1:攻撃する、3:薬草を使う、9逃げる>>」を表示し、入力待ちにする
            cmd_num = input("1:攻撃する、3:薬草を使う、9:逃げる>>")

            if cmd_num == "1":
                # プレイヤーが敵を攻撃。倒したらループを抜ける
                if self.attack(enemy):
                    break
            elif cmd_num == "3":
                # 薬草を使う
                self.use_plants()
            elif cmd_num == "9":
                # 逃げる
                print(self.name + "は逃げ出した！")
                return

            # 敵がプレイヤーを攻撃。倒されたらゲームオーバー
            if not enemy.attack(self):
                print(self.name + "はしんでしまった！世界は闇に包まれてしまった...")
                sys.exit()

        print(self.name + "は" + enemy.name + "を倒した！")

    def attack(self, enemy):
        """
        敵を攻撃する

        Parameters
        ----------
        enemy : Enemy
            敵のオブジェクト

        Returns
        -------
        bool
            True:敵を倒した、False:敵がまだ生きている
        """
        damage = random.randint(self.min_damage, self.max_damage)

        is_critical = False
        rand_num = random.randint(1, self.freq)
        if rand_num % self.freq == 0:
            is_critical = True

        # 自分のターンのメッセージ表示
        print(self.name + "のこうげき！")

        if True:
            print("かいしんのいちげき！")
            damage = damage * 2
        # 相手にダメージを与える
        enemy.hp -= damage

        if enemy.hp > 0:
            print(enemy.name + "に" + str(damage) + "のダメージを与えた！" + enemy.name + "のHPは" + str(enemy.hp) + "です。")
            return False
        else:
            print(enemy.name + "に" + str(damage) + "のダメージを与えた！" + enemy.name + "のHPは0です。")
            return True

    def use_plants(self):
        """
        薬草を使う

        Parameters
        ----------
        なし

        Returns
        -------
        なし
        """
        if self.plant_nums <= 0:
            print(str(self.name) + "は薬草を持っていない")
            return
        print(str(self.name) + "は薬草を使った！")

        self.hp += 30

        if self.hp > self.max_hp:
            self.hp = self.max_hp

        self.plant_nums -= 1

        print(str(self.name) + "のHPが" + str(self.hp) + "に回復した！")

    def healed_in_lake(self):
        """
        湖でHPを回復される

        Parameters
        ----------
        なし

        Returns
        -------
        なし
        """
        print("イベント発生！癒やしの湖で身を清めます。")

        self.hp = self.max_hp

        print(str(self.name) + "のHPが全回復した！現在のHPは" + str(self.hp) + "です。")

    def poisoned_in_swamp(self):
        """
        沼で毒に冒される

        Parameters
        ----------
        なし

        Returns
        -------
        なし
        """
        print("イベント発生！沼で毒に冒されました。")

        self.hp -= 20

        if self.hp > 0:
            print(str(self.name) + "は20のダメージを受けた！現在のHPは" + str(self.hp) + "です。")
        else:
            print(str(self.name) + "は20のダメージを受けた！" + str(self.name) + "は死んでしまった！世界は闇に包まれてしまった...")
            sys.exit()

    def quit_game(self):
        """
        ゲームを終了する

        Parameters
        ----------
        なし

        Returns
        -------
        なし
        """
        # 終了するかどうかの確認メッセージを表示
        cmd_str = input("ゲームの状態はセーブされません。終了しますか？(y/n)")
        # Yが押されたら終了
        if cmd_str == "y" or cmd_str == "Y":
            sys.exit()


if __name__ == '__main__':
    # プレイヤーのオブジェクトを作成
    kevin = Player("ケビン")

    # 敵のオブジェクトを作成
    enemy = Enemy("スラスラ")

    kevin.battle(enemy)

    kevin.show_status()
