import numpy as np
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix_string = ''
    
    # Read matrix
    for i in range(0,N):
        rowi = input()
        matrix_string = matrix_string + rowi + " " + str(i) + " 9; "
    matrix_string = matrix_string[0:-2]
    A = np.matrix(matrix_string)

    J_end = 0
    C_end = 0
    arrayA = np.array(A)
    arrayAsorted = arrayA[arrayA[:,0].argsort()]
    impossible = False
    for j in range(0,N):
        if J_end <= arrayAsorted[j,0]:
            arrayAsorted[j,3] = 1
            J_end = arrayAsorted[j,1]
        elif C_end <= arrayAsorted[j,0]:
            arrayAsorted[j,3] = 2
            C_end = arrayAsorted[j,1]
        else:
            impossible = True
            break
    if impossible == True:
        answer = 'IMPOSSIBLE'
    else:
        ordered_seq = '0'*N
        ordered_seq = list(ordered_seq)
        for k in range(0,N):
            pos = int(arrayAsorted[k,2])
            if arrayAsorted[k,3] == 1:
                ordered_seq[pos] = 'J'
            else:
                ordered_seq[pos] = 'C'
        answer = ''.join(ordered_seq)

    # Print results
    print("Case #{}: ".format(t)+answer)
        

    
        
    

