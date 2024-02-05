#importing all the relevant libraries
import math
import matplotlib.pyplot as plt
import random


class CountingBloomFilter():
    """
    Implementing the counting bloom filter which supports:
    - heah_cbf: calculates hash values (indices) for the item
    - search: queries the membership of an element
    - insert: inserts a string to the filter
    - delete: removes a string from the filter
    
    Attributes
    ----------
    fpr: float
        false-positive rate
    num_item: int
        number of items stored
    memory_size: int
        number of counters used 
    num_hashfn: int
        number of hash functions utilized
    primes: list of int
        list of prime numbers used for calculating the indeces
    """
    
    def __init__(self, fpr, num_item):
        """
        Creates class instance storing the most essential information about the data structure. 
    
        Parameters
        ---------------
        fpr: float
            false-positive rate
        num_item: int
            number of items stored
        
        """
        
        self.fpr = fpr
        self.num_item = num_item
        self.memory_size = int(-1* round((self.num_item * math.log2(self.fpr)) / math.log(2)))
        self.counters = [0] * self.memory_size 
        self.num_hashfn = int(round(self.memory_size/self.num_item * math.log(2)))
        #creating a bigger list of primes values and then taking only k of them
        self.primes_list = [131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 
                       181, 191, 193, 197, 199, 211, 223, 227, 229, 233]
        self.primes = self.primes_list[:self.num_hashfn]
    
    
    
    def hash_cbf(self, item):
        """
        Returns hash values of an item.
        
        Parameters
        ----------
        item: string
            a string the hash values for which should be calculated
        
        Returns
        ----------
        list of int
            list of hash values which are the same that indices
        """
        
        indices = []

        
        for prime_num in self.primes: 
            #each iteration corresponds to new hash function
            
            string_hash = 0
            
            for ind in range(len(item)):
                string_hash += (ord(item[ind]) * (prime_num) ** (len(item) - ind - 1))
                
            indices.append(string_hash % self.memory_size)
            
        return indices
    
    
    
    def search(self, item):
        """
        Searches for value in the set.
        
        Parameters
        ----------
        item: string
            a string the hash values for which should be calculated
        
        Returns
        ----------
        bool
            True: the item is possibly in the set; False: the item is not in the set
        """
        
        indices = self.hash_cbf(item)
        
        
        for ind in indices:
            if self.counters[ind] == 0:
                #print("Not in the set!")
                return False
        #print("Possibly in the set!")
        return True
    
        

    
    def insert(self, item):
        """
        Inserts the item in the set.
        
        Parameters
        ----------
        item: string
            a string the hash values for which should be calculated
        
        """
        indices = self.hash_cbf(item)
        
        for ind in indices:
            self.counters[ind] += 1
        
    
    
    def delete(self, item):
        """
        Deletes the item from the set. 
        
        Parameters
        ----------
        item: string
            a string the hash values for which should be calculated
        """
        
        indices = self.hash_cbf(item)
        
        for ind in indices:
            if self.counters[ind]:
                self.counters[ind] -= 1
            else:
                raise KeyError(f"The item {item} was not in the set.")