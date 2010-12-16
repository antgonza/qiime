#!/usr/bin/env python
# File created Sept 29, 2010
from __future__ import division

__author__ = "William Walters"
__copyright__ = "Copyright 2010, The QIIME project"
__credits__ = ["William Walters"]
__license__ = "GPL"
__version__ = "1.2.0-dev"
__maintainer__ = "William Walters"
__email__ = "William.A.Walters@colorado.edu"
__status__ = "Development"
 
from optparse import make_option

from qiime.util import parse_command_line_parameters, get_options_lookup
from qiime.quality_scores_plot import generate_histogram
from qiime.util import create_dir


options_lookup = get_options_lookup()

script_info={}
script_info['brief_description']="""Generates histograms of sequence quality scores and number of nucleotides recorded at a particular index"""
script_info['script_description']="""Two plots are generated by this module.  
The first shows line plots indicating the average and standard deviations
for the quality scores of the input quality score file, 
starting with the first nucleotide and ending with the the final 
nucleotide of the largest sequence.

A second histogram shows a line plot with the nucleotide count for each
position, so that one may easily visualize how sequence length drops off.

A dotted line shows the cut-off point for a score to be acceptable (default
is 25).

An text file logging the average, standard deviation, and base count 
for each base position is also generated.  These three sections are comma 
separated.

The truncate_fasta_qual_files.py module can be used to create truncated
versions of the input fasta and quality score files.  By using this module
to assess the beginning of poor quality base calls, one can determine 
the base position to begin truncating sequences at."""
script_info['script_usage']=[]
script_info['script_usage'].append(("""Example:""","""Generate plots and output to the quality_histograms folder""","""quality_score_plot.py -q seqs.qual -o quality_histograms/"""))
script_info['output_description']="""A .pdf file with the two plots will be created in the output directory"""
script_info['required_options']= [\
      
    make_option('-q', '--qual_fp',
        help='Quality score file used to generate histogram data.')
]

script_info['optional_options']= [\
    make_option('-o', '--output_dir',
        help='Output directory.  Will be created if does not exist.  '+\
        '[default: %default]', default="."),
        
    make_option('-s', '--score_min',
        help='Minimum quality score to be considered acceptable.  Used to '+\
        'draw dotted line on histogram for easy visualization of poor '+\
        'quality scores. [default: %default]', default=25, ),
        
    make_option('-v', '--verbose',
        action='store_false', default=True,
        help='Turn on this flag to disable verbose output. '+\
        ' [default: %default]')]
        
script_info['version'] = __version__

def main():
    option_parser, opts, args =\
     parse_command_line_parameters(suppress_verbose=True, **script_info)
      
    qual_fp = opts.qual_fp
    output_dir = opts.output_dir
    score_min = int(opts.score_min)
    verbose = opts.verbose
    
    create_dir(output_dir)
    
    generate_histogram(qual_fp, output_dir, score_min, verbose)
    


if __name__ == "__main__":
    main()
