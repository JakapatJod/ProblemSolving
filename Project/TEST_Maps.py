import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

# สถานที่ท่องเที่ยว
#18
G.add_edge('Somdej Phra Naraesuan Shrine', 'Chan Royal Palace', weight=0.014)
G.add_edge('Somdej Phra Naraesuan Shrine', 'Pot Noodle', weight=7.1)
#19
G.add_edge('Chan Royal Palace', 'Wat Phra Si Rattana Mahathat', weight=0.8)
G.add_edge('Chan Royal Palace', 'Pot Noodle', weight=1)
G.add_edge('Chan Royal Palace', 'Wat Rachburana', weight=1.9)
G.add_edge('Chan Royal Palace', 'Somdej Phra Naraesuan Shrine', weight=0.014)
#13
G.add_edge('Pot Noodle', 'Somdej Phra Naraesuan Shrine', weight=7.1)
G.add_edge('Pot Noodle', 'Chan Royal Palace', weight=0.1)
G.add_edge('Pot Noodle', 'Pattara Resort', weight=1.7)
G.add_edge('Pot Noodle', 'Popeye Coffee', weight=3.2)
#14
G.add_edge('Popeye Coffee', 'Pattara Resort', weight=2.1)
G.add_edge('Popeye Coffee', 'Ton kam pu Coffee', weight=3.5)
G.add_edge('Popeye Coffee', 'Pot Noodle', weight=3.2)
#15
G.add_edge('Ton kam pu Coffee', 'Pattara Resort', weight=1.9)
G.add_edge('Ton kam pu Coffee', 'Popeye Coffee', weight=3.5)
G.add_edge('Ton kam pu Coffee', 'Khanom chin ton kam pu', weight=0.001)
#16
G.add_edge('Khanom chin ton kam pu', 'Ton kam pu Coffee', weight=0.001)
G.add_edge('Khanom chin ton kam pu', 'Phitsanulok Walking Street', weight=1.9)
G.add_edge('Khanom chin ton kam pu', 'Pattara Resort', weight=3)
#12
G.add_edge('Pattara Resort', 'Khanom chin ton kam pu', weight=1.9)
G.add_edge('Pattara Resort', 'Ton kam pu Coffee', weight=1.9)
G.add_edge('Pattara Resort', 'Popeye Coffee', weight=2.1)
G.add_edge('Pattara Resort', 'Pot Noodle', weight=1.7)
G.add_edge('Pattara Resort', 'Phitsanulok Walking Street', weight=1.6)
G.add_edge('Pattara Resort', 'Pae Bhu Fah Thai', weight=1.6)
#10
G.add_edge('Phitsanulok Walking Street', 'Khanom chin ton kam pu', weight=3)
G.add_edge('Phitsanulok Walking Street', 'Pattara Resort', weight=1.6)
G.add_edge('Phitsanulok Walking Street', 'Pae Bhu Fah Thai', weight=0.170)
G.add_edge('Phitsanulok Walking Street', 'Chanu', weight=2.4)
#11
G.add_edge('Pae Bhu Fah Thai', 'Pattara Resort', weight=1.6)
G.add_edge('Pae Bhu Fah Thai', 'Phitsanulok Walking Street', weight=0.170)
#5
G.add_edge('Chanu', 'Phitsanulok Walking Street', weight=2.4)
G.add_edge('Chanu', 'Pheun Ban Jao Tawi Museum Sargeant Major Thawee Folk Museum', weight=0.950)
G.add_edge('Chanu', 'Tourism authority of thailand Phitsanulok', weight=0.5)
#4
G.add_edge('Tourism authority of thailand Phitsanulok', 'Chanu', weight=0.5)
G.add_edge('Tourism authority of thailand Phitsanulok', 'Wat Rachburana', weight=2.2)
#6
G.add_edge('Pheun Ban Jao Tawi Museum Sargeant Major Thawee Folk Museum', 'Chanu', weight=0.950)
G.add_edge('Pheun Ban Jao Tawi Museum Sargeant Major Thawee Folk Museum', 'Buranathai Buddha Casting Foundry', weight=0.1)
G.add_edge('Pheun Ban Jao Tawi Museum Sargeant Major Thawee Folk Museum', 'Ayara Grand Palace Hotel', weight=1.3)
#8
G.add_edge('Buranathai Buddha Casting Foundry', 'Pheun Ban Jao Tawi Museum Sargeant Major Thawee Folk Museum', weight=0.1)
G.add_edge('Buranathai Buddha Casting Foundry', 'Garden Birds of Thailand', weight=0.14)
G.add_edge('Buranathai Buddha Casting Foundry', 'Ayara Grand Palace Hotel', weight=1.4)
#7
G.add_edge('Garden Birds of Thailand', 'Buranathai Buddha Casting Foundry', weight=0.14)
G.add_edge('Garden Birds of Thailand', 'Ayara Grand Palace Hotel', weight=1.4)
#9
G.add_edge('Ayara Grand Palace Hotel', 'Pheun Ban Jao Tawi Museum Sargeant Major Thawee Folk Museum', weight=1.3)
G.add_edge('Ayara Grand Palace Hotel', 'Garden Birds of Thailand', weight=1.4)
G.add_edge('Ayara Grand Palace Hotel', 'Buranathai Buddha Casting Foundry', weight=1.4)
G.add_edge('Ayara Grand Palace Hotel', 'Wat Rachburana', weight=1.4)
G.add_edge('Ayara Grand Palace Hotel', 'Mai Oak Coffee', weight=1.6)
#3
G.add_edge('Wat Rachburana', 'Wat Nang Phaya', weight=0.050)
G.add_edge('Wat Rachburana', 'Ayara Grand Palace Hotel', weight=1.4)
G.add_edge('Wat Rachburana', 'Tourism authority of thailand Phitsanulok', weight=2.2)
G.add_edge('Wat Rachburana', 'Chan Royal Palace', weight=1.9)
#2
G.add_edge('Wat Nang Phaya', 'Wat Rachburana', weight=0.050)
G.add_edge('Wat Nang Phaya', 'Wat Phra Si Rattana Mahathat', weight=0.350)
#1
G.add_edge('Wat Phra Si Rattana Mahathat', 'Wat Nang Phaya', weight=0.350)
G.add_edge('Wat Phra Si Rattana Mahathat', 'Chan Royal Palace', weight=0.800)
G.add_edge('Wat Phra Si Rattana Mahathat', 'Mai Oak Coffee', weight=3.5)
#20
G.add_edge('Mai Oak Coffee', 'Wat Phra Si Rattana Mahathat', weight=3.5)
G.add_edge('Mai Oak Coffee', 'Ayara Grand Palace Hotel', weight=1.6)



print('-'*10,'Phitsanulok tourist attraction','-'*10,)
print('')
print('\t\t1.Travel')
print('\t\t2.')
print('')
op = int(input('\t\tEnter the chioce : '))
print('-'*51)
if op == 1: 
    location1 = input('\tChoose your location : ')
    location2 = input("\tWhere do you want to go :  ")
    print('\tShortest path from ',location1 ,'to',location2 ,'is',nx.shortest_path(G,source=location1,target=location2,weight='weight'))
    d = (nx.shortest_path_length(G,source=location1,target=location2,weight='weight'))
    print("\tThe distance is ",d,"km")
    #print("\tThe time is about",d//8,"minute")
    print('')
    edge_labels = nx.get_edge_attributes(G, 'weight')

    pos = nx.spring_layout(G) #วาดกกราฟ
    plt.figure(8,figsize=(20,20))
    nx.draw(G,pos, with_labels=True,font_color= 'yellow',node_size= 2000)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    plt.show()

