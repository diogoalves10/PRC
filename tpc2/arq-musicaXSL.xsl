<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:xd="http://www.oxygenxml.com/ns/doc/xsl"
    exclude-result-prefixes="xs xd"
    version="2.0">
    <xd:doc scope="stylesheet">
        <xd:desc>
            <xd:p><xd:b>Created on:</xd:b> Mar 22, 2021</xd:p>
            <xd:p><xd:b>Author:</xd:b> Diogo</xd:p>
            <xd:p>Conversão do arquivo Musical de XML para TTL</xd:p>
        </xd:desc>
    </xd:doc>
    
    <xsl:output method="text" encoding="UTF-8" indent="yes"></xsl:output>
    
    <xsl:template match="obra">
        ###  http://www.di.uminho.pt/prc2021/am#<xsl:value-of select="@id"/>
        :<xsl:value-of select="@id"/> rdf:type owl:NamedIndividual ,
        :Obra ;
        
        :titulo "<xsl:value-of select="titulo"/>"
        <xsl:if test="subtitulo">
        ; :subtítulo "<xsl:value-of select="subtitulo"/>"
        </xsl:if>
        
        <xsl:if test="tipo">
        ; :tipo "<xsl:value-of select="tipo"/>"
        </xsl:if>
        
        <xsl:if test="compositor">
       ; :compostaPor :<xsl:value-of select="replace(compositor,' ','')"/> 
        </xsl:if>
        
        <xsl:if test="arranjo">
            ;   :arranjadaPor :<xsl:value-of select="replace(arranjo,' ','')"/> 
        </xsl:if>
         
        
        <xsl:if test="inf-relacionada">
        ; :href "<xsl:value-of select="inf-relacionada/video/@href"/>" 
        </xsl:if>  .   
         
         
       
        ###  http://www.di.uminho.pt/prc2021/am#<xsl:value-of select="replace(compositor,' ','')"/>
        :<xsl:value-of select="replace(compositor,' ','_')"/> rdf:type owl:NamedIndividual ,
        :Compositor ;
        :compôs :<xsl:value-of select="@id"/>.
          
        
        <xsl:if test="arranjo">
            ###  http://www.di.uminho.pt/prc2021/am#<xsl:value-of select="replace(arranjo,' ','')"/>
            :<xsl:value-of select="replace(arranjo,' ','_')"/> rdf:type owl:NamedIndividual ,
            :Arranjo ,
            :Compositor ;
            :arranjou :<xsl:value-of select="@id"/> .            
        </xsl:if>
        
        
        <xsl:for-each-group select="instrumentos/instrumento" group-by=".">
            ###  http://www.di.uminho.pt/prc2021/amd#<xsl:value-of select="replace(designacao,' ','')"/> 
            :<xsl:value-of select="replace(designacao,' ','_')"/> rdf:type owl:NamedIndividual,
            :Instrumento ;
            :designação "<xsl:value-of select="designacao"/>" .
            # --------------------------------------------------
            
            <xsl:for-each select="partitura">
                ### http://www.di.uminho.pt/prc2021/amd#<xsl:value-of select="@path"/>
                :<xsl:value-of select="@path"/> rdf:type owl:NamedIndividual ,
                :Partitura ;
               
                :type "<xsl:value-of select="@type"/>" ;
                :path "<xsl:value-of select="@path"/>" 
                <xsl:if test="@afinacao">
                    ; :afinação "<xsl:value-of select="@afinacao"/>" 
                </xsl:if>
                <xsl:if test="@voz">
                    ; :voz "<xsl:value-of select="@voz"/>" 
                </xsl:if>
                <xsl:if test="@clave">
                    ; :clave "<xsl:value-of select="@clave"/>" 
                </xsl:if>  .
                # --------------------------------------------------
            </xsl:for-each>
            
        </xsl:for-each-group>
        
    </xsl:template>
    
   
</xsl:stylesheet>