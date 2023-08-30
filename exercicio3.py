#Configuração do Trilho:
#História de Usuário 1: Como condutor, quero definir os limites do trilho finito para que o trem nunca extrapole esses limites.

#História de Usuário 2: Como condutor, quero poder informar a posição inicial do trem no trilho finito.

#Execução dos Comandos:
#História de Usuário 3: Como condutor, quero poder fornecer uma lista de comandos para que o trem execute sequencialmente.

#História de Usuário 4: Como condutor, quero que o trem pare de se mover para a direita quando alcançar o limite superior do trilho finito.

#História de Usuário 5: Como condutor, quero que o trem pare de se mover para a esquerda quando alcançar o limite inferior do trilho finito.

#História de Usuário 6: Como condutor, quero que o trem execute no máximo 30 comandos em uma lista.

#Código Modificado:

def move_trem(comandos, posicao_inicial, limite_inferior, limite_superior):
    posicao_atual = posicao_inicial
    
    for comando in comandos:
        if comando == "DIREITA":
            if posicao_atual < limite_superior:
                posicao_atual += 1
        elif comando == "ESQUERDA":
            if posicao_atual > limite_inferior:
                posicao_atual -= 1
            
    return posicao_atual

# Configuração do trilho
limite_inferior = int(input("Informe o limite inferior do trilho: "))
limite_superior = int(input("Informe o limite superior do trilho: "))
posicao_inicial = int(input("Informe a posição inicial do trem: "))

# Execução dos comandos
comandos = input("Informe a lista de comandos (DIREITA/ESQUERDA separados por espaço): ").split()
if len(comandos) > 30:
    print("A lista de comandos não pode ter mais que 30 comandos.")
else:
    posicao_final = move_trem(comandos, posicao_inicial, limite_inferior, limite_superior)
    print("Posição Inicial:", posicao_inicial, "Posição Final:", posicao_final)
#Nesse código, o usuário é solicitado a fornecer as informações necessárias para configurar o trilho e iniciar a execução dos comandos. A função move_trem foi modificada para aceitar os parâmetros de posição inicial e os limites do trilho. Os comandos são lidos como uma única linha de entrada e são divididos em uma lista.

#As verificações foram adicionadas para garantir que o trem não exceda os limites do trilho finito e para limitar o número de comandos a 30.












def move_trem(comandos, posicao_inicial, limite_inferior, limite_superior):
    posicao_atual = posicao_inicial
    
    for comando in comandos:
        if comando == "DIREITA":
            if posicao_atual < limite_superior:
                posicao_atual += 1
        elif comando == "ESQUERDA":
            if posicao_atual > limite_inferior:
                posicao_atual -= 1
            
    return posicao_atual

# Configuração do trilho
limite_inferior = int(input("Informe o limite inferior do trilho: "))
limite_superior = int(input("Informe o limite superior do trilho: "))
posicao_inicial = int(input("Informe a posição inicial do trem: "))

# Execução dos comandos
comandos = input("Informe a lista de comandos (DIREITA/ESQUERDA separados por espaço): ").split()
if len(comandos) > 30:
    print("A lista de comandos não pode ter mais que 30 comandos.")
else:
    posicao_final = move_trem(comandos, posicao_inicial, limite_inferior, limite_superior)
    print("Posição Inicial:", posicao_inicial, "Posição Final:", posicao_final)
