import random
class Ambiente:
    def __init__(self):
        self.grid = [[0,0,0],[0,"x","x"], [0,0,1]]
    
    def mostrar_ambiente(self):
        for linha in self.grid:
            print(linha)


class Agente:

    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.posicao = [0,0]

    def verificar_objetivo(self):
        x, y = self.posicao
        return self.ambiente.grid[x][y] == 1

    def movimentos_possiveis(self):
        movimentos = []
        x, y = self.posicao
        grid = self.ambiente.grid
        if x > 0 and grid[x-1][y] != 'x':
            movimentos.append('cima')
        if x < len(grid) - 1 and grid[x+1][y] != 'x':
            movimentos.append('baixo')
        if y > 0 and grid[x][y-1] != 'x':
            movimentos.append('esquerda')
        if y < len(grid[0]) - 1 and grid[x][y+1] != 'x':
            movimentos.append('direita')
        return movimentos
    
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
            print(f"Agente movido para {self.posicao} na direção {direcao}")
        else:
            print(f"Não há movimentos possíveis a partir da posição {self.posicao}")
        
ambiente = Ambiente()
agente = Agente(ambiente)

ambiente.mostrar_ambiente()
print("Posição inicial do agente:", agente.posicao)

movimentos_maximos = 20
for _ in range(movimentos_maximos):
    agente.mover_agente()
    if agente.verificar_objetivo():
        print("O agente alcançou o objetivo!")
        break

print("Posição final do agente:", agente.posicao)