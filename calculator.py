def mean(values):
    if not values:
        raise ValueError("Values cannot be empty")
    
    return sum(values)/len(values)

def maximum(values):
    if not values:
        raise ValueError("Values cannot be empty")
    return maximum(values)

def data_range(values):
    if not values:
        raise ValueError("Values cannot be empty")
    return max(values) - min(values)