import requests as req
import urllib

GRAPH_DB_LINK = "http://gdb:7200/repositories/mapa"
PREFIXES = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX noInferences: <http://www.ontotext.com/explicit>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX : <http://www.di.uminho.pt/prc2021/teste-paises#>
"""

def main():


    query = """
    CONSTRUCT {
        ?s2 :éCidadeDe ?s1 .
    } WHERE {
        ?s1 rdf:type :País ;
            :temCidade ?s2 .
        
    }
    
    """

    res = req.get(GRAPH_DB_LINK, params=[('query', PREFIXES + query)])

    res.raise_for_status()

    res2 = req.get(GRAPH_DB_LINK + "/statements", params=["query", PREFIXES + res.text])

    res2.raise_for_status()

if __name__ == "__main__":
    main()