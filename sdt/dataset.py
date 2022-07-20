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

if __name__ == "__main__":
    dataset = Dataset(3)
    for i in range(5):
        dataset.add_source(dummy_datasource(3, 1.0, 10))
    print(dataset)