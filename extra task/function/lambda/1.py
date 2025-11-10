# lambda is anonymous function that used for normal calculation 
# its support multipe argument but support  single expression
# anonymous function means function with no name
# and alao its decalre using lambda keyword


ans=lambda x,y:x+y
print(ans(10,20))# 

# Rules & limitations

# Single expression only (no statements).

# Can’t contain return, pass, assert, yield (yield would make it a generator expression).

# Good for short throwaway functions.

# Readability suffers if complex.

# Typical uses

# Sorting keys

# Passing quick functions to map, filter, higher-order functions

# Small closures