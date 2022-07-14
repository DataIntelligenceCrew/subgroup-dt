# subgroup-dt

Source code for "Subgroup Data Tailoring for Intersectionally Fair Data Integration" by Jiwon Chang and Fatemeh Nargesian. 

SDT problem:
 - num_groups
 - dataset
    - data sources
        - data points
            - tuple of booleans of set length (= num_groups)
        - cost (number)
 - query
    - list of tuples of (sub)groups and an integer