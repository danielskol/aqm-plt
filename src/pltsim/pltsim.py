'''
Documentation, License etc.

@package pltsim
'''

import argparse
from simulation import simulate

def parseArgs():
    argParser = argparse.ArgumentParser(description = "Simpulate TCP and AQM algorithms on arbitary topology.")
    argParser.add_argument("-c", "--capacity", type = int, default = 100, help = "capacity of all links in packets per second")
    argParser.add_argument("-t", "--tcp", required = True, choices = ["Reno"], help = "tcp algorithm name")
    argParser.add_argument("-a", "--aqm", required = True, choices = ["RED", "CoDel"], help = "aqm algorithm name")
    argParser.add_argument("-r", "--routes", required = True, type = argparse.FileType('r'),
                           help = "file with flow routes\neach line has a chain of routers indexes, which represents a flow")
    argParser.add_argument("-o", "--output", required = True, type = argparse.FileType('w'),
                           help = "output file, where NS3 stores its log after execution")
    return argParser.parse_args()

def parseRoutes(routesFile):
    routes = []
    for line in routesFile:
        routes.append([int(routerIndex) for routerIndex in line.strip().split(' ')])
    return routes
    
if __name__ == "__main__":
    args = parseArgs()
    args.routes = parseRoutes(args.routes)
    simulate(args.routes, args.tcp, args.aqm, args.capacity, args.output)
