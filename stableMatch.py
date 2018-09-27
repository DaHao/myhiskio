#!/usr/bin/python3

###############################
# Stable Matching 
# everyone status set to free
# while ( man is free & not yet woman proposed ) do
#         woman = highest ranked in man list & man not yet to proposed
#         if ( woman is free ) then
#                 ( man, woman ) set engaged
#         else if ( woman is engaged but man rank high than current man ) then 
#                 current man set free
#                 ( man, woman ) set engaged
# return result
#
# {
#     "man":
#     {
#         "Victor": [ "Bertha", "Amy", "Diane", "Erika", "Clare" ],
#         "Wyatt": [ "Diane", "Bertha", "Amy", "Clare", "Erika" ],
#         "Xavier": [ "Bertha", "Erika", "Clare", "Diane", "Amy" ],
#         "Yancey": [ "Amy", "Diane", "Clare", "Bertha", "Erika" ],
#         "Zeus": [ "Bertha", "Diane", "Amy", "Erika", "Clare" ]
#     },
#     "woman":
#     {
#         "Amy": [ "Zeus", "Victor", "Wyatt", "Yancey", "Xavier" ],
#         "Bertha": [ "Xavier", "Wyatt", "Yancey", "Victor", "Zeus" ],
#         "Clare": [ "Wyatt", "Xavier", "Yancey", "Zeus", "Victor" ],
#         "Diane": [ "Victor", "Zeus", "Yancey", "Xavier", "Wyatt" ],
#         "Erika": [ "Yancey", "Wyatt", "Zeus", "Xavier", "Victor" ]
#     }
# }

import json
from pprint import pprint
from enum import Enum


class Relationship(Enum):
    free = 1
    engaged = 2
    married = 3

class Human():
    def __init__(self, name, lovelist):
        self.__name = name
        self.__status = Relationship.free
        self.__loverList = lovelist
        self.__lover = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def loverList(self):
        return self.__loverList

    @property
    def lover(self):
        return self.__lover

    @lover.setter
    def lover(self, name):
        self.__lover = name

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

class ChineseCupid():

    def __init__(self, loveData):
        self.manList = []
        for key, value in loveData['man'].items():
            self.manList.append(Human(key, value))

        self.womanList = []
        for key, value in loverData['woman'].items():
            self.womanList.append(Human(key, value))

# everyone status set to free
# while ( man is free & not yet woman proposed ) do
#         woman = highest ranked in man list & man not yet to proposed
#         if ( woman is free ) then
#                 ( man, woman ) set engaged
#         else if ( woman is engaged but man rank high than current man ) then 
#                 current man set free
#                 ( man, woman ) set engaged
# return result

    def findHuman(self, name):
        return next(man for man in self.manList + self.womanList if man.name == name)

    def findBetterHuman(self, man, name1, name2):
        index1 = man.loverList.index(name1)
        index2 = man.lvoerList.index(name2)
        return name1 if index1 < index2 else name2

    def match(self):
        while not all(man.status == Relationship.married for man in self.manList):
            man = next(man for man in self.manList 
                    if man.status == Relationship.free or man.status == Relationship.engaged)

            for womanName in man.loverList: 
                woman = findHuman(womanName)

                if woman.status == Relationship.free:
                    woman.status = Relationship.engaged
                    woman.lover = man.name 
                    man.status = Relationship.engaged
                    man.lover = woman.name
                    break

                else if woman.status == Relationship.engaged 
                        and findBetterHuman(woman, man.name, woman.lover) == man.name:
                    fiance = findHuman(woman.lover)
                    fiance.status = Relationship.free
                    fiance.lover = ""
                    woman.status = Relationship.engaged
                    woman.lover = man.name
                    man.status = Relationship.engaged
                    man.lover = woman.name
                    break

            if all(man.status == Relationship.engaged for man in self.manList):
                for man in self.manList:
                    man.status = Relationship.married

    def showMatch(self):
        for man in self.manList:
            loverName = '' if not man.lover else man.lover.name
            print(man.name, ' lover is ', loverName)

    

if __name__ == '__main__':
    with open('perference.json', 'r') as f:
        data = json.load(f)

    cc = ChineseCupid(data)
    cc.Match()
    cc.showMatch()
