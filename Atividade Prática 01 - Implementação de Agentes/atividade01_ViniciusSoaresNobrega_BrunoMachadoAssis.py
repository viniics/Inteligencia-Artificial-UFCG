class Ambiente:
    def __init__(self):
        self.grid = [[0,0,0],[0,"x","x"], [0,0,1]]
    
    def mostrar_ambiente(self):
        for linha in self.grid:
            print(linha)


class Agente:
    def __init__(self, ambiente):
        self.ambiente = ambiente
        self.posicao = [0,1]

    def mover_agente(self,direcao):
        return 0

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
        
ambiente = Ambiente()
agente = Agente(ambiente)

ambiente.mostrar_ambiente()
print(agente.movimentos_possiveis())
