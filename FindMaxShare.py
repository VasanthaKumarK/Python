__author__='Vasanth'
__Date__='2014-02-21'

import csv
from collections import OrderedDict, namedtuple


class Share():
        """ This a class which takes csv file as input and find a maximum ///
        vale of company in a given year"""

        def __init__(self,file):
                self.file=file


        def FindMaxShare(self):
                """ Ordereddict which is used to Sort the values ///
                in given dict data structure && namedtuple which is used to create tuple-like object from objects"""

                try:
                        with open(self.file) as input:
                                reader = csv.reader(input)
                                Result = namedtuple('Result', ['Share', 'Year', 'Month'])
                                od = OrderedDict()
                                names = next(reader)[2:]
                                for name in names:
                                        od[name] = Result(0, 'Year', 'Month')
                                for row in reader:
                                        Year, Month = row[:2]
                                        """ zip function used take an two input sequence ///
                                        and return product of the sequnce"""
                                        for name, Share in zip(names, map(int, row[2:])):
                                                if od[name].Share < Share:
                                                        od[name] = Result(Share, Year, Month)
                        print "Excepted Result of the Function"
                        print od.items()

                except IOError as e:
                        print e
                except Exception as e:
                        print e



if __name__=='__main__':
        shar=Share('Company_share.csv')
        shar.FindMaxShare()
