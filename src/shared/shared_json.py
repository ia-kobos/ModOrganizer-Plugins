import mobase, os
try:
    from PyQt5.QtCore import QCoreApplication, qInfo
except:
    from PyQt6.QtCore import QCoreApplication, qInfo

class SharedJson():

    def __init__(self, jsonObject=dict):
        self.json = jsonObject
        super().__init__()

    def getJsonProperty(self, key=str):
        try:
            return self.json[str(key)]
        except:
            return ""

    def getJsonArray(self, key=str):
        if not (data := self.getJsonProperty(key)):
            return None
        res = []
        try:
            res.extend(iter(data))
            return res
        except:
            return []

    def getJsonStringArray(self, key=str):
        return [str(path) for path in data] if (data := self.getJsonArray(key)) else []