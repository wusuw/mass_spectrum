# Author: shunkai 
# Date: 2021-03-23 22:13:29 
# Last Modified by:   shunkai 
# Last Modified time: 2021-03-23 22:13:29  
# describe:除去带有reference的行
 

import sys 


def main(filein,fileout) : 
    f1 = open(filein,"r")    # all_codon_shift2/out4_gene_expression
    fo = open(fileout,"w")   # out5_gene_expression_noref 
    for line in f1 :
        if "reference" in line:
            continue
        else:
            fo.write(line) 
main(sys.argv[1],sys.argv[2])
