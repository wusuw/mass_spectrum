# Author: shunkai 
# Date: 2021-02-20 15:13:19 
# Last Modified by:   shunkai 
# Last Modified time: 2021-02-20 15:13:19  
# describe:首先找到移码蛋白的基因的并且找到这些基因在origin组织里面的表达量

import sys 
def main(filein,filein2,sam_name,fileout) : 
    f1 = open(filein,"r")            # \all_codon_shift3\out1_origin_gene_info.txt
    f2 = open(filein2,"r")           # \all_codon_shift3\origin_proteinGrouip\proteinGroup.txt
    fo = open(fileout,"a+")           # \all_codon_shift3\out2_origin_gene_info.txt
    gene_lis = []
    for line in f1 : 
        gene = line.strip()
        gene_lis.append(gene)
    for lin in f2:
        seq = lin.split("\t")
        gene_ = seq[6]
        if gene_ in gene_lis:
            print(sam_name)
            fo.write("\t".join([sam_name,gene_,"\t".join(seq[36:46])])+"\n")


main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
