
import pytest
from sortalgorithms.insertion_sort import sort_array

def describe_given_an_array():
    
    def describe_with_a_single_element():
        
        test_array = [1]
        
        def it_returns_the_element_in_place():
            test_array_copy = test_array.copy()
            sort_array(test_array_copy)
            assert test_array_copy == test_array
            
    def describe_with_two_elements():
        
        def describe_already_sorted():
        
            test_array = [1, 2]
        
            def it_leaves_the_array_as_is():
                test_array_copy = test_array.copy()
                sort_array(test_array_copy)
                assert test_array_copy == test_array
                
        def describe_in_reverse_order():
        
            test_array = [2, 1]
        
            def it_swaps_the_elements():
                test_array_copy = test_array.copy()
                sort_array(test_array_copy)
                assert test_array_copy == [1, 2]
                
                