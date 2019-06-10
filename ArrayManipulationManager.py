#Manager
import numpy as np
import random
import string

cache_same, cache_shared, cache_iqr = {}, {}, {}

def getRandomStringArray():
    return [''.join(random.choices(string.ascii_letters + string.digits, k=random.randrange(1, 6))) for r in range(6)]

def removeSharedIntegers(array_a, array_b):
    matching_integers = []
    hkey = create_hashkey(str(array_a+array_b))
    cached_bool = contained_in_cache(hkey, cache_same)
    if cached_bool:
        return cache_same[hkey]
    else:
        pass

    if set(array_a) == set(array_b):
        return []
    
    for i in array_a:
        if i not in set(array_b):
            matching_integers.append(i)

    cache_same[hkey] = matching_integers
    return matching_integers

def getSharedString(array_a, array_b):
    matching_strings = []
    hkey = create_hashkey(str(array_a+array_b))
    cached_bool = contained_in_cache(hkey, cache_shared)
    if cached_bool:
        return cache_shared[hkey]
    else:
        pass
    if set(array_a) == set(array_b):
        return array_a
    else:
        pass

    for i in array_a:
        if i in array_b:
            matching_strings.append(i)

    cache_shared[hkey] = list(set(matching_strings))
    return matching_strings

def Iqr(array_a):
    hkey = create_hashkey(str(array_a))
    cached_bool = contained_in_cache(hkey, cache_iqr)
    if cached_bool:
        return cache_iqr[hkey]
    else:
        pass
    q1 = np.percentile(sorted(array_a), 25, interpolation='lower')
    median = np.percentile(sorted(array_a), 50)
    q3 = np.percentile(sorted(array_a), 75, interpolation='higher')
    IQR = {
        "Q1" : q1.item(),
        "median" : median.item(),
        "Q3" : q3.item()
    }
    cache_iqr[hkey] = IQR
    return IQR

def contained_in_cache(hash_key, cache_type):
    #check if in cache
    if hash_key in cache_type:
        return True
    else:
        return False
    
def create_hashkey(data_string):
    #compute hash key
    hash_key = hash(data_string)
    return hash_key

def clear_cache():
    cache_iqr.clear()
    cache_same.clear()
    cache_shared.clear()
    if cache_iqr == {} and cache_same == {} and cache_shared == {}:
        return True
    else:
        return False
