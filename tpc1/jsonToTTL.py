import json

f = open('dataset.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
################################ Inicio do ficheiro ttl ####################################
inicioTTL="""
@prefix : <http://www.di.uminho.pt/prc2021/uc#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://www.di.uminho.pt/prc2021/uc> .
<http://www.di.uminho.pt/prc2021/uc> rdf:type owl:Ontology .
#################################################################
#    Object Properties
#################################################################
###  http://www.di.uminho.pt/prc2021/uc#ensina
:ensina rdf:type owl:ObjectProperty ;
        owl:inverseOf :éEnsinadaPor ;
        rdfs:domain :Professor ;
        rdfs:range :UnidadeCurricular .
###  http://www.di.uminho.pt/prc2021/uc#frequenta
:frequenta rdf:type owl:ObjectProperty ;
           owl:inverseOf :éFrequentadaPor ;
           rdfs:domain :Aluno ;
           rdfs:range :UnidadeCurricular .
###  http://www.di.uminho.pt/prc2021/uc#éAlunoDe
:éAlunoDe rdf:type owl:ObjectProperty ;
          owl:inverseOf :éProfessorDe .
###  http://www.di.uminho.pt/prc2021/uc#éEnsinadaPor
:éEnsinadaPor rdf:type owl:ObjectProperty .
###  http://www.di.uminho.pt/prc2021/uc#éFrequentadaPor
:éFrequentadaPor rdf:type owl:ObjectProperty .
###  http://www.di.uminho.pt/prc2021/uc#éProfessorDe
:éProfessorDe rdf:type owl:ObjectProperty ;
              owl:propertyChainAxiom ( :ensina
                                       :éFrequentadaPor
                                     ) .
#################################################################
#    Data properties
#################################################################
###  http://www.di.uminho.pt/prc2021/uc#anoLectivo
:anoLectivo rdf:type owl:DatatypeProperty .
###  http://www.di.uminho.pt/prc2021/uc#designação
:designação rdf:type owl:DatatypeProperty .
###  http://www.di.uminho.pt/prc2021/uc#nome
:nome rdf:type owl:DatatypeProperty .
#################################################################
#    Classes
#################################################################
###  http://www.di.uminho.pt/prc2021/uc#Aluno
:Aluno rdf:type owl:Class ;
       rdfs:subClassOf [ rdf:type owl:Restriction ;
                         owl:onProperty :frequenta ;
                         owl:someValuesFrom :UnidadeCurricular
                       ] .
###  http://www.di.uminho.pt/prc2021/uc#Professor
:Professor rdf:type owl:Class ;
           rdfs:subClassOf [ rdf:type owl:Restriction ;
                             owl:onProperty :ensina ;
                             owl:someValuesFrom :UnidadeCurricular
                           ] .
###  http://www.di.uminho.pt/prc2021/uc#UnidadeCurricular
:UnidadeCurricular rdf:type owl:Class .
#################################################################
#    Individuals
#################################################################
"""

counter = 0 ## é necesário o contador para controlar o final de cada classe para diferenciar quando termina com "," ou com ";"

########################### éAlunoDe ######################################
eAlunoDe="                    :éAlunoDe "

for docente in data.get("docentes") :
    if(counter<3):
     eAlunoDe+="  :"+docente.get("id")+" ,           \n                            " 
     counter+=1
    
    else: 
     eAlunoDe+="  :"+docente.get("id")+" ;            \n\n"
     counter=0
  

  
########################### Frequenta ######################################
frequenta="                    :frequenta"

for uc in data.get("unidadesCurriculares") :
    if(counter<3):
        frequenta+="  :"+uc.get("id")+" ,            \n                              "
        counter+=1

    else:
        frequenta+="  :"+uc.get("id")+" ;            \n\n"
        counter=0


########################### Alunos ######################################
alunos = []

eProfessorDe="                    :éProfessorDe "
eFrequentadaPor="                    :éFrequentadaPor"

for aluno in data.get("alunos") :
    idAluno = aluno.get("primeiroNome").lower()+aluno.get("ultimoNome").lower()
    nome ="                    :nome        "+"\""+aluno.get("primeiroNome")+" "+aluno.get("ultimoNome")+"\"    ."
    alunos.append(":"+idAluno+"     rdf:type    owl:NamedIndividual,\n"+"                             :Aluno ;\n\n"+frequenta+eAlunoDe+nome+"\n")

    if(counter<199):
        eProfessorDe+="  :"+idAluno+" ,           \n                                  "
        eFrequentadaPor+="      :"+idAluno+" ,           \n                                    "
        counter+=1

    else:    
        eProfessorDe+="  :"+idAluno+" ;            \n\n"
        eFrequentadaPor+="      :"+idAluno+" ;            \n\n"
        counter=0
########################### Professores ######################################
professores = []

idsDocentes = {} ## dicionário para associar keys/values

for docente in data.get("docentes") :
    idDocente = docente.get("id")

    idsDocentes[docente.get("ensina")]=docente.get("id")

    ensina ="                    :ensina         :"+ docente.get("ensina")+" ;\n\n"
    nome ="                    :nome        "+"\""+docente.get("nome").get("primeiro")+" "+docente.get("nome").get("último")+"\"    ."
    
    professores.append(":"+idDocente+"     rdf:type    owl:NamedIndividual,\n"+"                             :Professor ;\n\n"+ensina+eProfessorDe+nome+"\n")

########################### UnidadeCurricular ######################################
ucs = []
for uc in data.get("unidadesCurriculares") :
    idDocente = docente.get("id")
    ensina ="                    :éEnsinadaPor         :"+idsDocentes[uc.get("id")]+" ;\n\n"
    designacao ="                    :designação        "+"\""+uc.get("designação")+"\"    ;\n"
    anoLectivo ="                    :anoLectivo        "+"\""+uc.get("anoLectivo")+"\"    .\n\n"

    ucs.append(":"+idDocente+"     rdf:type    owl:NamedIndividual,\n"+"                    :UnidadeCurricular ;\n\n"+ensina+eFrequentadaPor+designacao+anoLectivo+"\n")


with open('ucsInfo.ttl','w') as f:
    f.write(inicioTTL)
    for a in alunos:
        f.write(a)
    for p in professores:
        f.write(p)
    for u in ucs:
        f.write(u)

print("DONE!")
