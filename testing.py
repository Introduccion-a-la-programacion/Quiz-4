import Quiz4;
import pytest;
   
def test_esPrimo_1():
    assert Quiz4.esPrimo(1) == False
    
def test_esPrimo_2():
    assert Quiz4.esPrimo(5) == True
    
def test_esPrimo_3():
    assert Quiz4.esPrimo(15) == False

########################################

def test_invertirNumero_1():
    assert Quiz4.invertirNumero(51) == 15
    
def test_invertirNumero_2():
    assert Quiz4.invertirNumero(800001) == 100008

########################################

def test_formarMatriz_1():
    assert Quiz4.formarMatriz(2,3) == [[0,1,2], [3,4,5]]

def test_formarMatriz_2():
    assert Quiz4.formarMatriz(3,4) == [[0,1,2,3], [4,5,6,7], [8,9,10,11]]
