"""
Class intented to represent a specific Signal
a signal could be interpreted as an action over a stock at a specific timestamp.
i.e,
-> NHZUSD 10:00 PUT
-> PJYJPN 22:00 CALL
"""
class Signal:
    # constructor method 
    # remark that by default expiration time is 1
    def __init__(self,money: int,actives: str, expirations = 1):
        self.money = money
        self.actives = actives
        self.expirations = expirations

    # str representation of the signal
    def __str__(self):
        return f"{self.money} {self.actives} {self.expirations}"


