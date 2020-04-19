import numpy as np
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix_string = ''
    
    # Read matrix
    for i in range(0,N):
        rowi = input()
        matrix_string = matrix_string + rowi + "; "
    matrix_string = matrix_string[0:-2]
    A = np.matrix(matrix_string)
    At = A.transpose()

    # Trace
    tr = int(A.trace())

    rep_col_count = np.zeros((1,N), dtype=int)
    rep_row_count = np.zeros((N,1), dtype=int)
    
    for j in range(1,N+1):
        rowsum = np.count_nonzero(A == j, axis=1)
        colsum = np.count_nonzero(A == j, axis=0)

        rep_col_count = rep_col_count + (colsum > 1)
        rep_row_count = rep_row_count + (rowsum > 1)

    n_rep_rows = int(sum(rep_row_count > 0))
    n_rep_cols = int(sum((rep_col_count > 0).transpose()))

    # Print results
    print("Case #{}: {} {} {}".format(t, tr, n_rep_rows, n_rep_cols))
        

    
        
    

