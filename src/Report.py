import networkx as nx
from statistics import mean, variance
import json
import csv

index = ['', 'mean_degree', 'degree_variance', 'density', 'radius_by_hops', 'diameter_by_hops', 'min_length', 'max_length', 'radius_by_length', 'diameter_by_length', 'total_data_rate', 'blocking_coefficient']

def meanDegree(eon, degrees=None):
    if degrees is None:
        degrees = nx.degree(eon)
    degrees = [d[1] for d in degrees]
    return mean(degrees)

def degreeVariance(eon, degrees=None):
    if degrees is None:
        degrees = nx.degree(eon)
    degrees = [d[1] for d in degrees]
    return variance(degrees)

def getIdOrCreateCSV(csv_name, folder=''):
    results_csv = folder + csv_name + '.csv'
    numRows = 0
    try:
        with open(results_csv, 'r') as file:
            fileReader = csv.reader(file, delimiter=' ', quotechar='|')
            for row in fileReader:
                if row[0] not in (None, ""):
                    numRows += 1
        file.close()

        if numRows==0:
            raise IndexError
    except:
        with open(results_csv, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=index)
            writer.writeheader()
            numRows += 1
        file.close()
    return numRows-1

def writeCSV(eon, demands, csv_name, id=None, folder=''):
    data = CSVdata(eon, demands, id=id)

    if data is not None:
        results_csv = folder + csv_name + '.csv'
        with open(results_csv, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=index)
            writer.writerow(data)
        file.close()
        
def CSVdata(eon, demands, id=None):
    try:
        lengths = list(nx.get_edge_attributes(eon, 'length').values())
        degrees = nx.degree(eon)
        demands_report = fromDemands(demands)
        ecc_by_length = nx.eccentricity(eon, sp=dict(nx.all_pairs_dijkstra_path_length(eon, weight='length')))

        data = {
            '': id,
            'mean_degree': meanDegree(eon, degrees=degrees),
            'degree_variance': degreeVariance(eon, degrees=degrees),
            'density': nx.density(eon),
            'radius_by_hops': nx.radius(eon),
            'diameter_by_hops': nx.diameter(eon),
            'min_length': min(lengths),
            'max_length': max(lengths),
            'radius_by_length': nx.radius(eon, e=ecc_by_length),
            'diameter_by_length': nx.diameter(eon, e=ecc_by_length),
            'total_data_rate': demands_report['total_data_rate'], 
            'blocking_coefficient': demands_report['blocking_coefficient']
        }

        return data
    except:
        return None

def fromDemands(demands):
    total_data_rate = 0
    unexecuted = 0
    successes = 0
    blocks = 0
    n_demands = 0
    for demand in demands:
        n_demands += 1
        if demand.status is None:
            unexecuted += 1
        elif demand.status is True:
            successes += 1
            total_data_rate += demand.data_rate
        else:
            blocks += 1
    return {
        'total_data_rate': total_data_rate,
        'unexecuted': unexecuted,
        'successes': successes,
        'blocks': blocks,
        'unexecuted_rate': unexecuted / n_demands if n_demands > 0 else None,
        'success_rate': successes / n_demands  if n_demands > 0 else None,
        'blocking_coefficient': blocks / n_demands if n_demands > 0 else None,
    }