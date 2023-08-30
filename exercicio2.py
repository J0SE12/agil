# Trilho Finito:
#História de Usuário 1: Como condutor, quero que o trem pare de se mover para a direita quando alcançar a posição máxima no trilho finito.

#História de Usuário 2: Como condutor, quero que o trem pare de se mover para a esquerda quando alcançar a posição mínima no trilho finito.


def move_trem(comandos, trilho_finito=True):
    posicao_atual = 0
    limite_inferior = -2
    limite_superior = 10
    
    for comando in comandos:
        if comando == "DIREITA":
            if trilho_finito and posicao_atual == limite_superior:
                continue  # Não mova para a direita além do limite superior
            posicao_atual += 1
        elif comando == "ESQUERDA":
            if trilho_finito and posicao_atual == limite_inferior:
                continue  # Não mova para a esquerda além do limite inferior
            posicao_atual -= 1
            
    return posicao_atual

# Exemplos de uso com trilho infinito
comandos1 = ["DIREITA", "DIREITA"]
print("Posição Inicial: 0, Posição Final:", move_trem(comandos1, False))

comandos2 = ["ESQUERDA"]
print("Posição Inicial: 0, Posição Final:", move_trem(comandos2, False))

# Exemplos de uso com trilho finito
comandos3 = ["ESQUERDA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "ESQUERDA"]
print("Posição Inicial: 0, Posição Final:", move_trem(comandos3, True))

#Nesse código modificado, o argumento trilho_finito foi adicionado à função move_trem. Quando definido como True, o trem não poderá exceder os limites do trilho finito. Quando definido como False, o trem pode explorar o trilho infinito.

#As verificações foram adicionadas para garantir que o trem não se mova além dos limites definidos (limite inferior -2 e limite superior 10) se o trilho for finito. Se o trilho for infinito, essas verificações são ignoradas.

#Os exemplos de uso demonstram tanto o trilho infinito quanto o finito.








def move_trem(comandos, trilho_finito=True):
    posicao_atual = 0
    limite_inferior = -2
    limite_superior = 10
    
    for comando in comandos:
        if comando == "DIREITA":
            if trilho_finito and posicao_atual == limite_superior:
                continue  # Não mova para a direita além do limite superior
            posicao_atual += 1
        elif comando == "ESQUERDA":
            if trilho_finito and posicao_atual == limite_inferior:
                continue  # Não mova para a esquerda além do limite inferior
            posicao_atual -= 1
            
    return posicao_atual

# Exemplos de uso com trilho infinito
comandos1 = ["DIREITA", "DIREITA"]
print("Posição Inicial: 0, Posição Final:", move_trem(comandos1, False))

comandos2 = ["ESQUERDA"]
print("Posição Inicial: 0, Posição Final:", move_trem(comandos2, False))

# Exemplos de uso com trilho finito
comandos3 = ["ESQUERDA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "ESQUERDA"]
print("Posição Inicial: 0, Posição Final:", move_trem(comandos3, True))
