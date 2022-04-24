import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

#                นอน,ตั้ง
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)
G.add_node(9)
G.add_node(10)
G.add_node(11)
G.add_node(12)
G.add_node(13)
G.add_node(14)
G.add_node(15)
G.add_node(16)
G.add_node(17)
G.add_node(18)
G.add_node(19)
G.add_node(20)

# สถานที่ท่องเที่ยว
#18
G.add_edge(18, 19, weight=0.140)
G.add_edge(18, 13, weight=7.1)
#19
G.add_edge(19, 1, weight=0.8)
G.add_edge(19, 13, weight=7.7)
G.add_edge(19, 3, weight=1.9)
G.add_edge(19, 18, weight=0.140)
G.add_edge(19, 17, weight=1)
#17
G.add_edge(17, 19, weight=1)
G.add_edge(17, 13, weight=6.1)

#13
G.add_edge(13, 18, weight=7.1)
G.add_edge(13, 19, weight=0.1)
G.add_edge(13, 12, weight=1.7)
G.add_edge(13, 14, weight=3.2)
G.add_edge(13, 17, weight=6.1)

#14
G.add_edge(14, 12, weight=2.1)
G.add_edge(14, 15, weight=3.5)
G.add_edge(14, 13, weight=3.2)
#15
G.add_edge(15, 12, weight=1.9)
G.add_edge(15, 14, weight=3.5)
G.add_edge(15, 16, weight=0.240)
#16
G.add_edge(16, 15, weight=0.240)
G.add_edge(16, 10, weight=1.9)
G.add_edge(16, 12, weight=3)
#12
G.add_edge(12, 16, weight=1.9)
G.add_edge(12, 15, weight=1.9)
G.add_edge(12, 14, weight=2.1)
G.add_edge(12, 13, weight=1.7)
G.add_edge(12, 10, weight=1.6)
G.add_edge(12, 11, weight=1.6)
#10
G.add_edge(10, 16, weight=3)
G.add_edge(10, 12, weight=1.6)
G.add_edge(10, 11, weight=0.170)
G.add_edge(10, 5, weight=2.4)
#11
G.add_edge(11, 12, weight=1.6)
G.add_edge(11, 10, weight=0.170)
#5
G.add_edge(5, 10, weight=2.4)
G.add_edge(5, 6, weight=0.950)
G.add_edge(5, 4, weight=0.5)
#4
G.add_edge(4, 5, weight=0.5)
G.add_edge(4, 3, weight=2.2)
#6
G.add_edge(6, 5, weight=0.950)
G.add_edge(6, 8, weight=0.1)
G.add_edge(6, 9, weight=1.3)
#8
G.add_edge(8, 6, weight=0.1)
G.add_edge(8, 7, weight=0.14)
G.add_edge(8, 9, weight=1.4)
#7
G.add_edge(7, 8, weight=0.14)
G.add_edge(7, 9, weight=1.4)
#9
G.add_edge(9, 6, weight=1.3)
G.add_edge(9, 7, weight=1.4)
G.add_edge(9, 8, weight=1.4)
G.add_edge(9, 3, weight=1.4)
G.add_edge(9, 20, weight=1.6)
#3
G.add_edge(3, 2, weight=0.500)
G.add_edge(3, 9, weight=1.4)
G.add_edge(3, 4, weight=2.2)
G.add_edge(3, 19, weight=1.9)
#2
G.add_edge(2, 3, weight=0.500)
G.add_edge(2, 1, weight=0.350,pos=(50,10))
#1
G.add_edge(1, 2, weight=0.350)
G.add_edge(1, 19, weight=0.800)
G.add_edge(1, 20, weight=3.5)
#20
G.add_edge(20, 1, weight=3.5)
G.add_edge(20, 9, weight=1.6)

location1 = int(input('\tChoose your location 1 : '))
location2 = int(input('\tChoose your location 2 : '))
location3 = int(input('\tChoose your location 3 : '))
location4 = int(input('\tChoose your location 4 : '))
location5 = int(input('\tChoose your location 5 : '))

g = (nx.shortest_path_length(G,source=location1,target=location2 and location3 and location4 and location5,weight='weight'))
a1 = (nx.shortest_path(G,source=location1,target=location2,weight='weight'))
a4 = (nx.shortest_path(G,source=location2,target=location3,weight='weight'))
a9 = (nx.shortest_path(G,source=location3,target=location4,weight='weight'))
a13 = (nx.shortest_path(G,source=location4,target=location5,weight='weight'))

A = g+h+i+w

list1 = [A]
        
if min(list1) == A:
    print('Shortest path from ',location1 ,'to',location5 ,'is',a1+a4+a9+a13)

    print('The distance is  : %.0f'%(A),"km")
    x = nx.shortest_path(G,source=location1,target=location5,weight='weight')

    d = nx.shortest_path_length(G,source=location1,target=location5,weight='weight')
    DD = []
    i = 0

    while i < len(G):
        z = i+1
        if z in x:
            DD.append('blue')
        else:
            DD.append('yellow')
        i = i + 1
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        nx.draw(G, pos,node_color=DD, with_labels=True,node_size= 500)
        plt.show()

DD = []
PP = []
i = 0

while i < len(G):
    z = i+1
    if z in x:
        DD.append('red')
    else:
        DD.append('blue')
        
    i = i + 1


nx.draw(G, pos,node_color=DD, with_labels=True,node_size= 500)

plt.show()