import field_map
import sys


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
        print("")

        print("何をしますか？")

        cmd_num = input("1:サイコロを振る、2:現在の状態を確認する、9:ゲームを終了する>>")

        if cmd_num == "1":
            self.move()
        elif cmd_num == "2":
            self.show_status()
        elif cmd_num == "9":
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
        dice_num = field_map.shake_dice()

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

        event_nm = field_map.get_event(self.cur_pos)

        if event_nm == "GoMoreFofward":
            self.go_more_forward(2)
        elif event_nm == "GoBack":
            self.go_back(3)
        elif event_nm == "GoBackToStart":
            self.go_back_to_start()

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
        print("イベント発生！" + str(self.cells) + "マス後ろに戻ります。")

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
        print("{0}の現在位置は{1}です。".format(self.name, self.cur_pos))

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
        cmd_str = input("ゲームの状態はセーブされません。終了しますか？(y/n)")
        if cmd_str == "y" or cmd_str == "Y":
            sys.exit()

    pass
