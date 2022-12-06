import numpy as np


def gradient(A, x, y):
    """
    
    
    Parameters
    ----------
    x : float
    
    
    Return
    ------
    grad: float
    
    """
    grad = 2*A.T@A@x - 2*A.T@y
    
    return grad 


def run_gradient(x, A, y, iter, alpha):

    for it in range(iter):
        # Calculate gradient
        grad = gradient(A, x, y)
        # Update
        x = x - alpha*grad
        # Cek kondisi critical point
        fungsi_obj = obj_func(x, A, y)
        print('Error fungsi objective :', str(fungsi_obj))
        if fungsi_obj <= 1e-6:
            break

        # Append
     
    return x
    

def obj_func(x_inisiasi, *args):
    A, y = args
    return np.linalg.norm(A@x_inisiasi - y)**2


if __name__ == '__main__':
    x_asli = np.ones((10,1))
    x_inisiasi = np.random.randn(10,1)
    A = np.random.randn(20,10)
    y = A@x_asli
    alpha = 0.01
    it = 100
    x_gradient = run_gradient(x_inisiasi, A, y,it, alpha)
    args = (A,y)

    print('Error nilai x', str(np.linalg.norm(x_gradient - x_asli)**2))
    
    # Hitung dengan numeric
    x_analitik = np.linalg.pinv(A.T@A)@A.T@y

    print('Perbedaan analitik dan gradient ', str(np.linalg.norm(x_analitik - x_gradient)**2))

