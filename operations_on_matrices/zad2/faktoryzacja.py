def make_U_and_L(A):
    n = len(A)

    # tworzenie macierzy U z A
    for i in range(n):
        pivot_A = A[i][i]
        
        for j in range(i+1,n):
            tmp_A= A[j][i]
            # wpisanie współczynnika macierzy L
            for k in range(i,n):
                A[j][k] -= tmp_A * (A[i][k]/pivot_A)
            A[j][i] = tmp_A/pivot_A
                
    return A
