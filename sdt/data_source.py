import random
from group import *
from utils import *
from stat_tracker import *
import warnings

class DataSource:
    def __init__(self, num_groups, cost, stat_tracker):
        """
        @params
            num_groups: number of groups that data points may belong to
            cost: cost of sampling from this data source
            stat_tracker: instance of stat_tracker
        """
        self.data_points = []
        self.num_groups = num_groups
        self.cost = float(cost)
        self.stat_tracker = stat_tracker
    
    def __len__(self):
        return len(self.data_points)
    
    def __getitem__(self, position):
        return self.data_sources[position]
    
    def __str__(self):
        s = "{Cost: " + str(self.cost) + ", Length: " + str(len(self))
        s += ", Points: " + str(self.data_points) + ", Stats: "
        return s + str(self.stat_tracker) + "}"
    
    def __repr__(self):
        return (str(self))
    
    def probability(self, subgroup):
        return self.stat_tracker[subgroup] / len(self)
    
    def add_point(self, data_point):
        if len(data_point) is not self.num_groups:
            warnings.warn("Trying to add a data point with wrong"
                          "number of groups!")
        self.data_points.append(data_point)
        if self.stat_tracker is not None:
            self.stat_tracker.add_point(data_point)
    
    def sample(self):
        return random.choice(self.data_points)

def dummy_datasource(num_groups, cost, num_points):
    ds = DataSource(num_groups, cost, None)
    for i in range(num_points):
        p = DataPoint((rand_bool(), rand_bool(), rand_bool()))
        ds.add_point(p)
    return ds

if __name__ == "__main__":
    ds = dummy_datasource(3, 1.0, 10)
    print(ds)
    st = StatTracker(3, [Group((True, True, True)), Group((True, None, None))])
    ds = DataSource(3, 1.0, st)
    print(ds)