import warnings

class StatTracker:
    def __init__(self, num_groups, groups):
        self.num_groups = num_groups
        self.stats = { g : 0 for g in groups }

    def add_point(self, data_point):
        for group in self.stats.keys():
            if data_point.isin(group):
                self.stats[group] += 1
    
    def get_count(self, group):
        if group in self.stats.keys():
            return self.stats[group]
        else:
            return 0
    
    def empty_copy(self):
        return StatTracker(self.num_groups, self.num_groups.keys())
    
    def __str__(self):
        return str(self.stats)
    
    def __repr__(self):
        return str(self)
    
    def is_greater(self, other):
        """
        @returns whether counts for self is greater than other for all subgroups
        """
        for group, count in self.stats.items():
            if count < other[group]:
                return False
            return True