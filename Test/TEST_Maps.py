import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

# สถานที่ท่องเที่ยว
#18
G.add_edge('18', '19', weight=0.014)
G.add_edge('18', '13', weight=7.1)
#19
G.add_edge('19', '1', weight=0.8)
G.add_edge('19', '13', weight=1)
G.add_edge('19', '3', weight=1.9)
G.add_edge('19', '18', weight=0.014)
#13
G.add_edge('13', '18', weight=7.1)
G.add_edge('13', '19', weight=0.1)
G.add_edge('13', '12', weight=1.7)
G.add_edge('13', '14', weight=3.2)
#14
G.add_edge('14', '12', weight=2.1)
G.add_edge('14', '15', weight=3.5)
G.add_edge('14', '13', weight=3.2)
#15
G.add_edge('15', '12', weight=1.9)
G.add_edge('15', '14', weight=3.5)
G.add_edge('15', '16', weight=0.001)
#16
G.add_edge('16', '15', weight=0.001)
G.add_edge('16', '10', weight=1.9)
G.add_edge('16', '12', weight=3)
#12
G.add_edge('12', '16', weight=1.9)
G.add_edge('12', '15', weight=1.9)
G.add_edge('12', '14', weight=2.1)
G.add_edge('12', '13', weight=1.7)
G.add_edge('12', '10', weight=1.6)
G.add_edge('12', '11', weight=1.6)
#10
G.add_edge('10', '16', weight=3)
G.add_edge('10', '12', weight=1.6)
G.add_edge('10', '11', weight=0.170)
G.add_edge('10', '5', weight=2.4)
#11
G.add_edge('11', '12', weight=1.6)
G.add_edge('11', '10', weight=0.170)
#5
G.add_edge('5', '10', weight=2.4)
G.add_edge('5', '6', weight=0.950)
G.add_edge('5', '4', weight=0.5)
#4
G.add_edge('4', '5', weight=0.5)
G.add_edge('4', '3', weight=2.2)
#6
G.add_edge('6', '5', weight=0.950)
G.add_edge('6', '8', weight=0.1)
G.add_edge('6', '9', weight=1.3)
#8
G.add_edge('8', '6', weight=0.1)
G.add_edge('8', '7', weight=0.14)
G.add_edge('8', '9', weight=1.4)
#7
G.add_edge('7', '8', weight=0.14)
G.add_edge('7', '9', weight=1.4)
#9
G.add_edge('9', '6', weight=1.3)
G.add_edge('9', '7', weight=1.4)
G.add_edge('9', '8', weight=1.4)
G.add_edge('9', '3', weight=1.4)
G.add_edge('9', '20', weight=1.6)
#3
G.add_edge('3', '2', weight=0.050)
G.add_edge('3', '9', weight=1.4)
G.add_edge('3', '4', weight=2.2)
G.add_edge('3', '19', weight=1.9)
#2
G.add_edge('2', '3', weight=0.050)
G.add_edge('2', '1', weight=0.350)
#1
G.add_edge('1', '2', weight=0.350)
G.add_edge('1', '19', weight=0.800)
G.add_edge('1', '20', weight=3.5)
#20
G.add_edge('20', '1', weight=3.5)
G.add_edge('20', '9', weight=1.6)


