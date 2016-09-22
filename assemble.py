from basis_func import *
import numpy as np

def gradu_gradv(topo,x,y):
    """ A assembly code """
    return A

def f_v(topo,x,y):
    """ F assembly code """
    dx_phi,dy_phi,phi,surf_e = tri_p1(x,y,np.zeros(2)) # some problem here on eval_p
    F = surf_e / 3.0 * np.ones(x.shape[0])
    # for element in topo:



    print F
    return F
