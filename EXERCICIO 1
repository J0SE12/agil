def move_trem(comandos):
    posicao_atual = 0
    
    for comando in comandos:
        if comando == "DIREITA":
            posicao_atual += 1
        elif comando == "ESQUERDA":
            posicao_atual -= 1
            
    return posicao_atual

# Exemplos de uso
comandos1 = ["DIREITA", "DIREITA"]
print("Posição Inicial: 0, Posição Final:", move_trem(comandos1))

comandos2 = ["ESQUERDA"]
print("Posição Inicial: 0, Posição Final:", move_trem(comandos2))

comandos3 = ["ESQUERDA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "ESQUERDA"]
print("Posição Inicial: 0, Posição Final:", move_trem(comandos3))
