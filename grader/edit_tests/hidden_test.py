from calc import addition 

def test_hidden_add_small_numbers():
    assert addition(3, 4) == 7

def test_hidden_add_large_numbers():
    assert addition(3000, 4000) == 7000

def test_hidden_add_negative_numbers():
    assert addition(-3, -4) == -7   
