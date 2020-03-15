
'''
Registration Number,Model,Type,Start Time,End Time,Distance,Duration,Departure Point,Arrival Point,Comment
BS27ZBGP,SUZUKI JIMNY 1.3 2012,personal,2018-03-01 05:56:50,2018-03-01 06:01:17,1.8,0:04:27,"-26.1577709802, 28.0154520043","-26.1424196012, 28.016816411",

0 Registration Number,
1 Model,
2 Type,
3 Start Time,
4 End Time,
5 Distance,
6 Duration,
7 Departure Point,
8 Arrival Point,
9 Comment
'''

source_file_path = 'data/trip_report.csv'

def parse(line):
    
    v = line.split(',')
    
    try:
        return {
            "startTime": v[3],
            "endTime": v[4],
            "distance": v[5],
            "duration": v[6],
            "from": v[7],
            "to": v[8]
        }
    except:
        return None

lines = []

with open(source_file_path, 'r') as source_file:
    lines = source_file.read().split('\n')

print(len(lines))

parsed = [x for x in [parse(line) for line in lines][1:] if x is not None]

print([parsed[0]])