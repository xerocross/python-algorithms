
import pytest
from sortalgorithms.insertion_sort import sort_array as insertion_sort
from sortalgorithms.bubble_sort import sort_array as bubble_sort

@pytest.fixture(params=[insertion_sort, 
                        bubble_sort], 
                ids = ["insertion_sort",
                       "bubble_sort"])
def array_sort_function(request):
    return request.param