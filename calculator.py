def mean(values):
    if not values:
        raise ValueError("Values cannot be empty")
    
    return sum(values)/len(values)

def min(values):
    if not values:
        raise ValueError("Values cannot be empty")
    return min(values)
