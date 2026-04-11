class Bank:
    def __init__(self, bank, cash=None, account=None):
        self.bank = bank
        self.cash = cash
        self.account = account
        self.__encryptData = "这是数据\n"
        self.__log = "这是log日志\n"
        self.__working()                        # 允许调用

    def save_money(self):
        pass

    def view_log(self):                         # 提供一个给外部查看的接口
        return self.__log                       # 但不准从外部修改哦~

    def __updata_log(self):
        self.__log += self.__encryptData        # 允许查看或修改

    def __working(self):
        self.__updata_log()                     # 允许调用

# 实例化
China_bank = Bank("China_bank", cash=10000, account=1)

China_bank.save_money()                         # 允许调用
China_bank.account = 2                          # 允许查看或修改
print(China_bank.view_log())                    # 允许调用

China_bank.__updata_log()                       # 不许调用
China_bank.__encryptData = "我要破坏数据"        # 不许查看或修改

