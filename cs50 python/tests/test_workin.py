from working import convert
import pytest
def test_input():
    with pytest.raises(ValueError):
        convert("9 AM to 17 PM") 
    with pytest.raises(ValueError):
        convert("113:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("11:60 AM to 5:60 PM")
def test_output():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("1:30 PM to 5:00 PM") == "13:30 to 17:00"

def test_working():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

