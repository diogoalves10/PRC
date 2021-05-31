import requests as req
import urllib

GDB_LINK = "http://localhost:7200/repositories/familia/statements?query="
PREFIXES = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX noInferences: <http://www.ontotext.com/explicit>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX : <http://prc.di.uminho.pt/2021/myfamily#>
"""

def main():

    query = """
    CONSTRUCT {
    ?f :eIrmão ?g.
 }
 
 WHERE {
     ?f :temProgenitor ?p .
     ?g :temProgenitor ?p . 
    
    filter (?f != ?g)    
}
    """

    queryInsert = """
    INSERT DATA {
    """
    res = req.get(GDB_LINK, params=[('query', PREFIXES + query)])

    res.raise_for_status()
    
    ins = queryInsert + res + "}"
    x = req.post(GDB_LINK, params=[('query', PREFIXES + ins)])

if __name__ == "__main__":
    main()