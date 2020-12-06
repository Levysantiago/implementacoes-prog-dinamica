# ENUNCIADO
# Dada uma sequência X =< x 1 , x 2 , . . . , x m > e uma sequência Y =< y 1 , y 2 , . . . , y k >
# o problema da maior subsequência comum (LCS) consiste em encontrar a maior sub-
# sequência presente nas duas listas. Uma subsequência é uma sequência que aparece na
# mesma ordem relativa, mas não necessariamente contı́gua. Por exemplo, < a, b, c >,
# < a, b, g >, < b, d, f >, < a, e, g > e < a, c, e, f, g > são subsequências de ¡a,b,c,d,e,f,g¿.
# Desta forma, uma sequência com n elementos possui 2 n diferentes subsequências possı́veis.
# Este é um problema clássico em ciência da computação com diversas aplicações em bi-
# oinformática. Exemplos: A LCS para as sequências de entrada < A, B, C, D, G, H >
# e < A, E, D, F, H, R > é < A, D, H > com tamanho 3. A LCS para as sequências de
# entrada < A, G, G, T, A, B > e < G, X, T, X, A, Y, B > é < G, T, A, B > com tamanho 4.

# Entradas
# a - primeira sequência
# b - segunda sequência
def sequencia(a, b, sizeA, sizeB):
    finalSeq = []

    for i in range(0, sizeA):
        if(a[i]):
            for j in range(0, sizeB):
                if(b[j]):
                    if(a[i] == b[j]):
                        index = max(i,j)
                        finalSeq.append((index, a[i]))
                        b[j] = None
        a[i] = None
    
    finalSeq.sort()
    finalList = []
    for item in finalSeq:
        finalList.append(item[1])

    return finalList

# Executando
a = ['A', 'B', 'C', 'D', 'G', 'H']
b = ['A', 'D', 'E', 'F', 'H', 'R']
print(sequencia(a,b,len(a), len(b)))

a = ['A', 'G', 'G', 'T', 'A', 'B']
b = ['G', 'X', 'T', 'X', 'A', 'Y', 'B']
print(sequencia(a,b,len(a), len(b)))
