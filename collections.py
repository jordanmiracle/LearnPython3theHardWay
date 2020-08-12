# regular unsorted dict
d = {'banana':3, 'apple': 4, 'pear': 1, 'orange': 2}

# dictionary sorted by key

class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)

class Counter(dict):
    def __missing__(self, key):
        return 0
c = Counter()
c['red']
print(OrderedDict)

