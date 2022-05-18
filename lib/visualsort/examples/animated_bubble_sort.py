from visualsort.animation import animate_sorting
from visualsort.sorting_algorithms import bubble_sort_step
from random import randint

# Initialize random array of integers
array = [randint(1, 1000) for i in range(50)]

# Initialize generator function
generator = bubble_sort_step(array)

# Animate sorting from initialized sorting function
animate_sorting(array, generator)