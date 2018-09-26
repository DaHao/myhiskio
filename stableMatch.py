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
        self.name = name
        self.status = Relationship.free
        self.loverList = lovelist

    def setLover(self, human):
        self.lover = human

class ChineseCupid():

    def __init__(self, loveData):
        self.manList = []
        for key, value in loveData['man'].items():
            self.manList.append(Human(key, value))

    def Match(self):
        pprint(self.manList)

if __name__ == "__main__":

    with open('perference.json', 'r') as f:
        data = json.load(f)

    cc = ChineseCupid(data)
    cc.Match()
