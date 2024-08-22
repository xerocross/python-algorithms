
import pytest
from sortalgorithms.insertion_sort import sort_array

def describe_given_an_array():
    
    def describe_with_a_single_element():
        
        test_array = [1]
        
        def it_returns_the_element_in_place():
            test_array_copy = test_array.copy()
            sort_array(test_array_copy)
            assert test_array_copy == test_array