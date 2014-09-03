#!/bin/bash

#
# Day 1 - Homework: Part 2 - debug this bash script
#

echo "There are around 6 mistakes"

# navigate to folder with fastq data
FASTQ_DIR=/Users/cmdb/data/fastq
# navigate to folder to put output data in
OUTPUT_DIR=/Users/cmdb/data/day1
# common prefix to all data runs
SAMPLE_PREFIX=SRR072

# navigate to folder with genome data in it
GENOME_DIR=/Users/cmdb/data/genomes
GENOME_FILE=dmel-all-chromosome-r5.57 
ANNOTATION=dmel-all-r5.57.gff

CORES=4

for i in {893..916} # run for each sequence
do
  echo fastqc $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
  echo tophat -p $CORES -G $OUTPUT_DIR/$ANNOTATION -o $OUTPUT_DIR/th_$i --no-novel-juncs --segment-length 20 $GENOME_DIR/$GENOME_FILE $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq
  echo cufflinks -p $CORES -G $GENOME_DIR/$GENOME_FILE -o $OUTPUT_DIR $OUTPUT_DIR/accepted_hits.bam
done