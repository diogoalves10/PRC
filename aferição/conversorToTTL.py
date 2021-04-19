
def listaFrações():
  
    with open(('listaFrações.txt') ) as f:
        lines = f.readlines()
    res = ''
    for line in lines:
        descricao = line.split(',')[0].replace('º ','')
        fracao = line.split(',')[1]
        permi = line.split(',')[2]
        mensa = line.split(',')[3]
        res += '''###  http://www.di.uminho.pt/prc2021/condominios#'''+descricao +'''
        :'''+descricao +''' rdf:type owl:NamedIndividual ,
               :Fração ;
      :descrição "''' +descricao + '''"^^xsd:string ;
      :fração "''' + fracao + '''"^^xsd:string ;
      :mensalidade ''' +mensa + ''' ; 
      :permilagem '''+permi + '''.   
    '''
    with open('lifs.ttl','w') as fr:
        fr.write(res)   
      
     
def mapaPag():
    with open(('mapaPagamentos.txt') ) as f:
        lines = f.readlines()
    res = ''
    i = 0
    for line in lines:
        fracao = line.split(',')[0]
        months = []
        meses = ''
        for x in range (11):
            months.append(line.split(',')[x+1])
        for x in range (11):
            meses += '"'+months[x] + '", \n'
        inte = str(i)    
        res += '''###  http://www.di.uminho.pt/prc2021/condominios#pagamento'''+ inte +'''
        :pagamento'''+inte +''' rdf:type owl:NamedIndividual ,
               :Pagamento ;
        :descrição "''' +fracao + '''"^^xsd:string ;
        :mês '''+ str(meses) + ''' .
        '''
        i+=i
       
    with open('pagamentos.ttl','w') as fr:
        fr.write(res)   

def recDes():
  
    with open(('receitasEDespesas.txt') ) as f:
        lines = f.readlines()
    res = ''
    i=1
    for line in lines:
        numero = line.split(',')[0]
        tipo = line.split(',')[1]
        data = line.split(',')[2]
        valor = line.split(',')[3]
        entidade = line.split(',')[4]
        descricao = line.split(',')[5]
        res += '''###  http://www.di.uminho.pt/prc2021/condominios#entrada'''+ numero.split('/')[1] +'''
        :entrada'''+numero.split('/')[1] +''' rdf:type owl:NamedIndividual ,
                :entradaRec-Des ;
        :data "''' +data + '''"^^xsd:string ;       
        :descrição "''' +descricao.split('/n')[0] + '''"^^xsd:string ;
        :entidade "''' + entidade + '''"^^xsd:string ;
        :numero "''' + numero + '''"^^xsd:string ;
        :tipo "''' + tipo + '''"^^xsd:string ;
        :val ''' + valor + '''.  
        '''
    with open('recs-des.ttl','w') as fr:
        fr.write(res)   



def main():
    #listaFrações()
    #mapaPag()
   # recDes()
 
if __name__ == "__main__":
    main() 