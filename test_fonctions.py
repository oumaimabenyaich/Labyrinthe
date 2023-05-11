import pytest
import fonctions

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
boardR = [{'N': False, 'E': True, 'S': True, 'W': False, 'item': None},
          {'N': False, 'E': True, 'S': True, 'W': False, 'item': None},
          {'N': False, 'E': True, 'S': True, 'W': True, 'item': None}, 
          {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, 
          {'N': False, 'E': True, 'S': True, 'W': True, 'item': 1}, 
          {'N': False, 'E': False, 'S': True, 'W': True, 'item': 15}, 
          {'N': False, 'E': False, 'S': True, 'W': True, 'item': None}, 
          {'N': True, 'E': True, 'S': False, 'W': False, 'item': 12}, 
          {'N': False, 'E': True, 'S': False, 'W': True, 'item': 0}, 
          {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, 
          {'N': False, 'E': True, 'S': False, 'W': True, 'item': None},
          {'N': False, 'E': False, 'S': True, 'W': True, 'item': None},
          {'N': True, 'E': False, 'S': False, 'W': True, 'item': None},
          {'N': True, 'E': False, 'S': False, 'W': True, 'item': None},
          {'N': True, 'E': True, 'S': True, 'W': False, 'item': 2},
          {'N': True, 'E': False, 'S': True, 'W': True, 'item': 19}, 
          {'N': True, 'E': True, 'S': True, 'W': False, 'item': 3},
          {'N': True, 'E': True, 'S': True, 'W': False, 'item': 20},
          {'N': False, 'E': True, 'S': True, 'W': True, 'item': 4},
          {'N': True, 'E': True, 'S': True, 'W': False, 'item': 23},
          {'N': True, 'E': False, 'S': True, 'W': True, 'item': 5},
          {'N': False, 'E': True, 'S': True, 'W': False, 'item': None},
          {'N': False, 'E': True, 'S': False, 'W': True, 'item': None},
          {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, 
          {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, 
          {'N': False, 'E': True, 'S': True, 'W': False, 'item': 14}, 
          {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, 
          {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, 
          {'N': True, 'E': True, 'S': True, 'W': False, 'item': 6}, 
          {'N': True, 'E': False, 'S': True, 'W': False, 'item': None}, 
          {'N': True, 'E': True, 'S': False, 'W': True, 'item': 7}, 
          {'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, 
          {'N': True, 'E': False, 'S': True, 'W': True, 'item': 8}, 
          {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, 
          {'N': True, 'E': False, 'S': True, 'W': True, 'item': 9}, 
          {'N': True, 'E': True, 'S': False, 'W': False, 'item': 13},
          {'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, 
          {'N': True, 'E': True, 'S': False, 'W': True, 'item': 18}, 
          {'N': True, 'E': False, 'S': False, 'W': True, 'item': 17}, 
          {'N': False, 'E': True, 'S': True, 'W': True, 'item': 22}, 
          {'N': False, 'E': True, 'S': True, 'W': False, 'item': None}, 
          {'N': False, 'E': True, 'S': False, 'W': True, 'item': None}, 
          {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, 
          {'N': True, 'E': True, 'S': False, 'W': True, 'item': 21}, 
          {'N': True, 'E': True, 'S': False, 'W': True, 'item': None},
          {'N': True, 'E': True, 'S': False, 'W': False, 'item': None}, 
          {'N': True, 'E': True, 'S': False, 'W': True, 'item': 11}, 
          {'N': False, 'E': True, 'S': True, 'W': False, 'item': 16}, 
          {'N': True, 'E': False, 'S': False, 'W': True, 'item': None}
          ] 
 
tile1 = {"N": False, "E": True, "S": True, "W": False, "item": None}
tile2 = {"N": True, "E": False, "S": True, "W": False, "item": None}
tile3 = {"N": True, "E": True, "S": False, "W": True, "item": None}
tile4 = {"N": False, "E": False, "S": False, "W": True, "item": None}

state1 = {
  "players": ["LUR", "HSL"],
  "current": 0,
  "positions": [6, 47],
  "target": 3,
  "remaining": [4, 4],
  "tile": tile1,
  "board": board1
  }
state2 = {
  "players": ["LUR", "HSL"],
  "current": 0,
  "positions": [40, 47],
  "target": 3,
  "remaining": [4, 4],
  "tile": tile1,
  "board": board1
  }


def test_moveAEnvoyer():
    assert fonctions.moveAEnvoyer(tile1,'A',1) == {"tile": tile1,"gate" : "A","new_position": 1}

def test_jeuDuCoupTest():
    assert fonctions.jeuDuCoupTest(i =0, state = state1) == (tile1, 'A',6)
    assert fonctions.jeuDuCoupTest(i =51, state = state2) == (tile1, 'A',41)

def test_typeTile():
    assert fonctions.typeTile(tile = tile1) == 1
    assert fonctions.typeTile(tile = tile2) == 2
    assert fonctions.typeTile (tile = tile3) ==3
    assert fonctions.typeTile (tile= tile4) == 0

def test_yAQuoiCommePossiblite():
    assert fonctions.yAQuoiCommePossiblite(positionActuelle = 2,parent = 1,board = board1) == [2,1,[9]]

def test_trouverDesChemin():
    assert fonctions.trouverDesChemin(board = board1,positionPion = 0, positionTresor = 16,typeTile = 0, porte = 'A') == [16, [0, 1, 2]]

def test_pionAUnePorte():
    assert fonctions.pionAUnePorte(positionPion=1) == ('A','I')


def test_recreerLaMap():
    assert fonctions.recreerLaMap(board = board1, tile = tile1, porte = "A", positionPion = 43 ) ==(boardR,1)

def test_ouEstLeTresor():
    assert fonctions.ouEstLeTresor(board = board1 , cible = 1) == 4

def test_genererLesPortesAEssayer():
    assert fonctions.genererLesPortesAEssayer(22) == ["A","B","C","D","E","F","G","H","I","J","K","L"]

def test_afficherLePlateau():
    assert fonctions.afficherLePlateau(board = board1, tile = tile1, positionPion = 3) == None

def test_trouverTypeTile():
    assert fonctions.trouverTypeTile([0, 1, 2], {"N": False, "E": True, "S": True, "W": False, "item": 80}) == [{'N': False, 'E': True, 'S': False, 'W': True, 'item': 80}, 2]