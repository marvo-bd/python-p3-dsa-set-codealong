class MySet:
    def __init__(self, initial_list=None):
        '''Initialize the set with a list.'''
        self.dictionary = {}
        if initial_list:
            for item in initial_list:
                self.dictionary[item] = True

    def add(self, item):
        '''Add an item to the set.'''
        self.dictionary[item] = True

    def delete(self, item):
        '''Remove an item from the set.'''
        if item in self.dictionary:
            del self.dictionary[item]

    def has(self, item):
        '''Check if the set contains an item.'''
        return item in self.dictionary

    def size(self):
        '''Return the number of items in the set.'''
        return len(self.dictionary)

    def clear(self):
        '''Clear all items from the set.'''
        self.dictionary.clear()

    def __str__(self):
        '''Return a string representation of the set.'''
        return 'MySet: {' + ','.join(map(str, self.dictionary.keys())) + '}'
