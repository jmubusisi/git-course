import statistics

def mean(values):
    if not values:
        raise ValueError("Cannot calculate mean of empty dataset")
    
    return sum(values)/len(values)

def maximum(values):
    if not values:
        raise ValueError("Values cannot be empty")
    return maximum(values)

def data_range(values):
    if not values:
        raise ValueError("Values cannot be empty")
    return max(values) - min(values)

# ------------------------------------------#
#Create Standard Deviation Calculation
#--------------------------------------------#

def standard_deviation(values):
    if len(values) < 2:
        raise ValueError("Atleast two values are required")
    return statistics.stdev(values)



