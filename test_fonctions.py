import pytest
import fonctions


tileH = {"N": False, "E": True, "S": True, "W": False, "item": None}
def test_moveAEnvoyer():
    assert fonctions.moveAEnvoyer(tileH,'A',3) == {"tile": tileH,"gate" : "A","new_position": 3}


# def jeuDuCoupTest():
#     assert fonctions.jeuDuCoupTest(i = 0, state = {"a":"b"}) == 

def typeTile():
    assert fonctions.typeTile(tileH) == 2


# def pionAUnePorte():
#     assert fonctions.pionAUnePorte(  ) == 


# def recreerLaMap():
#     assert fonctions.recreerLaMap(  ) == 


# def ouEstLeTresor():
#     assert fonctions.ouEstLeTresor(  ) == 


# def jeuDuCoup():
#     assert fonctions.jeuDuCoup(  ) ==













