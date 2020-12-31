import csv

short_paths = []
with open('wikispeedia_paths-and-graph/shortest-path-distance-matrix.txt') as spdm:
    for ele in spdm.readlines()[17:]:
        short_paths.append(ele[:-1])

edges = []
for i in range(len(short_paths)):
    for j in range(len(short_paths[0])):
        if short_paths[i][j] == '1':
            edges.append(['A'+"{0:0=4d}".format(i+1),'A'+"{0:0=4d}".format(j+1)])

with open('edges.csv','w',newline='')  as fp_edge:
    writer = csv.writer(fp_edge)
    writer.writerows(edges)