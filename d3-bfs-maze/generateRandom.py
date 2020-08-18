#!/usr/bin/python

import sys, getopt
import random

def main(argv):
    outputfile = ''
    numnodes = 10
    degree = 2
    locality = 10 
    try:
        opts, args = getopt.getopt(argv,"h:o:n:d:l",["ofile=", "nodes=", "degree=", "locality="])
    except getopt.GetoptError:
        print 'generateRandom.py -o <outputfile> --nodes=<number of nodes> --degree=<degree of the graph> --locality=<how close are connections to each other>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'generateRandom.py -o <outputfile> --nodes=<number of nodes> --degree=<degree of the graph> --locality=<how close are connections to each other>'
            sys.exit()
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-n", "--nodes"):
            numnodes = int(arg)
        elif opt in ("-d", "--degree"):
            degree = int(arg)
        elif opt in ("-l", "--locality"):
            locality = int(arg)

    nodes=[]
    links=[]

    # populate the nodes
    current_id = 0
    for i in range(numnodes):
        nodes.append(current_id)
        current_id = current_id + 1

    for n in nodes:
        for d in range(degree):
            target_dist = random.randint(-locality, locality)
            target = (n + target_dist) % numnodes
            connection = [n, target]
            links.append(connection)

    # render the JSON
    out = open(outputfile, "w")
    out.write("{\n")
    
    # render nodes 
    nodestr = "\"nodes\" : [" 
    for n in nodes:
        nodestr += "\n{ \"id\": "+str(n)+", \"name\": \"node"+str(n)+"\"},"
    nodestr = nodestr[:-1] # remove the final comma
    nodestr += "\n]," 
    out.write(nodestr)

    # render links
    linkstr = "\"links\" : ["
    for l in links:
        linkstr += "\n{ \"source\": "+str(l[0])+", \"target\": "+str(l[1])+"},"
    linkstr = linkstr[:-1]
    linkstr += "\n]" 
    out.write(linkstr)

    out.write("}\n");
    out.close()

if __name__ == "__main__":
    main(sys.argv[1:])
