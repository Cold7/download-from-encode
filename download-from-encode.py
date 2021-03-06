import requests, json, collections
import argparse 
from os import mkdir
import multiprocessing as mp

########################################################################
##
## Function that download data
## this function take a link, this check if there exist the minium
## replicates, if it are in an adecuated condition (chemical treatments
## genetic modifications and cell cicle), pipeline completed, released
## and  genome version. if it pass all conditions final results will be
## downloaded
##
########################################################################
def download(link):
	print "under construction. But remember, we need to do a while condition to avoid error in json response"
	
########################################################################
##
## Input parameters
##
########################################################################

parser = argparse.ArgumentParser()

#general options
parser.add_argument("-c", "--cell_line", help="Cell line to download experimental results from the Encode platform", store=True)
parser.add_argument("-oc","--open_chr", help="Download associated data to open chromatine (values: True / False; default: True)")
parser.add_argument("-md", "--meth_dna", help="Download associated data to DNA methylation (values: True / False; default: True)")
parser.add_argument("-tf", "--transcription_factores", help="Download associated data to TFs (values: True / False; default: True)")
parser.add_argument("-hm", "--histone_mod", help="Download associated data to histone modification (values: True / False; default: True)")
parser.add_argument("-g", "--gene_expr", help="Download associated data to gene expression (values: True / False; default: True)")
parser.add_argument("-l", "--loops", help="Download associated data to DNA loops (values: True / False; default: True)")
parser.add_argument("-n", "--nproc", help="Number of processors to use (default: "+multiprocessing.cpu_count()+")", store = True, default = multiprocessing.cpu_count() , type=int)
parser.add_argument("-o","--output", help="Output path to make a tree of characteristics and then download data")

#specific options
parser.add_argument("-r", "--replicas", help="Number of min. number of replicates for each experiment (default: 2)", store = True, default = 2, type=int)
parser.add_argument("-gv", "--genome_version", help="Options: hg19 or GRCh38 (default: GRCh38)", store = True, default = "GRCh38")
parser.add_argument("-t", "--treatment", help="Options: yes or not (default: not)", store = True, default = "not")
parser.add_argument("-gm", "--genetic_modifications", help="Options: yes or not (default: not)", store = True, default = "not")
parser.add_argument("-cc", "--cell_cicle", help="Options: G1, G2 or none (default: none)", store = True, default = "none")








args = parser.parse_args()

########################################################################
##
## Defining global variables for use in each processor
##
########################################################################

global output, replicas, cell_line
output = args.output
replicas = args.replicas
cell_line = args.cell_line

#######################################################################
##
## Definition for each characteristic (using encode experiment names)
##
########################################################################

open_chrom = ["FAIRE-seq", "ATAC-seq", "DNase-seq", "MNase-seq"]
meth_dna = ["MRE-seq", "TAB-seq", "WGBS"]
chipseq = ["ChIP-seq"]
expression = ["polyA RNA-seq","total RNA-seq"]
loops = ["ChIA-PET", "Hi-C", "5C"]

total = open_chrom + meth_dna + chipseq + expression + loops
#calling multiprocess to download data in a parallel fashion
pool=mp.Pool(processes=args.nproc) #for multiprocessing
#pool.map(download_data,(cell_lines))
