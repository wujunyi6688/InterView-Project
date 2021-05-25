import time

class GameBody(object):
    def __init__(self, list_input, thing_name):
        self.data_list = list_input
        self.name = thing_name
        self.data_sum = self.sum()

    def sum(self):
        sums = 0
        for data in self.data_list:
            sums += int(data)
        return sums

    def get_num(self, index):
        return self.data_list[index-1]

    def set_num(self, index, data):
        self.data_list[index-1] = int(data)

    def is_clear(self):
        if self.data_sum <= 0:
            return False
        else:
            return True

    def show_current_status(self):
        i = 1
        print("")
        print("#" * 20)
        for data in self.data_list:
            print("第%d行的%s数目为：%d" %(i, self.name, data))
            i += 1
        print("#" * 20)
        print("")

    @ staticmethod
    def game_rules():
        # 进行游戏规则介绍，询问是否开始游戏
        print("")
        print("#" * 80)
        print("将15根牙签,分成三行,每行自上而下（其实方向不限）分别是3、5、7根安排两个玩家，"
              "每人可以在一轮内，在任意行拿任意根牙签，但不能跨行拿最后一根牙签的人即为输家")
        print("#" * 80)

pass




if __name__ == "__main__":
    #1. 实例化一个设定好的游戏体
    game = GameBody([3, 5, 7], "火柴")
    player_flag = False

    while True:
        time.sleep(1)
        game.game_rules()
        is_start = input("了解规则后，是否开始游戏？y/Y开始，n/N结束:  ")
        if is_start not in ("y", "Y", "n", "N"):
            print("错误提示：输入有误，请输入y/Y开始或者n/N结束")
            continue
        else:
            if is_start in ("n", "N"):
                break
            else:
                # 2. 进入循环判断
                # 判断是否最后一个物品（满足跳出循环）
                while game.is_clear():
                    time.sleep(0.5)
                    # 每一轮转换玩家身份
                    player_name = ""
                    player_flag = not player_flag
                    if player_flag:
                        player_name = "玩家1"
                    else:
                        player_name = "玩家2"

                    # 2.1 展示当前排列
                    game.show_current_status()
                    # 2.2 询问玩家抽取哪一行多少个物品
                    while True:
                        time.sleep(0.5)
                        try:
                            row, getnums = input("请%s输入目标行数和抽取的数目，示例：1 2:  " % player_name).split()
                            row = int(row)
                            getnums = int(getnums)
                        except ValueError:
                            print("错误提示：目标行数和抽取的数目输入有误，请重新输入")
                        else:
                            if game.get_num(row) < getnums:
                                print("错误提示：抽取的数目不能大于第%d行的数目" % row)
                                continue
                            else:
                                break

                    # 2.3 设置新的数据值
                    new_data = int(game.get_num(row)) - getnums
                    game.set_num(row, new_data)
                    game.data_sum = game.data_sum - getnums

                pass
                # 2.4 根据最后一轮抽取最后一个物品判断哪个玩家赢了和输了
                print("本轮游戏结束，%s抽取了最后一根%s, 你输了！！！" % (player_name, game.name))


    print("######## 成功退出游戏 ###########")


