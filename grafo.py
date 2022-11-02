import pandas as pd
import os


class Grafo:
    def __init__(self):
        self.__stations = []
        self._connectionInt = [[]]
        self.__connectionStr = [[]]
        self.__graph = [[]]
        self.__metroLines = [[]]
        self.__metroLinesNames = []
        
    def __init__(self, adress, fileName, Start, Stop, sepa = ','):
        self.__stations = []
        self._connectionInt = []
        self.__connectionStr = [[],[]]
        self.__graph = []
        self.__metroLines = [[]]
        self.__metroLinesNames = []
        
        
        os.chdir(adress)
        data = pd.read_csv(adress + "/" + fileName, sep = sepa)
        
        entradas = data[Start].to_list()
        salidas = data[Stop].to_list()
        self.__connectionStr[0] = entradas
        self.__connectionStr[1] = salidas

        self.__stations = self.uniqueValues(entradas + salidas)
        
        for i in range(len(self.__connectionStr[0])):
            self._connectionInt.append([self.convertToInt(self.__connectionStr[0][i]), self.convertToInt(self.__connectionStr[1][i])])
         
        for i in range(len(self.__stations)):
            j = []
            self.__graph.append(j)
        for [o,d] in self._connectionInt:
            self.__graph[o].append(d)
            self.__graph[d].append(o)
            
    def __str__(self):
        return self.__getNamesGrafo()
    
    
    
    
    
    #getter, setter y deleter 
    #estaciones    
    @property
    def stations(self):
        return self.__stations
    @stations.deleter
    def stations(self):
        del self.__stations
        
    #relaciones en Texto
    @property
    def conectionStr(self):
        return self.__connectionStr
    @conectionStr.deleter
    def conectionStr(self):
        del self.__connectionStr
        
    #relaciones en enteros
    @property
    def connectionInt(self):
        return self._connectionInt
    @connectionInt.deleter
    def connectionInt(self):
        del self._connectionInt
        
    #del grafo
    @property
    def graph(self):
        return self.__graph
    @graph.setter
    def graph(self, grafo):
        self.__graph = grafo
    @graph.deleter
    def graph(self):
        del self.__graph
    
    #los get de Sucesores    
    def getSucessors(self, valor):
        return self.__graph[valor]
    
    def getSucessorsList(self, vector):
        return self.__graph[vector[0]]
    
    def getSucessorsArray(self, array):
        return self.__graph[array[0][0]]
    
    
    
    
    
    
    
    
    #devuelve los valores unicos de una lista
    def uniqueValues(self, lista):
        aux = []
        for x in lista:
            if(x not in aux):
                aux.append(x)
        return aux
    
    #devuelve los nombres de las estaciones pasandolo de int a string
    def __getNamesGrafo(self):
        resul = ""
        for i in range(len(self.__graph)):
            resul += "\n" + str(i) + " " + self.convertToStr(i)
            for j in self.__graph[i]:
                resul += "\n  --> " + str(j) + " " +  self.convertToStr(j)
        return resul
    
    #devuelve el int asociado a una estacion
    def convertToInt(self, text):
        k = 0
        while(not text == self.__stations[k]):
            k += 1
        
        return k
        
    #devuelve el nombre de una estacion en base a su int
    def convertToStr(self, num):
        return self.__stations[num]
    
    
    def insertLines(self, path, name):
        self.__metroLines.append(path)
        self.__metroLinesNames.append(name)
    
    