from calc import addition 

def test_add_small_numbers():
    assert addition(1, 2) == 3

def test_add_large_numbers():
    assert addition(1000, 2000) == 3000

def test_add_negative_numbers():
    assert addition(-1, -1) == -2   
