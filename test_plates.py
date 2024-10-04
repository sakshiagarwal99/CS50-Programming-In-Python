from plates import is_valid

def test_length():
    assert is_valid("") == False
    assert is_valid("A") == False
    assert is_valid("DBJ") == True
    assert is_valid("DBH679") == True
    assert is_valid("BNK9870") == False

def test_alphabets():
    assert is_valid("AA222") == True
    assert is_valid("A9ASD") == False
    assert is_valid("A9ASD") == False
    assert is_valid("BNLK") == True

def test_numeric():
    assert is_valid("SK77J") == False
    assert is_valid("78DFH") == False
    assert is_valid("XW032") == False
    assert is_valid("XW324") == True
    assert is_valid("90324") == False

def test_punctuation():
    assert is_valid("JK,45K") == False
    assert is_valid("JK45K.") == False
    assert is_valid(".EWR90") == False
    assert is_valid(".,!") == False
    assert is_valid("DFR E4") == False

def test_alphanumeric():
    assert is_valid("ABC123") == True
    assert is_valid("ABC 123") == False
    assert is_valid("ABC@123") == False
    assert is_valid("AB#CD") == False
    assert is_valid("AB123!") == False

