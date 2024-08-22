
import pytest
from sortalgorithms.insertion_sort import sort_array

def describe_given_an_array():
    
    def describe_with_no_elements():
        
        test_array = [] 
        
        def it_leaves_the_list_empty():
            test_array_copy = test_array.copy()
            sort_array(test_array_copy)
            assert test_array_copy == []
            
    
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
                
    def describe_with_three_elements():
        
        def describe_already_in_order():
            
            test_array = [1, 2, 3]
            
            def it_leaves_the_array_sorted():
                test_array_copy = test_array.copy()
                sort_array(test_array_copy)
                assert test_array_copy == [1, 2, 3]
        
        def describe_in_reverse_order_3_2_1():
            
            test_array = [3, 2, 1]
            
            def it_sorts_the_array():
                test_array_copy = test_array.copy()
                sort_array(test_array_copy)
                assert test_array_copy == [1, 2, 3]
            
        def describe_in_unsorted_order_3_1_2():
            
            test_array = [3, 1, 2]
            
            def it_sorts_the_array():
                test_array_copy = test_array.copy()
                sort_array(test_array_copy)
                assert test_array_copy == [1, 2, 3]
            
    def describe_with_all_elements_the_same():
        
        test_array = [7, 7, 7, 7, 7, 7]
        
        def it_leaves_the_list_the_same():
            test_array_copy = test_array.copy()
            sort_array(test_array_copy)
            assert test_array_copy == test_array
        
    def describe_with_all_negative_integers():
        
        test_array = [-7, -17, -339187, -1, -6, -1992884]
        
        def it_sorts_the_negative_numbers():
            test_array_copy = test_array.copy()
            sort_array(test_array_copy)
            assert test_array_copy == [-1992884, -339187, -17, -7, -6, -1]
        
                
    def describe_with_a_mix_of_positive_and_negative_numbers():
        
        test_array = [-7, 12, -339187, 0, 15, -1992884]
        
        def it_sorts_the_list():
            test_array_copy = test_array.copy()
            sort_array(test_array_copy)
            assert test_array_copy == [-1992884, -339187, -7, 0, 12, 15]
        
                