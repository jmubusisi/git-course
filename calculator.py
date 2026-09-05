import statistics

#-----------------------------------------------------
# Mean Calculations
#-----------------------------------------------------
def mean(values):
    if not values:
        raise ValueError("Cannot calculate mean: atleast one value is required")

    return sum(values)/len(values)

#-------------------------------------------------------
# Max Value
#-------------------------------------------------------

def maximum(values):
    if not values:
        raise ValueError("Values cannot be empty")
    return maximum(values)

#---------------------------------------------------------
# Data Range
#---------------------------------------------------------

def data_range(values):
    if not values:
        raise ValueError("Values cannot be empty")
    return max(values) - min(values)

# -------------------------------------------------
# Standard Deviation Calculation
#--------------------------------------------------

def standard_deviation(values):
    if len(values) < 2:
        raise ValueError("Atleast two values are required")
    return statistics.stdev(values)



