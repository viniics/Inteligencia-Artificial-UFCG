#O objetivo da atividade é implementar um agente inteligente simples
# que tomará decisões em um ambiente simulado,
# sendo o ambiente um grid 2d, com um tesouro a ser encontrado pelo agente
# Para a nossa implementação, usamos um agente simples baseado em Regras,
# onde ele percorre 20 passos randomicamente por um ambiente modelado como uma Matriz 3x3,
# analisando quais são as direções percorríveis
# até chegar (ou não) no tesouro.
# Os lugares percorríveis na matriz são descritos como "0"
# o tesouro é descrito como "1", e os obstáculos são descritos como "x'.

import random
class Ambiente:

    # Criacao da matriz, arbitrariamente definida como uma 3x3
    def __init__(self):
        self.matriz = [[0,0,0],[0,"x","x"], [0,0,1]]
    
    def mostrar_ambiente(self):
        for linha in self.matriz:
            print(linha)


class Agente:
    # Construtor do Agente. Recebe um ambiente para que ele possa agir sobre
    # Agente começa na posicao linha 0, coluna 0
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.posicao = [0,0]

    # Função que verifica se o Agente já chegou no objetivo, que eh representado pelo numero "1"
    def verificar_objetivo(self):
        x, y = self.posicao
        return self.ambiente.matriz[x][y] == 1
    # Funcao que calcula os movimentos que são possíveis do agente realizar. Respeitando os limites da matriz e os obstaculos, represntados pelo "x"
    def movimentos_possiveis(self):
        movimentos = []
        x, y = self.posicao
        matriz = self.ambiente.matriz
        if x > 0 and matriz[x-1][y] != 'x':
            movimentos.append('cima')
        if x < len(matriz) - 1 and matriz[x+1][y] != 'x':
            movimentos.append('baixo')
        if y > 0 and matriz[x][y-1] != 'x':
            movimentos.append('esquerda')
        if y < len(matriz[0]) - 1 and matriz[x][y+1] != 'x':
            movimentos.append('direita')
        return movimentos
    
    # O metodo seleciona, randomicamente, um dos movimentos possiveis,
    # que sao obtidos atraves da funcao "movimentos_possives".
    # Baseado nessa feita, o agente faz seu movimento e atualiza o atributo "posicao".
    def mover_agente(self):
        movimentos_possiveis = self.movimentos_possiveis()
        if movimentos_possiveis:
            direcao = random.choice(movimentos_possiveis)
            x, y = self.posicao
            if direcao == 'cima':
                self.posicao = [x-1, y]
            elif direcao == 'baixo':
                self.posicao = [x+1, y]
            elif direcao == 'esquerda':
                self.posicao = [x, y-1]
            elif direcao == 'direita':
                self.posicao = [x, y+1]
            print(f"Agente movido para {direcao}, chegando na posicao {self.posicao}")
        
ambiente = Ambiente()
agente = Agente(ambiente)

ambiente.mostrar_ambiente()
print("Posição inicial do agente:", agente.posicao)
resultado_final = "O agente não alcancou o objetivo"

# Definindo o numero maximo de movimentos possiveis
movimentos_maximos = 20

# Agora, o agente vai se movimentar, ate encontrar o objetivo
for _ in range(movimentos_maximos):
    agente.mover_agente()

    # Se encontrar o tesouro, a iteracao acaba e o objetivo foi alcancado 
    if agente.verificar_objetivo():
        resultado_final = "O agente alcançou o objetivo!"
        break

print(f"\n{resultado_final}\nPosição final do agente: {agente.posicao}")