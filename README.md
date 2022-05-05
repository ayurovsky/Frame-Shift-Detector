# Frame-Shift-Detector

# Introduction

This README contains the instructions for running the frameshift detector and helper scripts to aid in generating new input files

# Section 1. Running the Frameshift Detector #

## 1.1 The Starts File

An example file is included: starts_combined_dataset_above_90.txt

The expected format for this input file is three lines for each gene:&nbsp;&nbsp;&nbsp;
Gene Name&nbsp;&nbsp;&nbsp;
Gene Nucletide Sequence&nbsp;&nbsp;&nbsp;
A comma separated list of integers, corresponding to the the number of ribosome profiling fragment starts at each nucleotide of the gene

Section 3 will describe the process of generating the starts file 

## 1.2 Get genome-wide proportions of starts in frame 1 vs. frame 2 + frame 3

Get the p (f2 + f3 proportion) and q (f1 proportion) values from the starts file 

An example run:&nbsp;&nbsp;&nbsp;
python get_mean_and_std_f1.py starts_combined_dataset_above_90.txt

will give the following output:&nbsp;&nbsp;&nbsp;
F1 mean with statistics is 0.8763924094763768&nbsp;&nbsp;&nbsp;
F1 stdev with statistics is 0.22906614440659637&nbsp;&nbsp;&nbsp;
Total f1 is 0.914418446440859&nbsp;&nbsp;&nbsp;
Total f2 is 0.04545015288643027&nbsp;&nbsp;&nbsp;
Total is: 48066725&nbsp;&nbsp;&nbsp;

q here is 0.914, and p is (1-0.914) = 0.086

these values should be entered at the top of the frame_shift_detector.py file, see section 1.3. 

## 1.3 
