import numpy as np


def fungsi_penjumlahan(input_vektor):
    """
    Ini adalah docstring, yaitu membantu menjelaskan apa itu parameter dari fungsi dan 
    apa keluarannya
    
    Parameters
    ----------
    input_vektor : array
    
    
    Return
    ------
    total: int atau float
    
    """
    
    # Alokasi variabel
    total = 0
    
    # Mulai loop
    for idx in range(len(input_vektor)):
    	total += input_vektor[idx]
    
    return total


if __name__ == '__main__':
    a = np.random.randn(100, 1)
    total_jumlah = fungsi_penjumlahan(input_vektor=a)
    # Cek kesamaan dengan numpy
    assert np.allclose(total_jumlah, np.sum(a))
    print(total_jumlah, np.sum(a))