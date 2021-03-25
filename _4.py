# Author: shunkai 
# Date: 2021-03-23 22:05:00 
# Last Modified by:   shunkai 
# Last Modified time: 2021-03-23 22:05:00  
# describe:分基因表达量

import sys 


def main(filein,filein2,fileout) : 
    f1 = open(filein,"r")       #  \all_codon_shift3\out1_origin_gene_info.txt    provide the gene name we have detected frameshift
    f2 = open(filein2,"r")      #   all_codon_shift3\out3           provide the peptide quantfy in all tissue 
    fo = open(fileout,"w")      #   out4_gene_expresion
    dic_gene = {}
    dic_hou = {}
    for line in f2 :
        line = line.strip()
        seq = line.split("\t")
        geneName = seq[1]
        if geneName  in dic_gene.keys():  
            dic_gene[geneName].append(line)
        if geneName not in dic_gene.keys():
            dic_gene[geneName] = []
            dic_gene[geneName].append(line)
    for lin in f1:
        lin = lin.strip()
        dic_hou[lin] = {}
        if lin in dic_gene.keys():
            for i in dic_gene[lin]:
                seq1 = i.split("\t")
                if seq1[-1] in dic_hou[lin].keys():
                    dic_hou[lin][seq1[-1]].append(seq1[-2])
                elif seq1[-1] not in dic_hou[lin].keys():
                    dic_hou[lin][seq1[-1]] = []
                    dic_hou[lin][seq1[-1]].append(seq1[-2])
        for k,v in dic_hou[lin].items():
            sum = 0
            for j in v:
                sum = sum + float(j) 
            fo.write("\t".join([lin,k,str(sum)])+"\n")
        #print(lin+"\t"+str(dic_hou[lin]))
main(sys.argv[1],sys.argv[2],sys.argv[3])
