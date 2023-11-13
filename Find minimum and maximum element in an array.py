def getMinMax(a, n):
    # Initialize min and max
    min_element = float('inf')
    max_element = float('-inf')

    # Iterate through the array to find min and max
    for num in a:
        min_element = min(min_element, num)
        max_element = max(max_element, num)

    return min_element, max_element
