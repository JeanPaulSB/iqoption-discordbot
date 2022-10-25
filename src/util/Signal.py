import discord
from datetime import datetime
"""
Class intented to represent a specific Signal
a signal could be interpreted as an operation over a stock at a specific timestamp.
i.e,
-> NHZUSD 10:00 PUT
-> PJYJPN 22:00 CALL
"""

class Signal:
    # constructor method 
    # remark that by default expiration time is 1
    def __init__(self,money: int,actives: str,direction: str, user_id, expirations = 1, timestamp = None):
        self.money = money
        self.actives = actives
        self.expirations = expirations
        self.direction = direction
        self.user_id = user_id
        self.created_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self.scheduled = False
        self.planned_to_exc = 0
        

    def buyNow(self,connection):
        check,id = connection.buy(self.money,self.actives,self.direction,self.expirations)
        self.id = id

        if check:
            return True
        else:
            return False
    
    def getPlannedExecution(self):
        timestamp = self.planned_to_exc.split(":")

        hour = timestamp[0]
        minutes = timestamp[1]
        return (hour,minutes)
    # str representation of the signal
    def __str__(self):
        return f"{self.money}  {self.actives} {self.direction} {self.expirations} {self.created_at} "


