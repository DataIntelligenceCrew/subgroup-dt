import warnings

class StatTracker:
    def __init__(self, num_groups, groups):
        self.num_groups = num_groups
        self.stats = { g : 0 for g in groups }

    def add_point(self, data_point):
        for group in self.stats.keys():
            if data_point.isin(group):
                self.stats.update({group : self.stats[group] + 1})
    
    def get_count(self, group):
        if group in self.stats.keys():
            return self.stats[group]
        else:
            return 0
        
    def set_count(self, group, count):
        self.stats.update({group : count})
    
    def empty_copy(self):
        return StatTracker(self.num_groups, self.stats.keys())

    def __getitem__(self, item):
        return self.stats[item]

    def __str__(self):
        return str(self.stats)
    
    def __repr__(self):
        return str(self)
    
    def is_not_satisfied_by(self, other):
        """
        @returns whether self, interpreted as a query, is satisfied by other
        """
        for group, count in self.stats.items():
            if count > other[group]:
                return True
        return False