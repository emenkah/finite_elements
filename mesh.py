import numpy as np

def read_msh(filename):

    """ read mesh code """

    x = np.array([])
    y = np.array([])

    f = open(filename,'r')

    for line in f:
        if line[0] == '$':
            print "this is useless"
        else:
            l = map(float,line.split())
            # print(map(float,line.split())) # convert string to list of floats
            if len(l) == 4:
                x = np.append(x,l[1])
                y = np.append(y,l[2])
            if len(l) == 7:

            if len(l) == 8:


    print(x)
    print(y)

    nodes = None
    b_nodes = None



    f.close()

    r_id = 0
    for row in topo:
        ck =      (x[row[1]]-x[row[0]])*(y[row[2]]-y[row[0]])
        ck = ck - (x[row[2]]-x[row[0]])*(y[row[1]]-y[row[0]])
        if ck < 0:
            topo[r_id,:] = np.array([[row[0],row[2],row[1]]])
        r_id+=1

    print r_id
    return topo , x , y , nodes , b_nodes
