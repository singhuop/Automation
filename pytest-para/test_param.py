from fact import fact
from fact import reverse_string
import pytest
'''
This is way you can write library  and test some corner cases about your function.  
'''
@pytest.mark.parametrize("input,output",[(1,1),(0,1),(5,120)])
def test_fact_01(input,output):
    result=fact(input)
    assert result==output

@pytest.mark.parametrize("input,output",[('a','a'),('ab','ba'),('abc','cba'),('test','tset')])
def test_rev_string(input,output):
    result=reverse_string(input)
    assert result==output
