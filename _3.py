# Author: shunkai 
# Date: 2021-02-20 20:14:54 
# Last Modified by:   shunkai 
# Last Modified time: 2021-02-20 20:14:54  
# describe: 按照组织和表达量连接在一起

import sys 


def main(filein,filein2,fileout) : 
    f1 = open(filein,"r")        # all_codon_shift2/out2_all_origin_shift_gene_info.txt
    f2 = open(filein2,"r")       # tissue.txt
    fo = open(fileout,"w")       # all_codon_shift2/out3_all_origin_gene_tissue_info.txt
    dic_tissue = {}
    for lin in f2 :
        if lin.startswith("Run"):
            continue
        else:
            seq1 = lin.split("\t")
            sampleName = seq1[2]
            tissues = seq1[5]
            if sampleName not in dic_tissue.keys():
                dic_tissue[sampleName] = []
                dic_tissue[sampleName].append(tissues)
            else:
                dic_tissue[sampleName].append(tissues)  
    for line in f1 :
        for k,v in dic_tissue.items():
            seq = line.strip().split("\t")
            if seq[0] == k :
                fo.write("\t".join([seq[0],seq[1],seq[2],v[0],"\n"+\
                    seq[0],seq[1],seq[3],v[1],"\n"+\
                    seq[0],seq[1],seq[4],v[2],"\n"+\
                    seq[0],seq[1],seq[5],v[3],"\n"+\
                    seq[0],seq[1],seq[6],v[4],"\n"+\
                    seq[0],seq[1],seq[7],v[5],"\n"+\
                    seq[0],seq[1],seq[8],v[6],"\n"+\
                    seq[0],seq[1],seq[9],v[7],"\n"+\
                    seq[0],seq[1],seq[10],v[8],"\n"+\
                    seq[0],seq[1],seq[11],v[9],"\n"]))
            else:
                continue

main(sys.argv[1],sys.argv[2],sys.argv[3])
