from Grafo1 import Grafo_dirigido, Nodo


def Edmonds_Karp(G, s, t, Gf):
    C = {}
    A = {}
    Q = []
    for v in G.V:
        C[v] = False
        A[v] = False
    C[s.id] = True
    Q.append(s)
    while len(Q) > 0:
        u = Q.pop()
        for v in u.vizinhos:
            if C[v] == False or Gf.V[u.id].vizinhos_saintes[v] > 0:
                C[v] = True
                A[v] = u.id
                if v == t:
                    p = [t]
                    w = t
                    while w != s:
                        w = A[w.id]
                        p.insert(0, w)
    return True




grafo = Grafo_dirigido()
with open('wiki.net', 'r') as arquivo:
    info = arquivo.read()
    info = info.split('\n')
    grafo.lerArquivo(info)

grafoF = Grafo_dirigido()
for v in grafo.V:
    grafoF.V[v] = grafo.V[v]
for e2 in grafo.E:
    e = [0, 0, 0]
    e[0] = grafoF.V[e2[1].id]
    e[1] = grafoF.V[e2[0].id]
    e[2] = 0
    grafoF.E.append(e)
    e[0].vizinhos_saintes[e[1].id] = 0
    e[1].vizinhos_entrantes[e[0].id] = 0
    grafoF.nE += 1

s = False
for v in grafo.V:
    if not s:
        s = grafo.V[v]
    t = grafo.V[v]


Edmonds_Karp(grafo, s, t, grafoF)