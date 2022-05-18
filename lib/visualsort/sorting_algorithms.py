def bubble_sort(array: list) -> list:
    """
    With every iteration, the largest element bubbles
    towards its correct position. This is a simple and
    straightforward algorithm to implement.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    if not array:
        return array

    n = len(array)
    for i in range(n):
        # Flag that will indicate that the iteration can
        # break early if no changes are needed.
        already_sorted = True

        # For each element in the array (except for the
        # elements that are already sorted), compare it
        # to the adjacent value in the array.
        for j in range(n - i - 1):
            # If the elements need to be swapped, swap them.
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                # The array is not already sorted
                already_sorted = False

        # If no changes were needed in the last iteration,
        # that means that the array is already completed
        # sorted.
        if already_sorted:
            break

    return array

def bubble_sort_step(array: list) -> list:
    """
    This function yields results for each step of bucket sort.
    
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    if not array:
        return [array]

    n = len(array)
    for i in range(n):
        # Flag that will indicate that the iteration can
        # break early if no changes are needed.
        already_sorted = True

        # For each element in the array (except for the
        # elements that are already sorted), compare it
        # to the adjacent value in the array.
        for j in range(n - i - 1):
            # If the elements need to be swapped, swap them.
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                # Return the current state of the array
                yield array[:]

                # The array is not already sorted
                already_sorted = False

        # If no changes were needed in the last iteration,
        # that means that the array is already completed
        # sorted.
        if already_sorted:
            break
    
    # Return the final sorted array
    yield array[:]

def insertion_sort(array: list) -> list:
    """
    Insertion sort takes each element in and finds the correct position
    when comparing it to the other previously sorted elements. This algorithm
    is simple and straightforward to implement.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    n = len(array)
    for i in range (1, n):
        # x is the element that is currently being sorted
        x = array[i]
        j = i - 1
        # Iterate across every other element in the list until x > an element.
        while (j >= 0 and x < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        # When x is found to be greater than an element,
        # add it after that element
        array[j + 1] = x
    
    return array

def insertion_sort_step(array: list) -> list:
    """
    This function yields results for each step of insertion sort.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    n = len(array)
    for i in range (1, n):
        # x is the element that is currently being sorted
        x = array[i]
        j = i - 1
        # Iterate across every other element in the list until x > an element.
        while (j >= 0 and x < array[j]):
            # Return the current state of the array
            yield array[:]
            array[j + 1] = array[j]
            j = j - 1
        # When x is found to be greater than an element,
        # add it after that element
        array[j + 1] = x
    
    # Return the final sorted array
    yield array[:]

def bucket_sort(array: list) -> list:
    """
    Bucket sort is a sorting algorithm that puts elements in buckets and
    sorts the buckets individually before merging them together. This is a 
    scatter-order-gather approach to sorting.
    
    This algorithm works best with data that is uniformly distributed.

    This function supports negative number sorting through sorting negatives
    separately, then merging negatives and positives into the final output.

    Time complexity: O(n+k)
    Space complexity: O(n)
    """
    # If array is empty, return
    if not array:
        return array
    # If array has a length of 1, return because there would be a division
    # by zero later on in the algorithm if there is only one element.
    elif len(array) == 1:
        return array
    
    sorted_array = []
    
    # Separating positive and negative values will allow for proper
    # sorting using bucket sort.
    positive_values = []
    negative_values = []
    for x in array:
        if x >= 0:
            positive_values.append(x)
        else:
            negative_values.append(-1 * x)
    
    array = positive_values

    negative_array = []
    if len(negative_values):
        negative_array = [-x for x in bucket_sort(negative_values)]
        negative_array.reverse()

    if array:
        # Find the max value in the list to help determine how the elements
        # will be separated into buckets.
        max_value = max(array)
        min_value = min(array)
        n = len(array)
        bucket_size = (max_value - min_value) / n

        # Create n empty buckets
        buckets_list = [[] for i in range(n)]
        
        # Put lists of elements into different buckets based on the size
        for i in range(n):
            index = int(array[i] / bucket_size)
            if index < n:
                buckets_list[index].append(array[i])
            else:
                buckets_list[n - 1].append(array[i])
        
        # Sort elements within the buckets
        for i in range(n):
            buckets_list[i] = insertion_sort(buckets_list[i])
        
        # Merge buckets with sorted elements
        for i in range(n):
            sorted_array = sorted_array + buckets_list[i]
    
    # If negative values were calculated, merge them with the
    # positive values that were sorted.
    if negative_array:
        sorted_array = negative_array + sorted_array

    return sorted_array

def bucket_sort_step(array: list) -> list:
    """
    This function yields results for each step of bucket sort.

    Time complexity: O(n+k)
    Space complexity: O(n)
    """
    # If array is empty, return
    if not array:
        return array
    # If array has a length of 1, return because there would be a division
    # by zero later on in the algorithm if there is only one element.
    elif len(array) == 1:
        return array
    
    sorted_array = []
    
    # Separating positive and negative values will allow for proper
    # sorting using bucket sort.
    positive_values = []
    negative_values = []
    for x in array:
        if x >= 0:
            positive_values.append(x)
        else:
            negative_values.append(-1 * x)
    
    array = positive_values

    negative_array = []
    if len(negative_values):
        negative_array = [-x for x in bucket_sort(negative_values)]
        negative_array.reverse()

    if array:
        # Find the max value in the list to help determine how the elements
        # will be separated into buckets.
        max_value = max(array)
        min_value = min(array)
        n = len(array)
        bucket_size = (max_value - min_value) / n

        # Create n empty buckets
        buckets_list = [[] for i in range(n)]
        
        # Put lists of elements into different buckets based on the size
        for i in range(n):
            # Return current state of the array
            current = []
            for x in buckets_list:
                current = current + x
            yield current

            index = int(array[i] / bucket_size)
            if index < n:
                buckets_list[index].append(array[i])
            else:
                buckets_list[n - 1].append(array[i])
        
        # Sort elements within the buckets
        for i in range(n):
            # Return current state of the array
            current = []
            for x in buckets_list:
                current = current + x
            yield current
            # Sort bucket
            # TODO: swaps not being tracked inside insertion_sort
            buckets_list[i] = insertion_sort(buckets_list[i])
        
        # Merge buckets with sorted elements
        for i in range(n):
            # Return the current state of the array
            yield sorted_array[:]
            # Merge next bucket with previously merged buckets
            sorted_array = sorted_array + buckets_list[i]
    
    # If negative values were calculated, merge them with the
    # positive values that were sorted.
    if negative_array:
        sorted_array = negative_array + sorted_array

    # Return the final sorted array
    yield sorted_array[:]