problema = { 
            'estadoInicial' : 'T',
            'estadoObjetivo' : 'RL',
            'acoes': {
                1 : ['T', 'C', 3],
                2 : ['C', 'T', 3],
                3 : ['T', 'F', 8],
                4 : ['F', 'T', 8],
                5 : ['F', 'C', 4],
                6 : ['C', 'F', 4],
                7 : ['C', 'P', 2],
                8 : ['P', 'C', 2],
                9 : ['P', 'F', 6],
                10 : ['F', 'P', 6],
                11 : ['P', 'CA', 5],
                12 : ['CA', 'P', 5],
                13 : ['F', 'G', 4],
                14 : ['G', 'F', 4],
                15 : ['G', 'CA', 6],
                16 : ['CA', 'G', 6],
                17 : ['CA', 'BB', 14],
                18 : ['BB', 'CA', 14], 
                19 : ['G', 'TM', 8],
                20 : ['TM', 'G', 8],
                21 : ['TM', 'BB', 4],
                22 : ['BB', 'TM', 4],
                23 : ['TM', 'E', 6],
                24 : ['E', 'TM', 6],
                25 : ['E', 'RL', 12],
                26 : ['RL', 'E', 12]
                } 
            }

borda = []

def criarNo(estado, noPai = None, acao = None, custo = 0, profundidade = 0):
  no = {}
  no['estado'] = estado
  no['noPai'] = noPai
  no['acao'] = acao
  no['custo'] = custo
  no['profundidade'] = profundidade
  return no


def buscarEmArvore(problema, borda):
    
    borda.append(criarNo(problema['estadoInicial']))
     
    while(True):
        if len(borda) == 0:
            print("Falha")
            return 
        
        no = borda.pop()
        
        if problema['estadoObjetivo'] == no['estado']:
            print('sucesso')
            print(no)
            return
        
        borda = [*borda, *expandir(no, problema)]
 
 
def expandir(no, problema):
    
    sucessores = []

    for index in problema['acoes']:

        if problema['acoes'][index][0] == no['estado']:

            s = {}
        
            s['estado'] = problema['acoes'][index][1]
            s['noPai'] = no['estado']
            s['acao'] = index
            s['custo'] = no['custo'] + problema['acoes'][index][2]
            s['profundidade'] = no['profundidade'] + 1 
            
            sucessores.append(s)

    return sucessores
 
 
 
buscarEmArvore(problema, borda)