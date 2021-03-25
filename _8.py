# Author: shunkai 
# Date: 2021-03-24 13:08:05 
# Last Modified by:   shunkai 
# Last Modified time: 2021-03-24 13:08:05  
# describe:
 

import sys 


def main(filein,filein2,fileout) : 
    f1 = open(filein,"r")    # out5_shift_gene_expression_noref
    f2 = open(filein2,"r")   # out5_gene_expression_noref
    fo = open(fileout,"w")   # out6_shift_origin_intensity
    dic_shift_gene = {}
    for line in f1 :
        seq = line.strip().split("\t")
        name = "\t".join(seq[0:2])
        inten = seq[2]
        dic_shift_gene[name] = inten

    for lin in f2:
        seq1 = lin.strip().split("\t")
        name1 = "\t".join(seq1[0:2])
        inten1 = seq1[2]
        if name1 in dic_shift_gene.keys():
            shift_liang = dic_shift_gene[name1]
            fo.write("\t".join([name1,str(inten1),str(shift_liang)])+"\n")
        if name1 not in dic_shift_gene.keys():
            shift_liang = 0
            fo.write("\t".join([name1,str(inten1),str(shift_liang)])+"\n")

main(sys.argv[1],sys.argv[2],sys.argv[3])
