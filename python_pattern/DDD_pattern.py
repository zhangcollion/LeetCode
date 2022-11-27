## Controller和VO负责暴露借口
### Controller 调用Service的方法

class VirtualWalletController:
    def __init__(self, virtual_wallet_service):
        self.virtual_wallet_service = virtual_wallet_service

    def get_balance(self, walletid):
        pass

    def debit(self, walletid, amount):
        pass

    def credit(self, walletid, amount):
        pass

    def transfer(self, from_walletid, to_walletid, amount):
        pass



## 充血DDD开发模式
### 把虚拟钱包VirtualWallet类设计成一个充血的Domain领域模型