#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    print("weights:", weights)
    # print("limit:", limit)
    # check if pair exist while looping
    for i,w in enumerate(weights):
        # Retrive using the key of value pair
        print("i:", i)
        print("w", w)
        if hash_table_retrieve(ht, w) != None:
            #if exists return key value pair
            f = hash_table_retrieve(ht, w)
            #Return with higher value index if the zeroth index
            # print(f, i)
            if f > i:
                return (f, i)
            else:
                return(i, f)
        #Insert into hash table
        hash_table_insert(ht, limit - w, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
