import json
  
# Opening JSON file
f = open('emd.json',)
  

data = json.load(f)
    
# Closing file
f.close()

atletas = []
clubes =[]
modalidades = []

for ind in data :
    clubes.append(ind['clube'])
    modalidades.append(ind['modalidade'])
    atleta = {}
    atleta['index'] = ind ['index']
    nome = ind['nome']
    nomeRes = nome['primeiro'] +' '+nome['último']
    atleta['nome'] = nomeRes
    atleta['idade'] = ind['idade']
    atleta ['género'] = ind ['género']
    atleta ['modalidae'] = ind ['modalidade']
    atleta['clube'] = ind ['clube']
    atleta['email'] = ind ['email']
    atleta ['federado'] = ind ['federado']
    atletas.append(atleta)

clubes = list(dict.fromkeys(clubes))
modalidades = list(dict.fromkeys(modalidades))


################################### EMD #############################################
for ind in data:
    print('###  http://www.di.uminho.pt/prc2021/gestaoEMD#EMD_'+ind['_id'])

    print(f":EMD_{ind['_id']} rdf:type owl:NamedIndividual , \n\t\t :EMD;")
    nome = ind['nome']
    
    nomeRes = nome['primeiro'] +' '+nome['último']
    print(f"\t\t :realizadoPor :A_{nomeRes.replace(' ','_')};")
    print(f"\t\t :dataEMD \"{ind['dataEMD']}\" ;")
    print(f"\t\t :resultado {ind['resultado']}.") 
                       

###########################Atletas################################################

for ind in data:
    nome = ind['nome']
    
    nomeRes = nome['primeiro'] +' '+nome['último']
    print(' ###  http://www.di.uminho.pt/prc2021/gestaoEMD#A_'+ nomeRes)
    
    print(f":A_{nomeRes.replace(' ','_')} rdf:type owl:NamedIndividual , \n\t\t :Atleta;")

    print(f"\t\t :pertenceA :{ind['clube'].replace(' ','')};")
    print(f"\t\t :pratica :{ind['modalidade']};")
    print(f"\t\t :email \"{ind['email']}\" ;")
    print(f"\t\t :federado {ind['federado']} ;")
    print(f"\t\t :genero \"{ind['género']}\" ;")
    print(f"\t\t :id \"A_{ind['index']}\" ;")
    print(f"\t\t :idade {ind['idade']} ;")
    print(f"\t\t :morada \"{ind['morada']}\" ;")

    print(f"\t\t :nome \"{nomeRes}\".") 
                       
##############################Clubes ################################

for ind in clubes:
    print('###  http://www.di.uminho.pt/prc2021/gestaoEMD#'+ind.replace(' ',''))

    print(f":{ind.replace(' ','')} rdf:type owl:NamedIndividual , \n\t\t :Clube;")
    print(f"\t\t :nome \"{ind}\" .")


################################## Modalidades ##################################

for ind in modalidades:
    print('###  http://www.di.uminho.pt/prc2021/gestaoEMD#'+ind)

    print(f":{ind} rdf:type owl:NamedIndividual , \n\t\t :Modalidade;")
    print(f"\t\t :nome \"{ind}\" .")