again = 'y'
while again == 'y' :
    print('-'*10,'Phitsanulok tourist attraction','-'*10,)
    print('')
    print('\t\t1.Travel')
    print('\t\t2.Graph')
    print('')
    op = int(input('\t\tEnter the chioce : '))
    print('-'*51)
    if op == 1:
        edge_labels = nx.get_edge_attributes(G, 'weight')
        pos = nx.spring_layout(G)
        plt.figure(8,figsize=(20,20))
        nx.draw(G,pos, with_labels=True,font_color= 'yellow',node_size= 2000)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
        plt.show()
    if op == 2: # TRAVEL A --> B

        location1 = input('\tChoose your location : ')
        location2 = input("\tWhere do you want to go :  ")
        print('\tShortest path from ',location1 ,'to',location2 ,'is',nx.shortest_path(G,source=location1
             ,target=location2,weight='weight'))

        d = (nx.shortest_path_length(G,source=location1,target=location2,weight='weight'))

        print("\tThe distance is ",d,"km")
    
        print('')

        edge_labels = nx.get_edge_attributes(G, 'weight')
        pos = nx.spring_layout(G) #วาดกกราฟ
        plt.figure(8,figsize=(20,20))
        nx.draw(G,pos, with_labels=True,font_color= 'yellow',node_size= 2000)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
        plt.show()
    if op == 3:
        location1=input("Enter your location :  ")
        location2=input("Where do you want to visit :  ")
        location3=input("Where do you want to visit :  ")
        location4=input("Where do you want to go :  ")
        a=(nx.shortest_path_length(G,source=location1,target=location2,weight='weight'))
        b=(nx.shortest_path_length(G,source=location2,target=location3,weight='weight'))
        c=(nx.shortest_path_length(G,source=location3,target=location4,weight='weight'))
        d=(nx.shortest_path_length(G,source=location1,target=location3,weight='weight'))
        e=(nx.shortest_path_length(G,source=location1,target=location4,weight='weight'))
        f=(nx.shortest_path_length(G,source=location2,target=location4,weight='weight'))
        g=(nx.shortest_path_length(G,source=location1,target=location2,weight='weight'))
        h=(nx.shortest_path_length(G,source=location2,target=location3,weight='weight'))
        i=(nx.shortest_path_length(G,source=location3,target=location4,weight='weight'))
        j=(nx.shortest_path_length(G,source=location1,target=location3,weight='weight'))
        k=(nx.shortest_path_length(G,source=location1,target=location4,weight='weight'))
        l=(nx.shortest_path_length(G,source=location2,target=location4,weight='weight'))
        m=(nx.shortest_path_length(G,source=location4,target=location3,weight='weight'))
        n=(nx.shortest_path_length(G,source=location4,target=location2,weight='weight'))
        o=(nx.shortest_path_length(G,source=location3,target=location2,weight='weight'))
        a1=(nx.shortest_path(G,source=location1,target=location2,weight='weight'))
        a2=(nx.shortest_path(G,source=location3,target=location2,weight='weight'))
        a3=(nx.shortest_path(G,source=location1,target=location3,weight='weight'))
        a4=(nx.shortest_path(G,source=location2,target=location3,weight='weight'))
        a5=(nx.shortest_path(G,source=location1,target=location4,weight='weight'))
        a6=(nx.shortest_path(G,source=location2,target=location4,weight='weight'))
        a7=(nx.shortest_path(G,source=location4,target=location2,weight='weight'))
        a8=(nx.shortest_path(G,source=location3,target=location2,weight='weight'))
        a8=(nx.shortest_path(G,source=location4,target=location3,weight='weight'))
        a9=(nx.shortest_path(G,source=location3,target=location4,weight='weight'))
        A=g+h+i
        B=g+l+m
        C=j+o+l
        D=j+i+n
        E=k+m+o
        F=k+n+h
        list1 =[A,B,C,D,E,F]

        if min(list1)==A:
          print('Shorttest path from ',location1 ,'to',location4 ,'is',a1+a4+a8)
        if min(list1)==B:
          print('Shorttest path from ',location1 ,'to',location4 ,'is',a1+a6+a9)
        if min(list1)==C:
          print('Shorttest path from ',location1 ,'to',location4 ,'is',a3+a8+a6)
        if min(list1)==D:
          print('Shorttest path from ',location1 ,'to',location4 ,'is',a3+a8+a7)
        if min(list1)==E:
          print('Shorttest path from ',location1 ,'to',location4 ,'is',a5+a9+a8)
        if min(list1)==F:
          print('Shorttest path from ',location1 ,'to',location4 ,'is',a5+a7+a4)
        print('The distance is  :',min(list1),"km")
        print("The time is about",(min(list1))//80,"hours")
        edge_labels = nx.get_edge_attributes(G, 'weight')
        #print (edge_labels)
        pos = nx.spring_layout(G)  #วาดกกราฟ
        plt.figure(8,figsize=(20,20))
        nx.draw(G,pos, with_labels=True,font_color= 'yellow',node_size= 2000)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
        plt.show()
    again = input("\tDo you want something more ? ( Enter y for yes ) or If you don't want to do it again ( type n ) : ")