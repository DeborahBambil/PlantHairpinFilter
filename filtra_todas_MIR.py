#Filtro dos genes snoRNAs do transcrito (GCF_000146045.2_R64_rna.fna) da levedura Yeast 
#AUTORA: MIRELE CAROLINA SOUZA

import re

#Leitura do Arquivo com o transcrito da Yeast
arquivo = open("hairpin.fa", "r")
#arquivo = open("teste_rna.fna", "r")
# Cria o arquivo de saida
arquivo_saida = open("saida_MIR_filtradas.fa", "w")
arq = open("saida_>_seq.fa", "w")

def filtro ():
    flag = 0
    j = 1
    cont = 0
    for line in arquivo:
        k = 1
        i = line
        if(flag == 1):
                i = line
                #print("FLAG: "+line)
                line = linha
                flag = 0
                
        match = re.search( r'^(>[\w]+-MIR[\w]+\sMI.+)', line) 
        if(match):        
            snoRNA = match.group(1)
            cont = cont+1
            #print(str(cont)+": "+line)
            arquivo_saida.write(snoRNA+"\n")
            arq.write(snoRNA+"\n")
            if(j == 1):
                for line in arquivo:
                    #print("LINHA DENTRO DO FOR: "+line)
                    snoRNA_match = re.search(r'(^[AUGC]+)', line) 
                    if(snoRNA_match and snoRNA_match.group(1)):
                        gene = snoRNA_match.group(1)
                        arquivo_saida.write(gene+"\n")
                        
                    match = re.search( r'^(>)', line) 
                    if(match):
                        linha = line
                        flag = 1
                        j = 0
                        break
            else:
                #print("LINHA ANTES DO FOR: "+line)
                for line in arquivo:
                    #print("LINHA DENTRO DO FOR: "+line)
                    #print("IIIIII: "+ i)
                    if(k==1):
                        snoRNA_match = re.search(r'(^[AUGC]+)', i) 
                        if(snoRNA_match and snoRNA_match.group(1)):
                            gene = snoRNA_match.group(1)
                            arquivo_saida.write(gene+"\n")
                            k = 0
                        
                    snoRNA_match = re.search(r'(^[AUGC]+)', line) 
                    if(snoRNA_match and snoRNA_match.group(1)):
                        gene = snoRNA_match.group(1)
                        arquivo_saida.write(gene+"\n")
                        
                    match = re.search( r'^(>)', line) 
                    if(match):
                        linha = line
                        flag = 1
                        break
            
            
filtro()