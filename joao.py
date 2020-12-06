# ENUNCIADO
# Joãozinho da Piada possui um repertório de n piadas, sendo que cada piada possui uma duração de Pi minutos e
# produz uma quantidade Ri de risadas. Uma piada i só gera risadas na primeira vez em que é contada. Escreva um
# algoritmo que maximize a quantidade de risadas em um show de Joãozinho, considerando que ele só possui C minutos
# para se apresentar.

# r - lista de risadas
# t - lista de tempos
# C - tempo maximo do show
# qp - quantidade de piadas
def maximizaPiadas(r, t, C, qp):
    # matriz
    mx = []
    aux = []
    Cplus1 = C+1
    for i in range(Cplus1):
        aux.append(0)
    mx.append(aux)
    
    aux = []
    for i in range(qp):
        mx.append([0])
    
    for i in range(1, qp+1):
        for j in range(1, Cplus1):
            risosCima = mx[i-1][j]
            mx[i].append(risosCima)
            tempoPiada = t[i-1]
            if(tempoPiada <= j):
                risosPiada = r[i-1]
                risos = risosPiada + mx[i-1][j - tempoPiada]
                if(risos > risosCima):
                    mx[i][j] = risos
    
    maxRisadas = mx[i][j]

    # seleciona piadas
    selecionados = []
    while(mx[i][j] != 0):
        if(mx[i][j] != mx[i-1][j]):
            selecionados.append(i)
            j -= t[i-1]
        i -= 1

    return maxRisadas, selecionados


# Executando
r = [2,5,6,3]
t = [5,3,2,5]
C = 10
qp = len(r)

# Resultado deve ser (14, [4, 3, 2])
# máximo de 14 risadas
# piadas 4, 3 e 2

print(maximizaPiadas(r,t,C,qp))