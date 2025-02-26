import argparse
import numpy
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

def plot_karyo(bins, outfile):
    plt.clf()
    plt.figure(figsize=(20,4), dpi=100)
    chr_locs = []
    x = 0
    for c in bins:
        med = numpy.median(bins[c])
        plt.scatter([x+i for i in range(len(bins[c])) if bins[c][i] != 2**16-1], [b for b in bins[c] if b != 2**16-1], color="blue", marker='.')
        plt.plot([x, x+len(bins[c])-1],[med,med], color="red", linestyle="solid", linewidth=3)
        chr_locs.append(x+len(bins[c])/2)
        x += len(bins[c])
        plt.plot([x+5, x+5], [0, 2**16-1], color="black")
        x += 10
    ymax = numpy.percentile(numpy.concatenate([bins[c] for c in bins]), 99.9)
    plt.xticks(chr_locs, [c for c in bins], rotation='vertical')
    plt.ylim((0,ymax))
    plt.xlim((0,x-10))
    plt.xlabel("Chromosome")
    plt.ylabel("Reads per Mbp")
    plt.title("Karyotype")
    plt.tight_layout()
    plt.savefig(outfile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Draw digital karyotype from coverage bins")
    parser.add_argument("tsv", help="Coverage TSV file")
    parser.add_argument("out", help="Output image file")
    args = parser.parse_args()

    # expect TSV coverage bins format:
    '''
chromosome	bin_start	bin_end	n_reads
chr1	0	1000000	1389
chr1	1000000	2000000	744
chr1	2000000	3000000	794
    '''
    bins = {}
    chr_lens = {}
    for line in open(args.tsv):
        fields = line.strip().split('\t')
        if fields[0] == "chromosome": # header
            continue
        if fields[0] not in bins:
            bins[fields[0]] = []
            chr_lens[fields[0]] = int(fields[2])
        bins[fields[0]].append(int(fields[3]))
        if int(fields[2]) > chr_lens[fields[0]]:
            chr_lens[fields[0]] = int(fields[2])

    plot_karyo({c:numpy.array(bins[c]) for c in bins}, args.out)
