# Author: shunkai 
# Date: 2021-03-24 00:06:08 
# Last Modified by:   shunkai 
# Last Modified time: 2021-03-24 00:06:08  
# describe:
 

import sys 


def main(filein,filein2,sam_name,fileout) : 
    f1 = open(filein,"r") 
    f2 = open(filein2,"r")
    fo = open(fileout,"a+")
    lis_gene_ni_genome = [] 
    for lin in f2:
        name = lin.strip()
        lis_gene_ni_genome.append(name)
    for line in f1 :
        seq = line.split("\t")
        shiftName = seq[5] 
        if "minus" in line or "plus" in line:
            if shiftName.startswith("REV") or shiftName in lis_gene_ni_genome:   # 判断是不是反向的以及判断打到的肽段是不是在基因组里面有的基因
                continue
            else:
                fo.write("\t".join([sam_name,shiftName.split("_")[0],"\t".join(seq[34:44])])+"\n")

main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
