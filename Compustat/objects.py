import datetime
import math
from errors import throwError

class element:
    def __init__(self, raw_data):
        self.raw = raw_data
        self.clean = dict()
        self.name = raw_data['coname']
        self.date = datetime.datetime.strptime(raw_data['rdqe'], "%m/%d/%Y").date()
        self.quarter = quarterDate(int(raw_data['year']), int(raw_data['qtr']))
    def toString(self):
        return self.name + " " + self.getDateStr()
    def getDateStr(self):
        return self.date.isoformat()
    def getQrtrStr(self):
        return self.quarter.toString()
    def getX(self, field):
        x = self.raw[field]
        try:
            return float(x)
        except (ValueError, TypeError) as e:
            throwError(e, self.name, self.getQrtrStr(), field, "")
            return 0

class security:
    def __init__(self, name):
        self.name = name
        self.elements = dict()

class quarterDate:
    def __init__(self, year, quarter):
        self.year = year
        self.quarter = quarter
    def iterate(self, n):
        y = self.year + math.floor((self.quarter + n - 1) / 4)
        q = (self.quarter + n - 1) % 4 + 1
        return quarterDate(y,q)
    def toString(self):
        return str(self.year) + "-" + str(self.quarter)
    
