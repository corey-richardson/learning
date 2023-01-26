from dec_to_bin import dec_to_bin
from bin_to_dec import bin_to_dec

def test_dec_to_bin_default_cases():
    assert dec_to_bin(0) == 0
    assert dec_to_bin(1) == 1
    
def test_dec_to_bin():
    assert dec_to_bin(2) == "010"
    assert dec_to_bin(3) == "011"
    assert dec_to_bin(4) == "0111"