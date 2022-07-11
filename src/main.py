import pymaze
from dijkstra import *
from pymaze import maze,agent,textLabel,COLOR
from timeit import timeit

if __name__=='__main__':

    m=maze()
    
    m.CreateMaze(loadMaze= 'maze--2022-07-10--15-30-52.csv',x=12,y=18)



    c = 'h'
    H={}
    i = 0

    for i in range(1,104):
        H[i] = c + str(i)
        
    
    
    #H[1]=agent(m,4,4,color=COLOR.red)

  
   
    i = 1
   #Inserindo os obstaculos no labirinto
    for l in range(2,20,2):
        for c in range(2,22, 7):
            H[i]=agent(m,l, c, color=COLOR.red)
            H[i].cost=10
            i += 1

   #Inserindo os obstaculos no labirinto
    for l in range(3,20,2):
        for c in range(3,22, 5):
            H[i]=agent(m,l, c, color=COLOR.red)
            H[i].cost=10
            i += 1

    #Inserindo os obstaculos no labirinto
    for l in range(4,20,2):
        for c in range(3,22, 4):
            H[i]=agent(m,l, c, color=COLOR.red)
            H[i].cost=10
            i += 1

   
    path ,c=dijkstra(m, H[1],H[2],H[3],H[4],H[5],H[6],H[7],H[8],H[9],H[10],
                        H[11],H[12],H[13],H[14],H[15],H[16],H[17],H[18],
                        H[19],H[20],H[21],H[22],H[23],H[24],H[25],H[26],
                        H[27],H[28],H[29],H[30],H[31],H[32],H[33],H[34],
                        H[35],H[36],H[37],H[38],H[39],H[40],H[41],H[42],
                        H[43],H[44],H[45],H[46],H[47],H[48],H[49],H[50],
                        H[51],H[52],H[53],H[54],H[55],H[56],H[57],H[58],
                        H[59],H[60],H[61],H[62],H[63],H[64],H[65],H[66],
                        H[67],H[68],H[69],H[70],H[71],H[72],H[73],H[74],
                        H[75],H[76],H[77],H[78],H[79],H[80],H[81],H[82],
                        H[83],H[84],H[85],H[86],H[87],H[88],H[89],H[90],
                        H[91],H[92],H[93],H[94],H[95],H[96],H[97],H[98],
                        H[99],H[100],H[101],H[102],H[103], start=(8,2))

    textLabel(m,'Custo Total do Percurso',c)

    a=agent(m,8,2,color=COLOR.cyan,filled=True,footprints=True)
    m.tracePath({a:path})

    m.run()

