import numpy as np
import copy


def list_to_tuple(x:list, directed):
    input_tuples = []
    if directed:
        input_tuples = [(x[i], x[i + 1], float(x[i + 2])) for i in range(0, len(x), 3)]
    else:
        for i in range(0, len(x), 3):
            input_tuples+=[(x[i], x[i + 1], float(x[i + 2]))]
            input_tuples+=[(x[i+1], x[i], float(x[i + 2]))]
    return input_tuples



# list of all nodes
# sort if possible for user's convenience (not possible if entries are a mix of numbers and letters)
def nodes_list(x):
    a = set()
    for i in x:
        fr, to, co = i
        a.add(fr)
        a.add(to)
    try:
        a = sorted(list(a))
    except TypeError:
        a = list(a)
    return a


# input x: list of tuples [(from, to, cost),...]
# output: all iterations, a list of lists of lists of lists (4 dim)
# unknown number of iterations of n tables, each n by n
def DV(x):

    # input x: list of tuples [(from, to, cost),...]
    # output: dict of all nodes and their neighbours+costs as dictionary but replacing all names with indexing
    # {node: {neigh:cost, neigh:cost ...}, ..}
    def nodes_info(x: list):
        all_nodes = {}
        L = nodes_list(x)
        for node in range(len(L)):  # to preserve order in nodes_list(x)
            all_nodes[node] = {}
        for i in x:
            fr, to, co = i
            all_nodes[L.index(fr)][L.index(to)] = co

        return all_nodes
    # instead of {'x': {'y': 2, 'z': 7}, 'y': {'x': 2, 'z': 1}, 'z': {'x': 7, 'y': 1}}
    # output is {0: {1: 2, 2: 7}, 1: {0: 2, 2: 1}, 2: {0: 7, 1: 1}}


    N = nodes_info(x)
    n=len(N)


    def initial():
        A = {}
        for node in range(n):
            A[node] = {}
            for dest in range(n):
                if node == dest:
                    A[node][dest] = 0
                else:
                    A[node][dest] = N[node].get(dest, np.inf)
        # A={0: {0: 0, 1: 2, 2: 7}, 1: {0: 2, 1: 0, 2: 1}, 2: {0: 7, 1: 1, 2: 0}}  for example

        B = []
        for i in range(n):
            init = [[np.inf] * n] * n
            for j in range(n):
                if i == j:
                    init[i] = list(A[i].values())
            B += [init]
        return B  # return list of lists of lists (easier to handle in html)

    # [[0, 2, 7], [inf, inf, inf], [inf, inf, inf]]
    # [[inf, inf, inf], [2, 0, 1], [inf, inf, inf]]
    # [[inf, inf, inf], [inf, inf, inf], [7, 1, 0]] for example

    # input: n tables (current iteration)
    # output: n tables once information has been sent to neighbouring nodes
    def send(tables):
        old_tables = copy.deepcopy(tables)          # won't change if 'tables' is edited
        for i in range(n):                          # for each old table
            for j in N[i].keys():                   # for each neighbour of each old table
                tables[j][i] = old_tables[i][i]     # update with new info
        return tables

    # input: n tables with new information
    # output: n tables once DV algorithm has been applied
    def update(tables):
        for i in range(n):                          # for each node/table i
            a = [0] * n                             # initialise new DV
            for j in range(n):                      # for each element j of the node's distance vector
                if j != i:                          # update all elements in DV other than D_i(i)=0
                    S = []
                    for v in N[i].keys():                   # for each neighbour of node i
                        S += [N[i][v] + tables[i][v][j]]    # c(i,v)+D_v(j) for each neighbour v
                    a[j] = min(S)                           # apply algorithm to define new DV
            tables[i][i] = a                                # replace DV in table
        return tables


    a=initial()
    S=[copy.deepcopy(a)]
    while True:
        b=send(a)
        S+=[copy.deepcopy(b)]
        a=update(b)
        S+=[copy.deepcopy(a)]
        if S[-1]==S[-2]:
            break
    return S


#uncomment the following to test DV() function

#x=[('z','y',1),('x','y',2),('x','z',7),('y','x',2),('y','z',1),('z','x',7)]
#x=[('w','z',5), ('z','w',5),('y','z',6),('z','y',6),('w','y',3),('y','w',3),('w','x',7),('x','w',7),('y','x',2),('x','y',2)]

# print('full algorithm')
# for table in DV(x):
#     print('')
#     for i in table:
#         print(i)










