"""Functions that implement sorting algorithms."""

__author__ = "730475919"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm; insert into an already sorted list."""
    # Step 1: Create an index variable to track the sorted indices in the list.
    sorted_index = 0
    
    # Step 2: Set up an overarching loop to iterate through the list excluding the final element.
    while sorted_index < len(x) - 1:
        
        # Step 3: Create another index variable to track the unsorted indices in the list.
        unsorted_index = sorted_index + 1
        
        # Step 4: Compare the current element to all elements in the sorted part of the list and make swaps as you go.
        while unsorted_index > 0 and x[unsorted_index] < x[unsorted_index - 1]:
            # Step 4.1: Check if the current element is less than the one directly before it.
            # Step 4.2: Swap the two elements.
            x[unsorted_index], x[unsorted_index - 1] = x[unsorted_index - 1], x[unsorted_index]
            # Step 4.3: Decrement the unsorted index variable.
            unsorted_index -= 1
        
        # Step 5: Increment the sorted index variable.
        sorted_index += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm; repeatedly find the minimum and swap it."""
    # Step 1: Create a counter variable to track the indices of the list.
    counter = 0
    
    # Step 2: Set up an overarching loop to iterate through the list.
    while counter < len(x):
        
        # Step 3: Find the index of the minimum element only from the unsorted portion of the list.
        min_index = counter
        
        # Step 3.1: Find the index of the minimum element without using min() function.
        for i in range(counter + 1, len(x)):
            if x[i] < x[min_index]:
                min_index = i
                
        # Step 4: Compare the minimum element to the current element, swap if necessary.
        if min_index != counter:
            # Step 5.1: Swap the minimum element with the current element.
            temp = x[min_index]
            x[min_index] = x[counter]
            x[counter] = temp
        
        # Step 6: Increment the counter.
        counter += 1
    return None