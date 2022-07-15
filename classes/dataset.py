import random
from utils import *
from data_source import *

class Dataset:
    def __init__(self, num_groups):
        """
        @params
            num_sources: nu
        """
        self.data_sources = []
        self.num_groups = num_groups
    
    def __len__(self):
        return len(self.data_sources)
    
    def __getitem__(self, position):
        return self.data_sources[position]
    
    def __str__(self):
        s = "Length: " + str(len(self)) + "\n"
        for data_source in self.data_sources:
            s += str(data_source) + "\n"
        return s.rstrip()
    
    def __repr__(self):
        return str(self)

    def add_source(self, data_source):
        self.data_sources.append(data_source)
    
    def argmax(self, function):
        maximizer = None
        max_value = float('-inf')
        for data_source in self.data_sources:
            if maximizer is None or function(data_source) > maximizer:
                maximizer = data_source
                max_value = function(data_source)
        return maximizer
    
    def argmin(self, function):
        def maximizer_function(data_source):
            return -1 * function(data_source)
        return self.argmax(maximizer_function)
    
    def max(self, function):
        max_value = float('-inf')
        for data_source in self.data_sources:
            if function(data_source) > max_value:
                max_value = function(data_source)
        return max_value

    def min(self, function):
        min_value = float('inf')
        for data_source in self.data_sources:
            if function(data_source) < max_value:
                min_value = function(data_source)
        return min_value

    
    def select(self, policy):
        """
        @param

        """
        if policy == "random":
            return random.choice(self.data_sources)
        elif policy == "DT-CoupColl":
            return self.select_DT_coupcoll()
        elif policy == "SDT-1-known":
            return self.select_SDT_1_known()
    
    def select_DT_coupcoll(self):
        group_num = random.randrange(self.num_groups)
        group_tuple = group_num_to_group_tuple(group_num, num_groups)
        def func_DT_coupcoll(data_source):
            return data_source.probability(group) / data_source.cost
        return self.argmax(func_DT_coupcoll)
    
    def select_SDT_1_known(self):
        def cost_of_group(subgroup):
            return self.cost / self.probability(subgroup)
        scores = []
        for data_source in self.data_sources:
            data_source_score = 0.0
            for subgroup in self.stat_tracker.keys():
                subgroup_score = self.probability(subgroup) * Qs
                subgroup_score *= self.min(cost_of_group)
                data_source_score += subgroup_score
            data_source_score /= data_source.cost
            scores.append(data_source_score)
        def 
        return score / dat


if __name__ == "__main__":
    dataset = Dataset(3)
    for i in range(5):
        dataset.add_source(dummy_datasource(3, 1.0, 10))
    print(dataset)