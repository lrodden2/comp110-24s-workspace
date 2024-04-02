"""Functions that implement sorting algorithms."""

__author__ = ""

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    idx1: int = 0
    while idx1 < len(x) - 1:
        idx2: int = idx1 + 1
        while idx2 > 0 and x[idx2] < x[idx2 - 1]:
                temp: int = x[idx1]
                x[idx1] = x[idx2-1]
                x[idx2-1] = temp
                idx2 -= 1
        idx1 += 1

def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    idx1: int = 0
    while idx1 < len(x):
        min_idx: int = idx1
        idx2: int = idx1 + 1
        while idx2 < len(x):
            if x[idx2] < x[min_idx]:
                min_idx = idx2
            idx2 += 1
        temp: int = x[idx1]
        x[idx1] = x[min_idx]    
        x[min_idx] = temp      
        idx1 += 1