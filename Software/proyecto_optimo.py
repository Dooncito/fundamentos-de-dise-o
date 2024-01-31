import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 100 # puntos por pulgada con lo que se muestra
mpl.rcParams['savefig.dpi'] = 150 #puntos por pulgada con lo que se guarda la grafica

import matplotlib.pyplot as plt
#aqui va los valores de evalaucion economica eje y
e_e=[0.859,0.808,0.783,0.773,1]
#aqui va los valores de evlacion tenica eje x
e_t=[0.809,0.780,0.756,0.859,1]
#linea oblicua
l=[0,0.5,1]
plt.plot(l,l)
#alternativas de solucion
s1=plt.scatter(e_t[0],e_e[0],marker='o',color='c')
s2=plt.scatter(e_t[1],e_e[1],marker='o',color='y')
s3=plt.scatter(e_t[2],e_e[2],marker='o',color='m')
s4=plt.scatter(e_t[3],e_e[3],marker='o',color='r')
s5=plt.scatter(e_t[4],e_e[4],marker='o',color='b')
plt.xlabel('Evaluación técnica')
plt.ylabel('Evaluación económica')
plt.title('Diagrama de evaluacion')
plt.grid(True)
plt.axis([0,1,0,1])
plt.legend((s1,s2,s3,s4,s5),('Preliminar1','Preliminar2','Preliminar3','Preliminar4','Ideal'),
           loc='upper right',#ubicacion de la leyenda
           title='Alternativas de solucion' #titulo de la leyenda
           ,bbox_to_anchor=(1.35,1.0),#Cuadro que se utiliza para colocar la leyenda junto con loc
           ncol=1) #numero de columnas que tiene la leyenda
plt.savefig("diagramavdi2225.png",#ruta
            bbox_inches='tight') #Cuadro delimitador en pulgadas
plt.show()#muestra la figura
