#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import sys
import numpy as np
import argparse
from collections import defaultdict

#deepfile = sys.argv[1]

def filter_PosDep(fileIn, n, outF):
    filtered_D = defaultdict(dict)

    resD = defaultdict(dict)

    outHandle = open(outF, "w")
    handleIn = open(fileIn, "r")
    for line in handleIn:
        XL = line.strip().split("\t")
        chrName = XL[0]
        pos     = int(XL[1])
        dep     = int(XL[2])
        if dep >= n:
            filtered_D[chrName][pos] = dep
    handleIn.close()
    
    for testChr in filtered_D:
        testDict = filtered_D[testChr]
        sortD1 = sorted(testDict.items(), key=lambda d: d[0])

        tmpPosEnd = set()
        for k,v in sortD1:
            KL = list(range(k+1, k+201))
            if all([mk not in testDict for mk in KL]):
                #print(testChr, k)
                tmpPosEnd.add(k)

        for i in tmpPosEnd:
            for j in range(i-1500, i):
                if j in testDict:
                    outHandle.write("{0}\t{1}\t{2}\n".format(testChr, j, i))

                    resD[testChr][j]=i-j
                    break            
    outHandle.close()
    return resD


if __name__ == "__main__":
    USAGE = """python {0} -i input_file
                        -m minimal depth
                        -o outputFile""".format(__file__)

    parser = argparse.ArgumentParser(description = USAGE)
    parser.add_argument("-i", "--inputDep", action = "store", required = True, help = "deepfile generated by samtools depth")
    parser.add_argument("-o", "--output", action = "store", default="res1.txt", help = "resultfile ")
    parser.add_argument("-m", "--minD", action = "store", type=int, help = "minimal standard for depth filtration")

    args = parser.parse_args()

    ## python calc_Depth_Structure.py -i Test_N49.deep -m 100
    ## minimal depth for filtration is 100,
    #  min gap length without depth is 200,
    #  maximal distance of start pos for depth detection is 1500
    outD = filter_PosDep(args.inputDep, args.minD, args.output )

    for c in outD:
        dchr = outD[c]
        for p in dchr:
            if dchr[p] > 50:
                print(c, p, dchr[p])
