# Author: shunkai 
# Date: 2021-03-24 13:51:04 
# Last Modified by:   shunkai 
# Last Modified time: 2021-03-24 13:51:04  
# describe:看各个组织中移码蛋白的量，不看基因的水平
 

import sys 


def main(filein,fileout) : 
    f1 = open(filein,"r")    # out6
    fo = open(fileout,"w")   # out7
    dic1 = {}
    for line in f1 : 
        seq = line.split("\t")
        tissue = seq[1]
        origin = float(seq[2])
        shift = float(seq[3])
        lis1 = [origin,shift]
        if tissue not in dic1.keys():
            dic1[tissue] = lis1
        if tissue in dic1.keys():
            dic1[tissue] = [dic1[tissue][0]+origin,dic1[tissue][1]+shift]
    for k,v in dic1.items():
        lis_v = []
        for i in v:
            lis_v.append(str(i))
        b = "\t".join(lis_v)
        fo.write("\t".join([str(k),b])+"\n")
main(sys.argv[1],sys.argv[2])
