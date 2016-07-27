import numpy as np
import numpy.matlib as nm
from vgd import VGD

class MVN:
    def __init__(self, mu, A):
        self.mu = mu
        self.A = A
    
    def dlnprob(self, theta):
        return -1*np.matmul(theta-nm.repmat(self.mu, theta.shape[0], 1), self.A)
    
if __name__ == '__main__':
    A = np.array([[0.2260,0.1652],[0.1652,0.6779]])
    mu = np.array([-0.6871,0.8010])
    
    model = MVN(mu, A)
    
    x0 = np.random.normal(0,1, [10,2]);
    #x0 = np.array([[-0.2870, 0.7716],[0.3683, 1.5184],[-0.2933,0.8799]]);
    theta = VGD().update(x0, model.dlnprob, n_iter=1000, stepsize=0.01)
    
    print np.mean(theta,axis=0)