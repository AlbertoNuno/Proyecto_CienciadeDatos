# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial.distance as sc
from myLib import mylib
import string
#%%definición de funciones 
def count_values(x,parameter):
    counter=0
    size=len(x)
    for i in range (size):
        if(x[i]==parameter):
            counter =counter+1  
    return counter 

#%%importacion de datos
 '../Data/datos_proyecto1.csv'
data = pd.read_csv( '../Data/datos_proyecto1.csv', encoding ='latin1')
data = data.iloc[:,0:7]

#%%repote de calidad de los datos
dqr= mylib.dqr(data)
#%%eliminación de datos nulos
data=data.dropna()
#%%lEstadísticas de los datos

plantel = (data['Plantel'])
modelo = data['Modelo educativo']
clave_c= data['Clave de la carrera']
carrea = data['Carrera Profesional Tecnico -Bachiller']
matricula = data['Matricula']
periodo = data['Periodo']
count_values(plantel,'Guadalajara II')
results_array=np.zeros(20)

#%%
for i in range(len(results_array)):
    counter =0
    for j in range(75):
        if(j<74):
            if(plantel[j]== plantel[j+1]):
                 counter=counter+1
            elif(plantel[j]!= plantel[j+1]):
                 results_array[i]=counter
                 
        else:
            if(plantel[j] == plantel[j-1]):
                counter=counter+1
        results_array[i]=(counter)  
        counter=0
                 
 #%%
gdl =count_values(plantel,'Guadalajara I')
lic =count_values(plantel,'Lic. Francisco Medina Ascencio, Mexicano-Italiano')
ar=count_values(plantel,'Arandas')
vta = count_values(plantel,'Puerto Vallarta')
gdl2 =count_values(plantel,'Guadalajara II')
tla =count_values(plantel,'Tlaquepaque')
jalos=count_values(plantel,'Jalostotitlan')
lagos=count_values(plantel,'Lagos de Moreno')
jo_ma =count_values(plantel,'Jose Ma. Martínez R- Tamazula')
aca=count_values(plantel,'Acatlan de Juarez')
gdl3 =count_values(plantel,'Guadalajara III')
ton = count_values(plantel,'Profa. Idolina Gaona de Cosio- Tonala')
zp =count_values(plantel,'Zapopan')
LB =count_values(plantel,'La Barca')
aj=count_values(plantel,'Ajijic-Chapala')
vta=count_values(plantel,'Puerto Vallarta II')              
tpa=count_values(plantel,'Tapalpa')   
enf = count_values(plantel,'Academia Municipal de Enfermeria')
maz= count_values(plantel,'Mazamitla')

eje_y = np.zeros(10)
for i in range(len(eje_y)):
    eje_y[i]=i+1

    
    #%%
con=0   
j=0 
def coun_uniques(series,string):
    counter=0
    for i in range(len(series)):
        if(plantel[i]==series):
            counter=counter+1
        j=j+1
    return con        

for j in range(len(plantel)):
    if(plantel[j] =='Guadalajara II'):
         con=con+1
            
    j=j+1
         
    
    
    




