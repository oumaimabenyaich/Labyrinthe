import pytest
import fonctions

tileH = {"N": False, "E": True, "S": True, "W": False, "item": None}
def test_moveAEnvoyer():
    assert fonctions.moveAEnvoyer(tileH,'A',3) == {"tile": tileH,"gate" : "A","new_position": 3}

board1 = [{"N": False, "E": True, "S": True, "W": False, "item": None}, #0
         {"N": False, "E": True, "S": False, "W": True, "item": 0}, #1
         {"N": False, "E": True, "S": True, "W": True, "item": None}, #2
         {"N": True, "E": False, "S": True, "W": False, "item": None}, #3
         {"N": False, "E": True, "S": True, "W": True, "item": 1}, #4
         {"N": False, "E": False, "S": True, "W": True, "item": 15}, #5
         {"N": False, "E": False, "S": True, "W": True, "item": None}, #6
         {"N": True, "E": True, "S": False, "W": False, "item": 12}, #7
         {"N": True, "E": False, "S": True, "W": True, "item": 19}, #8
         {"N": True, "E": False, "S": True, "W": False, "item": None}, #9 
         {"N": False, "E": True, "S": False, "W": True, "item": None}, #10
         {"N": False, "E": False, "S": True, "W": True, "item": None}, #11
         {"N": True, "E": False, "S": False, "W": True, "item": None}, #12
         {"N": True, "E": False, "S": False, "W": True, "item": None}, #13
         {"N": True, "E": True, "S": True, "W": False, "item": 2}, #14
         {"N": False, "E": True, "S": False, "W": True, "item": None}, #15
         {"N": True, "E": True, "S": True, "W": False, "item": 3}, #16
         {"N": True, "E": True, "S": True, "W": False, "item": 20}, #17
         {"N": False, "E": True, "S": True, "W": True, "item": 4}, #18
         {"N": True, "E": True, "S": True, "W": False, "item": 23}, #19
         {"N": True, "E": False, "S": True, "W": True, "item": 5}, #20
         {"N": False, "E": True, "S": True, "W": False, "item": None}, #21
         {"N": True, "E": False, "S": True, "W": False, "item": None}, #22
         {"N": True, "E": False, "S": True, "W": False, "item": None}, #23
         {"N": True, "E": False, "S": True, "W": False, "item": None}, #24
         {"N": False, "E": True, "S": True, "W": False, "item": 14}, #25
         {"N": True, "E": True, "S": False, "W": False, "item": None}, #26
         {"N": False, "E": True, "S": False, "W": True, "item": None}, #27
         {"N": True, "E": True, "S": True, "W": False, "item": 6}, #28
         {"N": False, "E": True, "S": True, "W": False, "item": None}, #29
         {"N": True, "E": True, "S": False, "W": True, "item": 7}, #30
         {"N": False, "E": True, "S": True, "W": False, "item": None}, #31
         {"N": True, "E": False, "S": True, "W": True, "item": 8}, #32
         {"N": True, "E": True, "S": False, "W": False, "item": None}, #33
         {"N": True, "E": False, "S": True, "W": True, "item": 9}, #34
         {"N": True, "E": True, "S": False, "W": False, "item": 13}, #35
         {"N": True, "E": True, "S": False, "W": True, "item": 21}, #36
         {"N": True, "E": True, "S": False, "W": True, "item": 18}, #37
         {"N": True, "E": False, "S": False, "W": True, "item": 17}, #38
         {"N": False, "E": True, "S": True, "W": True, "item": 22}, #39
         {"N": False, "E": True, "S": True, "W": False, "item": None}, #40
         {"N": False, "E": True, "S": False, "W": True, "item": None}, #41
         {"N": True, "E": True, "S": False, "W": False, "item": None}, #42
         {"N": False, "E": True, "S": False, "W": True, "item": 10}, #43
         {'N': True, 'E': True, 'S': False, 'W': True, 'item': None}, #44
         {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, #45
         {'N': True, 'E': True, 'S': False, 'W': True, 'item': 11}, #46
         {'N': False, 'E': True, 'S': True, 'W': False, 'item': 16},   #47 ######################
         {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}] #48
def test_ouEstLeTresor():
    assert fonctions.ouEstLeTresor(board = board1 , cible = 1) == 4


#def recreerLaMap():
#   assert fonctions.recreerLaMap(board = board1, tile = tileH, porte = "A", positionPion = -1 ) == 





