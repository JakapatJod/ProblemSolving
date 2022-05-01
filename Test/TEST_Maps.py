import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

#             
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
G.add_edge(2, 3, weight=0.500,pos=(50,10))
G.add_edge(2, 1, weight=0.350,pos=(50,10))
#1
G.add_edge(1, 2, weight=0.350)
G.add_edge(1, 19, weight=0.800)
G.add_edge(1, 20, weight=3.5)
#20
G.add_edge(20, 1, weight=3.5)
G.add_edge(20, 9, weight=1.6)

pos = nx.spring_layout(G) #วาดกกราฟ
labels = nx.get_edge_attributes(G,'weight')

again = 'y'
while again == 'y' :
    print('-'*10,'Phitsanulok tourist attraction','-'*10,)
    print('')
    print('\t\t1.Show Map')
    print('\t\t2.Travel 2-5 location')
    print('\t\t3.Present Program')
    print('')
    op = int(input('\t\tEnter the chioce : '))
    print('-'*51)

    if op == 1: # Show Map
        edge_labels = nx.get_edge_attributes(G, 'weight')
        pos = nx.spring_layout(G)  #วาดกกราฟ
        plt.figure(8,figsize=(20,20))
        nx.draw(G,pos, with_labels=True,font_color= 'yellow',node_size= 500)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
        plt.show()
        
    if op == 2: # Travel 5 location
      
        print('')
        T = int(input('Please select 2 - 5 places you want to go : '))
        print('')
        if T == 3:
          location1 = int(input('\tChoose your location 1 : '))
          location2 = int(input('\tChoose your location 2 : '))
          location3 = int(input('\tChoose your location 3 : '))
          g = (nx.shortest_path_length(G,source=location1,target=location2,weight='weight'))
          h = (nx.shortest_path_length(G,source=location2,target=location3,weight='weight'))
          a1 = (nx.shortest_path(G,source=location1,target=location2,weight='weight'))
          a4 = (nx.shortest_path(G,source=location2,target=location3,weight='weight'))    
          AB = g+h # ระยะทางทั้งหมด
          B1 = a1 + a4 # เส้นทาง

          list1 = [AB]

          POP = [] # remove duplicate
          for i in B1:
            if i not in POP:
                POP.append(i)

          if min(list1) == AB:
            print('\tShortest path from ',location1 ,'to',location3 ,'is',POP)

          print('\tThe distance is  : %.2f'%(AB),"km")
          
          DD = []
          i = 0

          while i < len(G):
            z = i+1
            if z in POP:
              DD.append('blue')
            else:
              DD.append('yellow')
            i = i + 1
          nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
          nx.draw(G, pos,node_color=DD, with_labels=True,node_size= 500)

          plt.show()

        if T == 4:
          location1 = int(input('\tChoose your location 1 : '))
          location2 = int(input('\tChoose your location 2 : '))
          location3 = int(input('\tChoose your location 3 : '))
          location4 = int(input('\tChoose your location 4 : '))
          g = (nx.shortest_path_length(G,source=location1,target=location2,weight='weight'))
          h = (nx.shortest_path_length(G,source=location2,target=location3,weight='weight'))
          i = (nx.shortest_path_length(G,source=location3,target=location4,weight='weight'))
          a1 = (nx.shortest_path(G,source=location1,target=location2,weight='weight'))
          a4 = (nx.shortest_path(G,source=location2,target=location3,weight='weight'))
          a9 = (nx.shortest_path(G,source=location3,target=location4,weight='weight'))

          ABC = g+h+i # ระยะทางทั้งหมด
          B2 = a1 +a4 +a9 # เส้นทาง

          list1 = [ABC]

          POP2 = []
          for i in B2: # remove duplicate
            if i not in POP2:
                POP2.append(i)

          if min(list1) == ABC:
            print('\tShortest path from ',location1 ,'to',location4 ,'is',POP2)

          print('\tThe distance is  : %.2f'%(ABC),"km")
         
          DD = []
          i = 0

          while i < len(G):
            z = i+1
            if z in POP2:
              DD.append('blue')
            else:
              DD.append('yellow')
            i = i + 1
          nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
          nx.draw(G, pos,node_color=DD, with_labels=True,node_size= 500)

          plt.show()

        if T == 5:

          location1 = int(input('\tChoose your location 1 : '))
          location2 = int(input('\tChoose your location 2 : '))
          location3 = int(input('\tChoose your location 3 : '))
          location4 = int(input('\tChoose your location 4 : '))
          location5 = int(input('\tChoose your location 5 : '))

          g = (nx.shortest_path_length(G,source=location1,target=location2,weight='weight'))
          h = (nx.shortest_path_length(G,source=location2,target=location3,weight='weight'))
          i = (nx.shortest_path_length(G,source=location3,target=location4,weight='weight'))
          w = (nx.shortest_path_length(G,source=location4,target=location5,weight='weight'))

          a1 = (nx.shortest_path(G,source=location1,target=location2,weight='weight'))
          a4 = (nx.shortest_path(G,source=location2,target=location3,weight='weight'))
          a9 = (nx.shortest_path(G,source=location3,target=location4,weight='weight'))
          a13 = (nx.shortest_path(G,source=location4,target=location5,weight='weight'))

          V = g+h+i+w # ระยะทางทั้งหมด
          B3 = a1+a4+a9+a13 # เส้นทาง

          list1 = [V]
          POP3 = []
          
          for i in B3: # remove duplicate
            if i not in POP3:
                POP3.append(i)
          if min(list1) == V:
            print('\tShortest path from ',location1 ,'to',location5 ,'is',POP3)

          print('\tThe distance is  : %.2f'%(V),"km")
         
          DD = []
          i = 0

          while i < len(G):
            z = i+1
            if z in POP3:
              DD.append('blue')
            else:
              DD.append('yellow')
            i = i + 1
          nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
          nx.draw(G, pos,node_color=DD, with_labels=True,node_size= 500)
          plt.show()

    if op == 3: # Present Program
        print('')
        location1 = int(input('\tChoose your location : '))
        location2 = int(input("\tWhere do you want to go :  "))
        print('')
        print('\tShortest path from ',location1 ,'to',location2 ,'is',nx.shortest_path(G,source=location1,
        target=location2,weight='weight'))

        x = nx.shortest_path(G,source=location1,target=location2,weight='weight')
        dc = nx.shortest_path_length(G,source=location1,target=location2,weight='weight')
        print('')
        print('The distance is  : %.2f'%(dc),"km")


        DD = []
        PP = []
        i = 0

        while i < len(G):
          z = i+1
          if z in x:
            DD.append('red')
          else:
            PP.append(z)
          i = i + 1
          
        for k in PP:
          G.remove_node(k)
        nx.draw_networkx_edge_labels(DD,pos,edge_labels=labels)

        nx.draw(G, pos,node_color=DD, with_labels=True,node_size= 500)

        plt.show()

    print('')
    again = input("\tDo you want something more ? ( Enter y for yes ) or If you don't want to do it again ( type n ) : ")