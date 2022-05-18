from visualsort.animation import animate_sorting
from visualsort.sorting_algorithms import insertion_sort_step
from random import randint

# Initialize random array of integers
array = [randint(1, 100) for i in range(50)]

# Initialize generator function
generator = insertion_sort_step(array)

# Animate sorting from initialized sorting function
animate_sorting(array, generator)