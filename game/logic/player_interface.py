

class PlayerInterface:
    def set_health(self, amount: int):
        """"""
        pass

    def get_health(self) -> int:
        """"""
        pass

    def death(self):
        """"""
        pass

    def shoot_gun(self):
        """"""
        pass

    def ads(self, enable: bool):
        """"""
        pass

    def sprint(self, enable: bool):
        """"""
        pass
