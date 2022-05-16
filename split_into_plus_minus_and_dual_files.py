#!/usr/bin/python
import sys

inFile = open(sys.argv[1], "r")
gene = inFile.readline().strip()
lineListDict = dict()
while gene:                                                                                                                                                    
    seq = inFile.readline()                                                                                                                                   
    starts_string = inFile.readline()                                                                                                                          
    current_gene = gene                                                                                                                                        
    gene = inFile.readline().strip()                                                                                                                           
    lineList = [int(x) for x in starts_string.strip()[:-1].split(",")] 
    lineListDict[current_gene] = lineList
inFile = open(sys.argv[2], "r")
genePDict = dict()
geneShiftStartDict = dict()
geneShiftEndDict = dict()
genePercent = dict()
geneBeforePvalue = dict()
geneNumReads = dict()
geneDirection = dict()
genePlusOne = dict()
geneMinusOne = dict()
geneDualPlusOne = dict()
geneDualMinusOne = dict()

for line in inFile:
    Info_string = line.strip()
    letters = inFile.readline().rstrip("\n").split(" ")
    reads_1 = inFile.readline().rstrip("\n").split(" ")
    reads_2 = inFile.readline().rstrip("\n").split(" ")
    percents = inFile.readline().rstrip("\n").split(",")
    blank = inFile.readline()
    gene_name = Info_string.split("\t")[0].split(" ")[1]
    p_value  = float(Info_string.split("\t")[1].split(" ")[1])

    
    detected_shift = int(Info_string.split("\t")[3].split(" ")[1])
    detected_shift_end = detected_shift + int(Info_string.split("\t")[4].split(" ")[1])
    
    geneDirection[gene_name] = Info_string.split("\t")[5].split(" ")[1]
    if ( Info_string.split("\t")[6].split(" ")[1] == "no" ):
        if (geneDirection[gene_name] == "plus"):
            genePlusOne[gene_name] = "yes"
        else:
            geneMinusOne[gene_name] = "yes"
    else:
        if (geneDirection[gene_name] == "plus"):
            geneDualPlusOne[gene_name] = "yes"
        else:
            geneDualMinusOne[gene_name] = "yes"
    genePercent[gene_name] = float(Info_string.split("\t")[7].split(" ")[1])
    
    geneNumReads[gene_name] = float(Info_string.split("\t")[8].split(" ")[1])
    geneBeforePvalue[gene_name] = float(Info_string.split("\t")[9].split(" ")[1])

    genePDict[gene_name] = p_value
    geneShiftStartDict[gene_name] = detected_shift
    geneShiftEndDict[gene_name] = detected_shift_end
    
sorted_PVals = sorted(genePDict.items(), key=lambda x: x[1])
    
outFile = open(sys.argv[3], "w")
outFile2 = open(sys.argv[4], "w")
outFile3 = open(sys.argv[5], "w")

outFile.write("gene,gene_shift_start,gene_shift_end,p_value,percent_shifted,num_reads\n")
outFile2.write("gene,gene_shift_start,gene_shift_end,p_value,percent_shifted,num_reads\n")
outFile3.write("gene,gene_shift_end,p_value,percent_shifted,num_reads,direction_of_shift\n")
for (gene, p_val) in sorted_PVals:
    if gene in genePlusOne:
        outFile.write(gene + "," + str(geneShiftStartDict[gene]) + "," + str(geneShiftEndDict[gene]) + ",10^" + str(round(p_val)) + "," + str(round(genePercent[gene],2)) + "," + str(geneNumReads[gene]) +  "\n")
    if gene in geneMinusOne:
        outFile2.write(gene + "," + str(geneShiftStartDict[gene]) + "," + str(geneShiftEndDict[gene]) + ",10^" + str(round(p_val)) + "," + str(round(genePercent[gene],2)) + "," + str(geneNumReads[gene]) + "\n")
    if gene in geneDualPlusOne:
        outFile3.write(gene + "," + str(geneShiftEndDict[gene]) + ",10^" + str(round(p_val)) + "," + str(round(genePercent[gene],2)) + "," + str(geneNumReads[gene]) + ",plus\n")
    if gene in geneDualMinusOne:
        outFile3.write(gene + "," + str(geneShiftEndDict[gene]) + ",10^" + str(round(p_val)) + "," + str(round(genePercent[gene],2)) + "," + str(geneNumReads[gene]) + ",minus\n")
