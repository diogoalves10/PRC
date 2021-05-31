const { default: axios } = require('axios');
var express = require('express');
var router = express.Router();
var gdb = require('../utils/graphdb')


/* GET home page. */
router.get('/api/emd', async function(req, res) {

  var myquery = `
  select ?s where { 
    ?s a :EMD.
  }
  `

  var result = await gdb.execQuery(myquery); /*await é quando é assincruno pode-se usar try catch*/
  var dados = result.results.binding.map(c => {
    return {
      nome: c.nome.value,
      data: c.data.value,
      resultado: c.resultado.value
    }
  })
  res.jsonp(dados)
});

router.get('/api/emd/:id', async function(req, res, next) {
  var myquery = `select ?nome ?data ?resultado  where {
    :${req.params.id} a :EMD ;
         :nome ?nome;
         :dataEMD ?data;
         :resultado ?resultado.
         
  }`

  var result = await gdb.execQuery(myquery);
});

router.get('/api/modalidades', async function(req, res, next) {
    var myquery = `select distinct(?s)  where {
      ?s a :Modalidades.          
    }`
  
var result = await gdb.execQuery(myquery);  
  });

router.get('api/emd?res=OK', async function(req, res, next) {
  var myquery = `select (count(?s) as ?validos) where { 
    ?s a :EMD;
        :resultado "true"^^xsd:boolean
         
  }`

var result = await gdb.execQuery(myquery);  
});

router.get('/api/modalidades/:id', async function(req, res, next) {
  var result = await gdb.execQuery(myquery);  
});

router.get('/api/atletas?gen=F', async function(req, res, next) {
    var myquery = `select ?nome where { 
      ?s a :Atleta;
          :genero "F"
           
    }order by (?name)`

  var result = await gdb.execQuery(myquery);  
  });

router.get('/api/atletas?clube=X', async function(req, res, next) {
  var myquery = `select  * where {
    ?s a :Atleta;
    :pertenceA :${req.params.clube}
  	 
} `

  

  var result = await gdb.execQuery(myquery);  
});
module.exports = router;
