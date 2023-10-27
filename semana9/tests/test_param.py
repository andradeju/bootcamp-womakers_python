'''def test_string_is_digit():
  items = ['Bola','1', '10', '33','Bacon']
  for item in items:
    assert item.isdigit()'''

#usando parametrização    
'''import pytest

@pytest.mark.parametrize("item", ['0','1', '10', '33','9'])
def test_string_is_digit(item):
  assert item.isdigit()'''

import pytest 

@pytest.mark.parametrize("item, attribute", [("", "format"), (list(), "append")])
def test_attributes(item, attribute):
  assert hasattr(item, attribute)
