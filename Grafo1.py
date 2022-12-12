from multiprocessing import connection


class Nodo():
    def __init__(self, n, rotulo):
        self.id = n
        self.rotulo = rotulo
        self.conections = 0
        self.vizinhos = {}


class Grafo():
    def __init__(self):
        self.V = {}
        self.nV = 0
        self.E = []
        self.nE = 0

    def vertices(self):
        return self.V

    def arestas(self):
        return self.E

    def qtdVertices(self):
        return self.nV

    def qtdArestas(self):
        return self.nE

    def grau(self, v):
        return v.conections

    def rotulo(self, v):
        return v.rotulo

    def vizinhos(self, v):
        return v.vizinhos

    def haAresta(self, u, v):
        if u.vizinhos[v.id] < float('inf'):
            return True
        return False

    def peso(self, u, v):
        return u.vizinhos[v.id]

    def getNodo(self, id):
        return self.V[id]

    def lerArquivo(self, arquivo):
        leitura = 0
        for linha in arquivo:
            if linha == '':
                continue
            if linha[0] == '*':
                leitura += 1
                continue
            else:
                if leitura == 1:
                    valores = linha.split(' ')
                    node = Nodo(valores[0], valores[1])
                    self.V[node.id] = node
                    self.nV += 1
                elif leitura == 2:
                    valores = linha.split(' ')
                    u = self.getNodo(valores[0])
                    v = self.getNodo(valores[1])
                    u.conections += 1
                    v.conections += 1
                    u.vizinhos[v.id] = valores[2]
                    v.vizinhos[u.id] = valores[2]
                    self.nE += 1
                    self.E.append([u, v, valores[2]])



class Nodo_d(Nodo):
    def __init__(self, n, rotulo):
        super().__init__(n, rotulo)
        self.vizinhos_saintes = {}
        self.vizinhos_entrantes = {}

class Grafo_dirigido(Grafo):
    def __init__(self):
        super().__init__()

    def peso(self, u, v):
        return u.vizinhos_saintes[v.id]

    def get_vizinhos_saintes(self, v):
        return v.vizinhos_saintes

    def get_vizinhos_entrantes(self, v):
        return v.vizinhos_entrantes

    def lerArquivo(self, arquivo):
        leitura = 0
        for linha in arquivo:
            if linha == '':
                continue
            if linha[0] == '*':
                leitura += 1
                continue
            else:
                if leitura == 1:
                    valores = linha.split(' ')
                    node = Nodo_d(valores[0], valores[1])
                    self.V[node.id] = node
                    self.nV += 1
                elif leitura == 2:
                    valores = linha.split(' ')
                    u = self.getNodo(valores[0])
                    v = self.getNodo(valores[1])
                    u.conections += 1
                    v.conections += 1
                    u.vizinhos_saintes[v.id] = valores[2]
                    v.vizinhos_entrantes[u.id] = valores[2]
                    self.nE += 1
                    self.E.append([u, v, valores[2]])

    def inverter_arcos(self):
        E_t = []
        for arco in self.arestas():
            E_t.append([arco[1], arco[0], arco[2]])
        self.E = E_t
        for v in list(self.vertices().values()):
            aux = v.vizinhos_saintes
            v.vizinhos_saintes = v.vizinhos_entrantes
            v.vizinhos_entrantes = aux

    

grafo = Grafo()
with open('facebook_santiago.net', 'r') as arquivo:
    info = arquivo.read()
    info = info.split('\n')
    grafo.lerArquivo(info)