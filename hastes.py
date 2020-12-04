# ENUNCIADO
# Dada uma haste de n polegadas de comprimento e uma tabela de
# preços p i para i = 1, 2, ..., n, determine a receita máxima r n que se pode obter cortando a haste e vendendo os
# pedaços. Observe que, se o preço p n para uma haste de comprimento n for suficientemente grande, uma solução ótima
# pode exigir que ela não seja cortada.

# Params
# p - lista de preços
# n - tamanho da haste
def hastes(p, n):
    if(n == 0):
        return 0
    if(n == 1):
        return p[0]
    l = []
    until = (n // 2) + (n % 2) + 1
    for i in range(1,until):
        print(i, " e ", n-i)
        l.append(p[i-1] + p[n - i-1])
    print(l)
    return max(l)

_p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(hastes(_p, 3))