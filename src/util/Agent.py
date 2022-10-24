from iqoptionapi.stable_api import IQ_Option
from datetime import datetime

"""
Class intended to represent an user agent with properties that the default discord model
doesn't have
"""

# temporal credentials for testing
# cejimah732@ekbasia.com
# tomyandres12
class Agent:
    def __init__(self,user,password):
        self.user = user
        self.password = password
        self.logged = False
        self.scheduled_signals = []
        self.type = "PRACTICE"
        self.balance = 0
        self.looping = False # this means wheter it is checking for scheduled signals
        self.api_username = ''
        self.api_password = ''
        self.api_logged = False

    def setUser(self,user):
        self.user = user
    def setPassword(self,password):
        self.password = password

    def setPracticeMode(self):
        self.type = "PRACTICE"
        self.connection.change_balance(self.type)
    def setRealMode(self):
        self.type = "REAL"
        self.connection.change_balance(self.type)
    def checkMode(self) -> str:
        return self.type

    def getBalance(self) -> float:
        self.balance = self.connection.get_balance()
        return self.balance

    # getting first five positions and sorting them by the corresponding timestamps
    def getClosedPositions(self)-> dict:
        response = self.connection.get_optioninfo(100)['msg']['result']['closed_options'][:5]
        sorted_list = sorted(response, key = lambda d: d['created'], reverse = True)
        return sorted_list

    def getOpenPositions(self) -> dict:
        response = self.connection.get_optioninfo(100)['msg']['result']['open_options']
        return response

    def scheduleSignal(self, signal):
        self.scheduled_signals.append(signal)
    def getScheduledSignals(self) -> list or bool:
        signals = self.scheduled_signals if len(self.scheduled_signals) > 0 else False
        return signals
        


    # connecting with the API
    def connect(self) -> bool:
        connection = IQ_Option(self.user,self.password)
        result = connection.connect()
        if result[0]:
            self.logged = True
            self.connection = connection
            return True
        else:
            return False

