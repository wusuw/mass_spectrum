# Author: shunkai 
# Date: 2021-03-23 20:35:33 
# Last Modified by:   shunkai 
# Last Modified time: 2021-03-23 20:35:33  
# describe: 取出具有移码的基因的名字
import sys 

def main(filein,fileout) : 
    f1 = open(filein,"r")     #all_codon_shift2/lz_shift2_result/gene_count.txt
    fo = open(fileout,"w")    #all_codon_shift2/out1_origin_gene_info
    lis_name = []
    for line in f1 : 
        geneName = line.split("_")[0]
        lis_name.append(geneName)
    lis_name = list(set(lis_name))
    for i in lis_name:
        fo.write(i+"\n")
 
main(sys.argv[1],sys.argv[2])
