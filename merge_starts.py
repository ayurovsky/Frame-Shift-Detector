#!/usr/bin/python

infiles = ["all_jan2014_bowtie_28_starts", "Wu2019_bowtie_unique_28_29_starts", "Guydosh2014_bowtie_unique_28_29_starts", "Young2015_bowtie_unique_28_starts"]
outFile = open("combined_starts_four_sets_above_90", "w")
seq_dict = dict()
starts_dict = dict()
for f in infiles:
	inFile = open(f, "r")
	gene = inFile.readline().strip()
	while gene:
		seq = inFile.readline()
		starts_string = inFile.readline()
		current_gene = gene
		gene = inFile.readline().strip()

		ss = starts_string.strip()[:-1].split(",")
		if (current_gene not in seq_dict):
			seq_dict[current_gene] = seq
			starts_dict[current_gene] = ss
		else:
			new_starts = [int(starts_dict[current_gene][i]) + int(ss[i]) for i in range(len(ss))]
			starts_dict[current_gene] = new_starts
	inFile.close()
for gene in seq_dict:
	outString = gene + "\n"
	outString += seq_dict[gene] 
	outString += ",".join([str(x) for x in starts_dict[gene]]) + ",\n"
	outFile.write(outString)
outFile.close()
