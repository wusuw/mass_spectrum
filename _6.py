# Author: shunkai 
# Date: 2021-03-23 22:18:33 
# Last Modified by:   shunkai 
# Last Modified time: 2021-03-23 22:18:33  
# describe:按照基因分文件，最后用来画图
 
 

import sys 


def main(filein) : 
    f1 = open(filein,"r")  #all_codon_shift2/out5_gene_xepression_noref
    for line in f1 : 
        line = line.strip()
        seq = line.strip().split("\t")
        genename = seq[0]
        fo = open("all_codon_shift3/shift3_shift_origin/"+genename+".txt","a+") 
        fo.write(line+"\n") 

main(sys.argv[1])

