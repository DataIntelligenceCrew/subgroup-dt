import random
from dataset import *
from group import *

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
        self.coll = None

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
        self.collected_stats = self.query.empty_copy()
        total_cost = 0.0
        while self.query.is_not_satisfied_by(self.collected_stats):
            selected_source = self.select(policy)
            new_point = selected_source.sample()
            unified_set.append(new_point)
            self.collected_stats.add_point(new_point)
            total_cost += selected_source.cost
        return unified_set, total_cost, self.collected_stats
    
    def select(self, policy):
        if policy == "random":
            return random.choice(self.dataset.data_sources)
        elif policy == "DT-CoupColl":
            return self.select_DT_coupcoll()
        elif policy == "SDT-1-known":
            return self.select_SDT_1_known()
    
    def select_DT_coupcoll(self):
        #group_num = random.randrange(self.num_groups)
        #group = Group(group_num_to_group_tuple(group_num, self.num_groups))
        group = random.choice(list(self.query.stats.keys()))
        def func_DT_coupcoll(data_source):
            return data_source.probability(group) / data_source.cost
        return argmax(self.dataset.data_sources, func_DT_coupcoll)
    
    def select_SDT_1_known(self):
        def cost_of_group(data_source, subgroup):
            if data_source.probability(subgroup) == 0.0:
                return float('inf')
            else:
                return data_source.cost / data_source.probability(subgroup)
        scores = []
        for data_source in self.dataset.data_sources:
            data_source_score = 0.0
            for subgroup in self.query.stats.keys():
                subgroup_score = data_source.probability(subgroup) 
                subgroup_score *= max(0, self.query[subgroup] - self.collected_stats[subgroup])
                costs_of_this_subgroup = [ cost_of_group(data_source, subgroup) for data_source in self.dataset.data_sources ]
                subgroup_score *= min(costs_of_this_subgroup)
                data_source_score += subgroup_score
            data_source_score /= data_source.cost
            scores.append(data_source_score)
        selected_source = argmax2(scores)
        return self.dataset.data_sources[selected_source]

if __name__ == "__main__":
    num_experiments = 100
    policies = [ "random", "DT-CoupColl", "SDT-1-known" ]
    policy_total_costs = { p: 0 for p in policies }
    for i in range(num_experiments):
        if (i % 10 == 0):
            print(str(i))
        # Create a SubgroupDT Object
        tracked_groups = [(True, None), (False, None), (None, True), (None, False), (True, True), (True, False), (False, True), (False, False)]
        tracked_groups = [ Group(g) for g in tracked_groups ]
        dataset = Dataset(2)
        for i in range(5):
            cost = random.uniform(0, 1)
            stat_tracker = StatTracker(2, tracked_groups)
            data_source = DataSource(2, cost, stat_tracker)
            for j in range(13):
                new_point = Group((rand_bool_none(), rand_bool_none()))
                data_source.add_point(new_point)
            dataset.add_source(data_source)
        query = StatTracker(2, tracked_groups)
        query.set_count(Group((True, None)), 50)
        query.set_count(Group((False, None)), 50)
        query.set_count(Group((None, True)), 50)
        query.set_count(Group((None, False)), 50)
        query.set_count(Group((True, True)), 20)
        query.set_count(Group((True, False)), 20)
        query.set_count(Group((False, True)), 20)
        query.set_count(Group((False, False)), 20)
        sdt = SubgroupDT(dataset, 2, query)
        # Run experiment
        for policy in policies:
            unified_set, total_cost, collected_stats = sdt.run(policy)
            # Update results
            policy_total_costs.update({policy : policy_total_costs[policy] + total_cost})
    # Report results
    for policy in policies:
        print(policy, policy_total_costs[policy] / num_experiments)