#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for i in tickets:
        # print(i.source, i.destination)
        hash_table_insert(hashtable, str(i.source), str(i.destination))
    #Flight list
    flights = []
    #origin
    dest = hash_table_retrieve(hashtable, 'NONE')
    # Loop till you hit none
    while dest != 'NONE':
        flights.append(dest)
        dest = hash_table_retrieve(hashtable, dest)

    return flights
    