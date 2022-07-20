import warnings
from utils import *

# Represents a group/subgroup as a tuple of booleans
# Uses None for groups that do not matter
# Bottom-level subgroups are synonymous with data points

class Group:
    def __init__(self, group_membership):
        """
        @params
            group_membership: n-tuple of booleans, either True, False, or None
        """
        self.group_membership = group_membership
    
    def __len__(self):
        return len(self.group_membership)
    
    def __getitem__(self, position):
        return self.group_membership[position]

    def contains(self, other):
        if len(self) is not len(other):
            warnings.warn("Groups have different lengths. Defaulting "
                "containment test to False.")
            return False
        for i in range(len(self)):
            if self[i] is not None:
                if other[i] is None:
                    return False
                elif self[i] ^ other[i]:
                    return False
        return True
    
    def isin(self, other):
        return other.contains(self)
    
    def __str__(self):
        """
        @returns a representation of this group as a pattern
        """
        return ''.join(bool_to_str(g) for g in self)
    
    def __repr__(self):
        return (str(self))
    
    def __hash__(self):
        return hash(self.group_membership)
    
    def __eq__(self, other):
        return self.group_membership == other.group_membership

# Alias Group into DataPoint as syntactic sugar
DataPoint = Group

if __name__ == "__main__":
    G1 = Group((True, None, None))
    G2 = Group((None, True, None))
    G3 = Group((None, None, True))
    s12 = Group((True, True, None))
    s12n3 = Group((True, True, False))
    s1234 = Group((True, True, True, True))
    print(G1)
    print(G2)
    print(G3)
    print(s12)
    print(s12n3)
    print(s1234)
    print(s1234.contains(G1))
    print(s12.contains(G1))
    print(G1.contains(s12))
    print(G3.contains(s12))
    print(s12.isin(G2))