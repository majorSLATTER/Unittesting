from lib import *

def test_tvOnOff():
    tv1 = Television(True, 1, 1, False)
    tv1.tvOnOff()
    assert tv1.on == False
    tv1.tvOnOff()
    assert tv1.on == True

def test_chUpDownGet():
    tv1 = Television(True, 1, 1, False)
    assert tv1.getCh() == 1
    tv1.chUp()
    assert tv1.getCh() == 2
    tv1.chDown()
    assert tv1.getCh() == 1

def test_volUpDownGet():
    tv1 = Television(True, 1, 1, False)
    assert tv1.getVol() == 1
    tv1.volUp()
    assert tv1.getVol() == 2
    tv1.volDown()
    assert tv1.getVol() == 1

def test_mute():
    tv1 = Television(True, 1, 1, False)
    assert tv1.getMuted() == False
    tv1.mute()
    assert tv1.getMuted() == True