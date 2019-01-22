graph = {'0 0': set(['0 1', '1 0']),
		 '0 1': set(['0 0', '0 2', '1 1']),
         '0 2': set(['0 1', '0 3', '1 2']),
         '0 3': set(['0 2', '0 4', '1 3']),
		 '0 4': set(['0 3', '0 5', '1 4']),
		 '0 5': set(['0 4', '0 6', '1 5']),
		 '0 6': set(['0 5', '0 7', '1 6']),
		 '0 7': set(['0 6', '0 8', '1 7']),
		 '0 8': set(['0 7', '0 9', '1 8']),
		 '0 9': set(['0 8', '0 10', '1 9']),
		 '0 10': set(['0 9', '0 11', '1 10']),
		 '0 11': set(['0 10', '0 12', '1 11']),
		 '0 12': set(['0 11', '0 13', '1 12']),
		 '0 13': set(['0 12', '0 14', '1 13']),
		 '0 14': set(['0 13', '1 14']),
		 
		 '1 0': set(['0 0', '1 1', '2 0']),
		 '1 1': set(['0 1', '1 0', '2 1', '1 2' ]),
         '1 2': set(['0 2', '1 1', '2 2', '1 3' ]),
         '1 3': set(['0 3', '1 2', '2 3', '1 4' ]),
		 '1 4': set(['0 4', '1 3', '2 4', '1 5' ]),
		 '1 5': set(['0 5', '1 4', '2 5', '1 6' ]),
		 '1 6': set(['0 6', '1 5', '2 6', '1 7' ]),
		 '1 7': set(['0 7', '1 6', '2 7', '1 8' ]),
		 '1 8': set(['0 8', '1 7', '2 8', '1 9' ]),
		 '1 9': set(['0 9', '1 8', '2 9', '1 10' ]),
		 '1 10': set(['0 10', '1 9', '2 10', '1 11' ]),
		 '1 11': set(['0 11', '1 10', '2 11', '1 12' ]),
		 '1 12': set(['0 12', '1 11', '2 12', '1 13' ]),
		 '1 13': set(['0 13', '1 12', '2 13', '1 14' ]),
		 '1 14': set(['0 14', '1 13', '2 14']),
		 
		 '2 0': set(['1 0', '2 1', '3 0']),
		 '2 1': set(['1 1', '2 0', '3 1', '2 2' ]),
         '2 2': set(['1 2', '2 1', '3 2', '2 3' ]),
         '2 3': set(['1 3', '2 2', '3 3', '2 4' ]),
		 '2 4': set(['1 4', '2 3', '3 4', '2 5' ]),
		 '2 5': set(['1 5', '2 4', '3 5', '2 6' ]),
		 '2 6': set(['1 6', '2 5', '3 6', '2 7' ]),
		 '2 7': set(['1 7', '2 6', '3 7', '2 8' ]),
		 '2 8': set(['1 8', '2 7', '3 8', '2 9' ]),
		 '2 9': set(['1 9', '2 8', '3 9', '2 10' ]),
		 '2 10': set(['1 10', '2 9', '3 10', '2 11' ]),
		 '2 11': set(['1 11', '2 10', '3 11', '2 12' ]),
		 '2 12': set(['1 12', '2 11', '3 12', '2 13' ]),
		 '2 13': set(['1 13', '2 12', '3 13', '2 14' ]),
		 '2 14': set(['1 14', '2 13', '3 14']),
		 
		 '3 0': set(['2 0', '3 1', '4 0']),
		 '3 1': set(['2 1', '3 0', '4 1', '3 2' ]),
         '3 2': set(['2 2', '3 1', '4 2', '3 3' ]),
         '3 3': set(['2 3', '3 2', '4 3', '3 4' ]),
		 '3 4': set(['2 4', '3 3', '4 4', '3 5' ]),
		 '3 5': set(['2 5', '3 4', '4 5', '3 6' ]),
		 '3 6': set(['2 6', '3 5', '4 6', '3 7' ]),
		 '3 7': set(['2 7', '3 6', '4 7', '3 8' ]),
		 '3 8': set(['2 8', '3 7', '4 8', '3 9' ]),
		 '3 9': set(['2 9', '3 8', '4 9', '3 10' ]),
		 '3 10': set(['2 10', '3 9', '4 10', '3 11' ]),
		 '3 11': set(['2 11', '3 10', '4 11', '3 12' ]),
		 '3 12': set(['2 12', '3 11', '4 12', '3 13' ]),
		 '3 13': set(['2 13', '3 12', '4 13', '3 14' ]),
		 '3 14': set(['2 14', '3 13', '4 14']),
		 
		 '4 0': set(['3 0', '4 1', '5 0']),
		 '4 1': set(['3 1', '4 0', '5 1', '4 2' ]),
         '4 2': set(['3 2', '4 1', '5 2', '4 3' ]),
         '4 3': set(['3 3', '4 2', '5 3', '4 4' ]),
		 '4 4': set(['3 4', '4 3', '5 4', '4 5' ]),
		 '4 5': set(['3 5', '4 4', '5 5', '4 6' ]),
		 '4 6': set(['3 6', '4 5', '5 6', '4 7' ]),
		 '4 7': set(['3 7', '4 6', '5 7', '4 8' ]),
		 '4 8': set(['3 8', '4 7', '5 8', '4 9' ]),
		 '4 9': set(['3 9', '4 8', '5 9', '4 10' ]),
		 '4 10': set(['3 10', '4 9', '5 10', '4 11' ]),
		 '4 11': set(['3 11', '4 10', '5 11', '4 12' ]),
		 '4 12': set(['3 12', '4 11', '5 12', '4 13' ]),
		 '4 13': set(['3 13', '4 12', '5 13', '4 14' ]),
		 '4 14': set(['3 14', '4 13', '5 14']),
		 
		 '5 0': set(['4 0', '5 1', '6 0']),
		 '5 1': set(['4 1', '5 0', '6 1', '5 2' ]),
         '5 2': set(['4 2', '5 1', '6 2', '5 3' ]),
         '5 3': set(['4 3', '5 2', '6 3', '5 4' ]),
		 '5 4': set(['4 4', '5 3', '6 4', '5 5' ]),
		 '5 5': set(['4 5', '5 4', '6 5', '5 6' ]),
		 '5 6': set(['4 6', '5 5', '6 6', '5 7' ]),
		 '5 7': set(['4 7', '5 6', '6 7', '5 8' ]),
		 '5 8': set(['4 8', '5 7', '6 8', '5 9' ]),
		 '5 9': set(['4 9', '5 8', '6 9', '5 10' ]),
		 '5 10': set(['4 10', '5 9', '6 10', '5 11' ]),
		 '5 11': set(['4 11', '5 10', '6 11', '5 12' ]),
		 '5 12': set(['4 12', '5 11', '6 12', '5 13' ]),
		 '5 13': set(['4 13', '5 12', '6 13', '5 14' ]),
		 '5 14': set(['4 14', '5 13', '6 14']),
		 
		 '6 0': set(['5 0', '6 1', '7 0']),
		 '6 1': set(['5 1', '6 0', '7 1', '6 2' ]),
         '6 2': set(['5 2', '6 1', '7 2', '6 3' ]),
         '6 3': set(['5 3', '6 2', '7 3', '6 4' ]),
		 '6 4': set(['5 4', '6 3', '7 4', '6 5' ]),
		 '6 5': set(['5 5', '6 4', '7 5', '6 6' ]),
		 '6 6': set(['5 6', '6 5', '7 6', '6 7' ]),
		 '6 7': set(['5 7', '6 6', '7 7', '6 8' ]),
		 '6 8': set(['5 8', '6 7', '7 8', '6 9' ]),
		 '6 9': set(['5 9', '6 8', '7 9', '6 10' ]),
		 '6 10': set(['5 10', '6 9', '7 10', '6 11' ]),
		 '6 11': set(['5 11', '6 10', '7 11', '6 12' ]),
		 '6 12': set(['5 12', '6 11', '7 12', '6 13' ]),
		 '6 13': set(['5 13', '6 12', '7 13', '6 14' ]),
		 '6 14': set(['5 14', '6 13', '7 14']),
		 
		 '7 0': set(['6 0', '7 1', '8 0']),
		 '7 1': set(['6 1', '7 0', '8 1', '7 2' ]),
         '7 2': set(['6 2', '7 1', '8 2', '7 3' ]),
         '7 3': set(['6 3', '7 2', '8 3', '7 4' ]),
		 '7 4': set(['6 4', '7 3', '8 4', '7 5' ]),
		 '7 5': set(['6 5', '7 4', '8 5', '7 6' ]),
		 '7 6': set(['6 6', '7 5', '8 6', '7 7' ]),
		 '7 7': set(['6 7', '7 6', '8 7', '7 8' ]),
		 '7 8': set(['6 8', '7 7', '8 8', '7 9' ]),
		 '7 9': set(['6 9', '7 8', '8 9', '7 10' ]),
		 '7 10': set(['6 10', '7 9', '8 10', '7 11' ]),
		 '7 11': set(['6 11', '7 10', '8 11', '7 12' ]),
		 '7 12': set(['6 12', '7 11', '8 12', '7 13' ]),
		 '7 13': set(['6 13', '7 12', '8 13', '7 14' ]),
		 '7 14': set(['6 14', '7 13', '8 14']),
		 
		 '8 0': set(['7 0', '8 1', '9 0']),
		 '8 1': set(['7 1', '8 0', '9 1', '8 2' ]),
         '8 2': set(['7 2', '8 1', '9 2', '8 3' ]),
         '8 3': set(['7 3', '8 2', '9 3', '8 4' ]),
		 '8 4': set(['7 4', '8 3', '9 4', '8 5' ]),
		 '8 5': set(['7 5', '8 4', '9 5', '8 6' ]),
		 '8 6': set(['7 6', '8 5', '2 6', '8 7' ]),
		 '8 7': set(['7 7', '8 6', '9 7', '8 8' ]),
		 '8 8': set(['7 8', '8 7', '9 8', '8 9' ]),
		 '8 9': set(['7 9', '8 8', '9 9', '8 10' ]),
		 '8 10': set(['7 10', '8 9', '9 10', '8 11' ]),
		 '8 11': set(['7 11', '8 10', '9 11', '8 12' ]),
		 '8 12': set(['7 12', '8 11', '9 12', '8 13' ]),
		 '8 13': set(['7 13', '8 12', '9 13', '8 14' ]),
		 '8 14': set(['7 14', '8 13', '9 14']),
		 
		 '9 0': set(['8 0', '9 1', '10 0']),
		 '9 1': set(['8 1', '9 0', '10 1', '9 2' ]),
         '9 2': set(['8 2', '9 1', '10 2', '9 3' ]),
         '9 3': set(['8 3', '9 2', '10 3', '9 4' ]),
		 '9 4': set(['8 4', '9 3', '10 4', '9 5' ]),
		 '9 5': set(['8 5', '9 4', '10 5', '9 6' ]),
		 '9 6': set(['8 6', '9 5', '10 6', '9 7' ]),
		 '9 7': set(['8 7', '9 6', '10 7', '9 8' ]),
		 '9 8': set(['8 8', '9 7', '10 8', '9 9' ]),
		 '9 9': set(['8 9', '9 8', '10 9', '9 10' ]),
		 '9 10': set(['8 10', '9 9', '10 10', '9 11' ]),
		 '9 11': set(['8 11', '9 10', '10 11', '9 12' ]),
		 '9 12': set(['8 12', '9 11', '10 12', '9 13' ]),
		 '9 13': set(['8 13', '9 12', '10 13', '9 14' ]),
		 '9 14': set(['8 14', '9 13', '10 14']),
		 
		 '10 0': set(['9 0', '10 1', '11 0']),
		 '10 1': set(['9 1', '10 0', '11 1', '10 2' ]),
         '10 2': set(['9 2', '10 1', '11 2', '10 3' ]),
         '10 3': set(['9 3', '10 2', '11 3', '10 4' ]),
		 '10 4': set(['9 4', '10 3', '11 4', '10 5' ]),
		 '10 5': set(['9 5', '10 4', '11 5', '10 6' ]),
		 '10 6': set(['9 6', '10 5', '11 6', '10 7' ]),
		 '10 7': set(['9 7', '10 6', '11 7', '10 8' ]),
		 '10 8': set(['9 8', '10 7', '11 8', '10 9' ]),
		 '10 9': set(['9 9', '10 8', '11 9', '10 10' ]),
		 '10 10': set(['9 10', '10 9', '11 10', '10 11' ]),
		 '10 11': set(['9 11', '10 10', '11 11', '10 12' ]),
		 '10 12': set(['9 12', '10 11', '11 12', '10 13' ]),
		 '10 13': set(['9 13', '10 12', '11 13', '10 14' ]),
		 '10 14': set(['9 14', '10 13', '11 14']),
		 
		 '11 0': set(['10 0', '11 1', '12 0']),
		 '11 1': set(['10 1', '11 0', '12 1', '11 2' ]),
         '11 2': set(['10 2', '11 1', '12 2', '11 3' ]),
         '11 3': set(['10 3', '11 2', '12 3', '11 4' ]),
		 '11 4': set(['10 4', '11 3', '12 4', '11 5' ]),
		 '11 5': set(['10 5', '11 4', '12 5', '11 6' ]),
		 '11 6': set(['10 6', '11 5', '12 6', '11 7' ]),
		 '11 7': set(['10 7', '11 6', '12 7', '11 8' ]),
		 '11 8': set(['10 8', '11 7', '12 8', '11 9' ]),
		 '11 9': set(['10 9', '11 8', '12 9', '11 10' ]),
		 '11 10': set(['10 10', '11 9', '12 10', '11 11' ]),
		 '11 11': set(['10 11', '11 10', '12 11', '11 12' ]),
		 '11 12': set(['10 12', '11 11', '12 12', '11 13' ]),
		 '11 13': set(['10 13', '11 12', '12 13', '11 14' ]),
		 '11 14': set(['10 14', '11 13', '12 14']),
		 
		 '12 0': set(['11 0', '12 1', '13 0']),
		 '12 1': set(['11 1', '12 0', '13 1', '12 2' ]),
         '12 2': set(['11 2', '12 1', '13 2', '12 3' ]),
         '12 3': set(['11 3', '12 2', '13 3', '12 4' ]),
		 '12 4': set(['11 4', '12 3', '13 4', '12 5' ]),
		 '12 5': set(['11 5', '12 4', '13 5', '12 6' ]),
		 '12 6': set(['11 6', '12 5', '13 6', '12 7' ]),
		 '12 7': set(['11 7', '12 6', '13 7', '12 8' ]),
		 '12 8': set(['11 8', '12 7', '13 8', '12 9' ]),
		 '12 9': set(['11 9', '12 8', '13 9', '12 10' ]),
		 '12 10': set(['11 10', '12 9', '13 10', '12 11' ]),
		 '12 11': set(['11 11', '12 10', '13 11', '12 12' ]),
		 '12 12': set(['11 12', '12 11', '13 12', '12 13' ]),
		 '12 13': set(['11 13', '12 12', '13 13', '12 14' ]),
		 '12 14': set(['11 14', '12 13', '13 14']),
		 
		 '13 0': set(['12 0', '13 1', '14 0']),
		 '13 1': set(['12 1', '13 0', '14 1', '13 2' ]),
         '13 2': set(['12 2', '13 1', '14 2', '13 3' ]),
         '13 3': set(['12 3', '13 2', '14 3', '13 4' ]),
		 '13 4': set(['12 4', '13 3', '14 4', '13 5' ]),
		 '13 5': set(['12 5', '13 4', '14 5', '13 6' ]),
		 '13 6': set(['12 6', '13 5', '14 6', '13 7' ]),
		 '13 7': set(['12 7', '13 6', '14 7', '13 8' ]),
		 '13 8': set(['12 8', '13 7', '14 8', '13 9' ]),
		 '13 9': set(['12 9', '13 8', '14 9', '13 10' ]),
		 '13 10': set(['12 10', '13 9', '14 10', '13 11' ]),
		 '13 11': set(['12 11', '13 10', '14 11', '13 12' ]),
		 '13 12': set(['12 12', '13 11', '14 12', '13 13' ]),
		 '13 13': set(['12 13', '13 12', '14 13', '13 14' ]),
		 '13 14': set(['12 14', '13 13', '14 14']),
		 
		 '14 0': set(['13 0', '14 1',]),
		 '14 1': set(['13 1', '14 0', '14 2' ]),
         '14 2': set(['13 2', '14 1', '14 3' ]),
         '14 3': set(['13 3', '14 2', '14 4' ]),
		 '14 4': set(['13 4', '14 3', '14 5' ]),
		 '14 5': set(['13 5', '14 4', '14 6' ]),
		 '14 6': set(['13 6', '14 5', '14 7' ]),
		 '14 7': set(['13 7', '14 6', '14 8' ]),
		 '14 8': set(['13 8', '14 7', '14 9' ]),
		 '14 9': set(['13 9', '14 8', '14 10' ]),
		 '14 10': set(['13 10', '14 9', '14 11' ]),
		 '14 11': set(['13 11', '14 10', '14 12' ]),
		 '14 12': set(['13 12', '14 11', '14 13' ]),
		 '14 13': set(['13 13', '14 12', '14 14' ]),
		 '14 14': set(['14 13', '13 14',])}
		 
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            if vertex == "0 0":
                nn.detection(nn, 1)
            elif vertex == "0 1":
                nn.detection(nn, 2)
            elif vertex =="0 2":
                nn.detection(nn, 3)
            elif vertex =="0 3":
                nn.detection(nn, 4)
            elif vertex =="0 4":
                nn.detection(nn, 5)
            elif vertex =="0 5":
                nn.detection(nn, 6)
            elif vertex =="0 6":
                nn.detection(nn, 7)
            elif vertex =="0 7":
                nn.detection(nn, 8)
            elif vertex =="0 8":
                nn.detection(nn, 9)
            elif vertex =="0 9":
                nn.detection(nn, 10)
            elif vertex =="0 10":
                nn.detection(nn, 11)
            elif vertex =="0 11":
                nn.detection(nn, 12)
            elif vertex =="0 12":
                nn.detection(nn, 13)
            elif vertex =="0 13":
                nn.detection(nn, 14)
            elif vertex =="0 14":
                nn.detection(nn, 15)

            elif vertex == "1 0":
                nn.detection(nn, 16)
            elif vertex == "1 1":
                nn.detection(nn, 17)
            elif vertex =="1 2":
                nn.detection(nn, 18)
            elif vertex =="1 3":
                nn.detection(nn, 19)
            elif vertex =="1 4":
                nn.detection(nn, 20)
            elif vertex =="1 5":
                nn.detection(nn, 21)
            elif vertex =="1 6":
                nn.detection(nn, 22)
            elif vertex =="1 7":
                nn.detection(nn, 23)
            elif vertex =="1 8":
                nn.detection(nn, 24)
            elif vertex =="1 9":
                nn.detection(nn, 25)
            elif vertex =="1 10":
                nn.detection(nn, 26)
            elif vertex =="1 11":
                nn.detection(nn, 27)
            elif vertex =="1 12":
                nn.detection(nn, 28)
            elif vertex == "1 13":
                nn.detection(nn, 29)
            elif vertex =="1 14":
                nn.detection(nn, 30)


            elif vertex == "2 0":
                nn.detection(nn, 31)
            elif vertex == "2 1":
                nn.detection(nn, 32)
            elif vertex =="2 2":
                nn.detection(nn, 33)
            elif vertex =="2 3":
                nn.detection(nn, 34)
            elif vertex =="2 4":
                nn.detection(nn, 35)
            elif vertex =="2 5":
                nn.detection(nn, 36)
            elif vertex =="2 6":
                nn.detection(nn, 37)
            elif vertex =="2 7":
                nn.detection(nn, 38)
            elif vertex =="2 8":
                nn.detection(nn, 39)
            elif vertex =="2 9":
                nn.detection(nn, 40)
            elif vertex =="2 10":
                nn.detection(nn, 41)
            elif vertex =="2 11":
                nn.detection(nn, 42)
            elif vertex =="2 12":
                nn.detection(nn, 43)
            elif vertex == "2 13":
                nn.detection(nn, 44)
            elif vertex =="2 14":
                nn.detection(nn, 45)


            elif vertex == "3 0":
                nn.detection(nn, 46)
            elif vertex == "3 1":
                nn.detection(nn, 47)
            elif vertex =="3 2":
                nn.detection(nn, 48)
            elif vertex =="3 3":
                nn.detection(nn, 49)
            elif vertex =="3 4":
                nn.detection(nn, 50)
            elif vertex =="3 5":
                nn.detection(nn, 51)
            elif vertex =="3 6":
                nn.detection(nn, 52)
            elif vertex =="3 7":
                nn.detection(nn, 53)
            elif vertex =="3 8":
                nn.detection(nn, 54)
            elif vertex =="3 9":
                nn.detection(nn, 55)
            elif vertex =="3 10":
                nn.detection(nn, 56)
            elif vertex =="3 11":
                nn.detection(nn, 57)
            elif vertex =="3 12":
                nn.detection(nn, 58)
            elif vertex == "3 13":
                nn.detection(nn, 59)
            elif vertex =="3 14":
                nn.detection(nn, 60)


            elif vertex == "4 0":
                nn.detection(nn, 61)
            elif vertex == "4 1":
                nn.detection(nn, 62)
            elif vertex =="4 2":
                nn.detection(nn, 63)
            elif vertex =="4 3":
                nn.detection(nn, 64)
            elif vertex =="4 4":
                nn.detection(nn, 65)
            elif vertex =="4 5":
                nn.detection(nn, 66)
            elif vertex =="4 6":
                nn.detection(nn, 67)
            elif vertex =="4 7":
                nn.detection(nn, 68)
            elif vertex =="4 8":
                nn.detection(nn, 69)
            elif vertex =="4 9":
                nn.detection(nn, 70)
            elif vertex =="4 10":
                nn.detection(nn, 71)
            elif vertex =="4 11":
                nn.detection(nn, 72)
            elif vertex =="4 12":
                nn.detection(nn, 73)
            elif vertex == "4 13":
                nn.detection(nn, 74)
            elif vertex =="4 14":
                nn.detection(nn, 75)


            elif vertex == "5 0":
                nn.detection(nn, 76)
            elif vertex == "5 1":
                nn.detection(nn, 77)
            elif vertex =="5 2":
                nn.detection(nn, 78)
            elif vertex =="5 3":
                nn.detection(nn, 79)
            elif vertex =="5 4":
                nn.detection(nn, 80)
            elif vertex =="5 5":
                nn.detection(nn, 81)
            elif vertex =="5 6":
                nn.detection(nn, 82)
            elif vertex =="5 7":
                nn.detection(nn, 83)
            elif vertex =="5 8":
                nn.detection(nn, 84)
            elif vertex =="5 9":
                nn.detection(nn, 85)
            elif vertex =="5 10":
                nn.detection(nn, 86)
            elif vertex =="5 11":
                nn.detection(nn, 87)
            elif vertex =="5 12":
                nn.detection(nn, 88)
            elif vertex == "5 13":
                nn.detection(nn, 89)
            elif vertex =="5 14":
                nn.detection(nn, 90)



            elif vertex == "6 0":
                nn.detection(nn, 91)
            elif vertex == "6 1":
                nn.detection(nn, 92)
            elif vertex =="6 2":
                nn.detection(nn, 93)
            elif vertex =="6 3":
                nn.detection(nn, 94)
            elif vertex =="6 4":
                nn.detection(nn, 95)
            elif vertex =="6 5":
                nn.detection(nn, 96)
            elif vertex =="6 6":
                nn.detection(nn, 97)
            elif vertex =="6 7":
                nn.detection(nn, 98)
            elif vertex =="6 8":
                nn.detection(nn, 99)
            elif vertex =="6 9":
                nn.detection(nn, 100)
            elif vertex =="6 10":
                nn.detection(nn, 101)
            elif vertex =="6 11":
                nn.detection(nn, 102)
            elif vertex =="6 12":
                nn.detection(nn, 103)
            elif vertex == "6 13":
                nn.detection(nn, 104)
            elif vertex =="6 14":
                nn.detection(nn, 105)



            elif vertex == "7 0":
                nn.detection(nn, 106)
            elif vertex == "7 1":
                nn.detection(nn, 107)
            elif vertex =="7 2":
                nn.detection(nn, 108)
            elif vertex =="7 3":
                nn.detection(nn, 109)
            elif vertex =="7 4":
                nn.detection(nn, 110)
            elif vertex =="7 5":
                nn.detection(nn, 111)
            elif vertex =="7 6":
                nn.detection(nn, 112)
            elif vertex =="7 7":
                nn.detection(nn, 113)
            elif vertex =="7 8":
                nn.detection(nn, 114)
            elif vertex =="7 9":
                nn.detection(nn, 115)
            elif vertex =="7 10":
                nn.detection(nn, 116)
            elif vertex =="7 11":
                nn.detection(nn, 117)
            elif vertex =="7 12":
                nn.detection(nn, 118)
            elif vertex == "7 13":
                nn.detection(nn, 119)
            elif vertex =="7 14":
                nn.detection(nn, 120)

            elif vertex == "8 0":
                nn.detection(nn, 121)
            elif vertex == "8 1":
                nn.detection(nn, 122)
            elif vertex =="8 2":
                nn.detection(nn, 123)
            elif vertex =="8 3":
                nn.detection(nn, 124)
            elif vertex =="8 4":
                nn.detection(nn, 125)
            elif vertex =="8 5":
                nn.detection(nn, 126)
            elif vertex =="8 6":
                nn.detection(nn, 127)
            elif vertex =="8 7":
                nn.detection(nn, 128)
            elif vertex =="8 8":
                nn.detection(nn, 129)
            elif vertex =="8 9":
                nn.detection(nn, 130)
            elif vertex =="8 10":
                nn.detection(nn, 131)
            elif vertex =="8 11":
                nn.detection(nn, 132)
            elif vertex =="8 12":
                nn.detection(nn, 133)
            elif vertex == "8 13":
                nn.detection(nn, 134)
            elif vertex =="8 14":
                nn.detection(nn, 135)

            elif vertex == "9 0":
                nn.detection(nn, 136)
            elif vertex == "9 1":
                nn.detection(nn, 137)
            elif vertex =="9 2":
                nn.detection(nn, 138)
            elif vertex =="9 3":
                nn.detection(nn, 139)
            elif vertex =="9 4":
                nn.detection(nn, 140)
            elif vertex =="9 5":
             nn.detection(nn, 141)
            elif vertex =="9 6":
                nn.detection(nn, 142)
            elif vertex =="9 7":
                nn.detection(nn, 143)
            elif vertex =="9 8":
                nn.detection(nn, 144)
            elif vertex =="9 9":
                nn.detection(nn, 145)
            elif vertex =="9 10":
                nn.detection(nn, 146)
            elif vertex =="9 11":
                nn.detection(nn, 147)
            elif vertex =="9 12":
                nn.detection(nn, 148)
            elif vertex == "9 13":
                nn.detection(nn, 149)
            elif vertex =="9 14":
                nn.detection(nn, 150)

            elif vertex == "10 0":
                nn.detection(nn, 151)
            elif vertex == "10 1":
                nn.detection(nn, 152)
            elif vertex =="10 2":
                nn.detection(nn, 153)
            elif vertex =="10 3":
                nn.detection(nn, 154)
            elif vertex =="10 4":
                nn.detection(nn, 155)
            elif vertex =="10 5":
                nn.detection(nn, 156)
            elif vertex =="10 6":
                nn.detection(nn, 157)
            elif vertex =="10 7":
                nn.detection(nn, 158)
            elif vertex =="10 8":
                nn.detection(nn, 159)
            elif vertex =="10 9":
                nn.detection(nn, 160)
            elif vertex =="10 10":
                nn.detection(nn, 161)
            elif vertex =="10 11":
                nn.detection(nn, 162)
            elif vertex =="10 12":
                nn.detection(nn, 163)
            elif vertex == "10 13":
                nn.detection(nn, 164)
            elif vertex =="10 14":
                nn.detection(nn, 165)


            elif vertex == "11 0":
                nn.detection(nn, 166)
            elif vertex == "11 1":
                nn.detection(nn, 167)
            elif vertex == "11 2":
                nn.detection(nn, 168)
            elif vertex =="11 3":
                nn.detection(nn, 169)
            elif vertex =="11 4":
                nn.detection(nn, 170)
            elif vertex =="11 5":
                nn.detection(nn, 171)
            elif vertex =="11 6":
                nn.detection(nn, 172)
            elif vertex =="11 7":
                nn.detection(nn, 173)
            elif vertex =="11 8":
                nn.detection(nn, 174)
            elif vertex =="11 9":
                nn.detection(nn, 175)
            elif vertex =="11 10":
                nn.detection(nn, 176)
            elif vertex =="1 11":
                nn.detection(nn, 177)
            elif vertex =="11 12":
                nn.detection(nn, 178)
            elif vertex == "11 13":
                nn.detection(nn, 179)
            elif vertex =="11 14":
                nn.detection(nn, 180)
            



            elif vertex == "12 0":
                nn.detection(nn, 181)
            elif vertex == "12 1":
                nn.detection(nn, 182)
            elif vertex =="12 2":
                nn.detection(nn, 183)
            elif vertex =="12 3":
                nn.detection(nn, 184)
            elif vertex =="12 4":
                nn.detection(nn, 185)
            elif vertex =="12 5":
                nn.detection(nn, 186)
            elif vertex =="12 6":
                nn.detection(nn, 187)
            elif vertex =="12 7":
                nn.detection(nn, 188)
            elif vertex =="12 8":
                nn.detection(nn, 189)
            elif vertex =="12 9":
                nn.detection(nn, 190)
            elif vertex =="12 10":
                nn.detection(nn, 191)
            elif vertex =="12 11":
                nn.detection(nn, 192)
            elif vertex =="12 12":
                nn.detection(nn, 193)
            elif vertex == "12 13":
                nn.detection(nn, 194)
            elif vertex =="12 14":
                nn.detection(nn, 195)

            elif vertex == "13 0":
                nn.detection(nn, 196)
            elif vertex == "13 1":
                nn.detection(nn, 197)
            elif vertex == "13 2":
                nn.detection(nn, 198)
            elif vertex =="13 3":
                nn.detection(nn, 199)
            elif vertex =="13 4":
                nn.detection(nn, 200)
            elif vertex =="13 5":
                nn.detection(nn, 201)
            elif vertex =="13 6":
                nn.detection(nn, 202)
            elif vertex =="13 7":
                nn.detection(nn, 203)
            elif vertex =="13 8":
                nn.detection(nn, 204)
            elif vertex =="13 9":
                nn.detection(nn, 205)
            elif vertex =="13 10":
                nn.detection(nn, 206)
            elif vertex =="13 11":
                nn.detection(nn, 207)
            elif vertex =="13 12":
                nn.detection(nn, 208)
            elif vertex == "13 13":
                nn.detection(nn, 209)
            elif vertex =="13 14":
                nn.detection(nn, 210)


            elif vertex == "14 0":
                nn.detection(nn, 211)
            elif vertex == "14 1":
                nn.detection(nn, 212)
            elif vertex =="14 2":
                nn.detection(nn, 213)
            elif vertex =="14 3":
                nn.detection(nn, 214)
            elif vertex =="14 4":
                nn.detection(nn, 215)
            elif vertex =="14 5":
                nn.detection(nn, 216)
            elif vertex =="14 6":
                nn.detection(nn, 217)
            elif vertex =="14 7":
                nn.detection(nn, 218)
            elif vertex =="14 8":
                nn.detection(nn, 219)
            elif vertex =="14 9":
                nn.detection(nn, 220)
            elif vertex =="14 10":
                nn.detection(nn, 221)
            elif vertex =="14 11":
                nn.detection(nn, 222)
            elif vertex =="14 12":
                nn.detection(nn, 223)
            elif vertex == "14 13":
                nn.detection(nn, 224)
            elif vertex =="14 14":
                nn.detection(nn, 225)
                    if nn.detecion == 1:
                        clf.predict() 
                        if clf.predict() == 1:
                            visited add(vertex) 
                    elif nn.detecion == 0:
                        visited add(vertex)
                    elif nn.detecion == 2:
                        clf.predict() 
                        if clf.predict() == 1:
                            visited add(vertex)           
            print(vertex)
            queue.extend(graph[vertex] - visited)
        
    return visited



import pygame
import csv
from os import path
from collections import deque
vec = pygame.math.Vector2
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 

WIDTH = 20
HEIGHT = 20
 

MARGIN = 5
 


grid = []
for row in range(15):
    grid.append([])
    for column in range(15):
        grid[row].append(0)  
 
grid[0][0] = 1
 
pygame.init()
 
WINDOW_SIZE = [382, 382]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
pygame.display.set_caption("Array Backed Grid")
 

done = False
 
clock = pygame.time.Clock()
 



while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            bfs(graph, '0 0')
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
            matrix = [[]]
           

            
                
              
    screen.fill(BLACK)
 
    for row in range(15):
        for column in range(15):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
  
    clock.tick(60)
 

    pygame.display.flip()
 

#pygame.quit()



    

     
