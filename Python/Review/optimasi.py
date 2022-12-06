import numpy as np 


def gradient(x1, x2):
    """
    Parameters
    ----------
    x : float
    
    
    Return
    ------
    grad: float
    
    """
    grad_1 = 2*x1
    grad_2 = 2*x2
    
    return grad_1, grad_2


def run_gradient(x1, x2, iter, alpha):

    temp_x1 = []
    temp_x2 = []
    for it in range(iter):
        # Calculate gradient
        grad_1, grad_2 = gradient(x1, x2)
        # Update
        x1 = x1 - alpha*grad_1
        x2 = x2 - alpha*grad_2
        # Cek kondisi critical point
        if abs(grad_1) <= 1e-6 and abs(grad_2) <= 1e-6 :
            print('Solusi x1 dan x2', str(x1), str(x2))
            break
        # Append
        temp_x1.append(x1)
        temp_x2.append(x2)

        print(x1, x2)

    return temp_x1, temp_x2


def obj_func(x):
    x1 = x[0]
    x2 = x[1]
    return x1**2 + x2**2 + 0.5


if __name__ == '__main__':
    x = np.random.rand(2, 1)*10
    # Coba ganti parameter alpha dari 0.1, 0.01 dan 5
    alpha = 0.1
    iter = 500
    all_x1, all_x2 = run_gradient(x[0], x[1], iter, alpha)