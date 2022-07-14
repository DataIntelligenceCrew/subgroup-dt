import random

# Represents a single instance of the Subgroup DT problem. 
# In other words, implements (D, G, C, Q) as a class. 
# Implements the algorithms via the run() function that runs specified
# algorithm and returns the results. 

class SubgroupDT:
    def __init__(self, dataset, num_groups, query):
        """
        @params 
            dataset: an instance of the Dataset class
            num_groups: number of groups in dataset & query
            query: an instance of the StatTracker class
        """
        # Instance variable assignment
        self.dataset = dataset
        self.num_groups = num_groups
        self.query = query

    def __str__(self):
        return "Query: " + str(self.query) + "\nDataset: " + str(self._dataset)

    def run(self, policy):
        """
        @params
            policy: string denoting policy used to choose data source
                - "random": randomly chooses a data source
                - "DT-CoupColl": copies the original DT problem's CoupColl
                - "DT-MAB": copies the original DT problem's MAB
                - "exact": pre-compute F(Q) values for optimal choices
                - "SDT-1-TL-known": sum(P(s|D)) / C
                - "SDT-2-unknown: sum(P(s|D)) / C * curvature
        @returns
            unified set : a list of data points
            total cost : cost that was needed to collect the unified set
            collected stats : stat tracker for the unified set
        """
        unified_set = [] # Collected data points
        collected_stats = StatTracker(self.num_groups, query.empty_copy())
        total_cost = 0.0
        while not collected_stats.is_greater(query):
            optimal_source = None # todo
            new_point = optimal_source.sample()
            unified_set.append(new_point)
            collected_stats.add_point(new_point)
            total_cost += optimal_source.cost
        return unified_set, total_cost, collected_stats

if __name__ == "__main__":
    pass