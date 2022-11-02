from grafo import Grafo

class heuristicSearch:

    __grafo =  Grafo
    __origin = int
    __dest = int
    __path = []
    __printProcess = False
    #constructor de clase    
    def __init__(self, orig = 0, dest = 0):
        self.__grafo =  Grafo
        self.__origin = orig
        self.__dest = dest
        self.__path = []
        self.__printProcess = False
        
    def __str__(self):
        return self.__grafo.__str__()
        
    def initGraph(self, adress, fileName, OriginStation, DestinyStation,  sepa):
        self.__grafo = Grafo(adress, fileName, OriginStation, DestinyStation, sepa)
                
    #metodos setter, getter y deleter
    #de grafo
    @property
    def grafo(self):
        return self.__grafo.__realcionesStr
    @grafo.setter
    def set_grafo(self, grafo):
        self.__grafo = grafo
    @grafo.deleter
    def grafo(self):
        del self.__grafo
        
    #de origen
    @property
    def origin(self):
        return self.__origin
    @origin.setter
    def set_origin(self, val):
        if(type(val) == str):
            self.__setoriginstr(val)
        elif(type(val) == int):
            self.__setoriginint(val)
            
    def __setoriginstr(self, val):
        self.__origin = self.__grafo.convertToInt(val)
        
    def __setoriginint(self, val):
        self.__origin = val
        
    @origin.deleter
    def origin(self):
        del self.__origin
        
    #de destino
    @property
    def dest(self):
        return self.__dest
    @dest.setter
    def set_dest(self, val):
        if(type(val) == str):
            self.__setdeststr(val)
        elif(type(val) == int):
            self.__setdestint(val)
            
    def __setdeststr(self, val):
        self.__dest = self.__grafo.convertToInt(val)
        
    def __setdestint(self, val):
        self.__dest = val
    @dest.deleter
    def dest(self):
        del self.__dest
        
    #de path
    @property
    def path(self):
        return self.__path
    @path.setter
    def path(self, val):
        self.__path = val
    @origin.deleter
    def path(self):
        del self.__path    

    #de imprimir proceso  
    @property 
    def printProcess(self):
        return self.__printProcess
    @printProcess.setter
    def set_PrintProcess(self, val):
        self.__printProcess = val 

    
    
    
    
    #utilidades aparte
    #obtener el nombre de la estacion por su int
    def getStation(self, val):
        return self.__grafo.convertToStr(val) 
    
    #saber dónde está el resultado
    def findCorrect(array, nodoFinal):
        i = 0
        resul = -1
        while((resul == -1) and (i < len(array))):
            if(heuristicSearch.end(array[i], nodoFinal)):
                resul = i
            i += 1
        return resul
      
    #extrae los nodos siguientes del último nodo y lo inserta dentro del path
    def expand(self, path):
        expansion = self.__grafo.getSucessorsList(path)
        nuevos = []
        for n in expansion:
            if not (n in path):
                nuevos.append([n]+path)
        return nuevos
    
    def insertMetroLines(self, path, name):
        resul = []
        resul.append(path[0])
        for i in  range(len(path) - 1):
            aux = self.__amplitudeNoPrint(path[i], path[i+1])
            resul.append(aux[1:])
        self.__grafo.insertLines(resul, name)
    
    
    
    
    
    
    #saber si ha terminado la busqueda
    def end(vector, nodofinal):
        if(isinstance(vector, int)):
            heuristicSearch.endNum(vector, nodofinal)
        elif(isinstance(vector[0], int)):
            return heuristicSearch.endList(vector, nodofinal)
        elif(isinstance(vector[0], list)):
            return heuristicSearch.endArray(vector, nodofinal)
    
    def endNum(n, nodoFinal):
        return (n == nodoFinal)
    
    def endList(lista, nodoFinal):
        resul = False
        i = 0
        while ((not resul) and i < len(lista)):
            resul = heuristicSearch.endNum(lista[i], nodoFinal)
            i += 1    
        return resul
    
    def endArray(lista, nodoFinal):
        resul = False
        i = 0
        while ((not resul) and i < len(lista)):
            resul = heuristicSearch.endList(lista[i], nodoFinal)
            i += 1    
        return resul
    
    
    
    #Algoritmos
    
    #busqueda en profundidad
    def depth(self):
        if(self.__printProcess):
            return self.__depthPrint()
        else:
            return self.__depthNotPrint()
        
    def __depthPrint(self):
        cp = [[self.__origin]]
        lengthSeacrhinglist = []
        while cp:
            print("\n",cp)
            if(heuristicSearch.end(cp, self.__dest)):
                print("Length of SearchList: " + str(lengthSeacrhinglist))
                return list(reversed(cp[heuristicSearch.findCorrect(cp, self.__dest)]))
            expansion = self.expand(cp[0])
            cp = expansion + cp[1:]
            lengthSeacrhinglist.append(len(cp))
        
        return []
    
    def __depthNotPrint(self):
        cp = [[self.__origin]]
        while cp:
            if(heuristicSearch.end(cp, self.__dest)):
                return list(reversed(cp[heuristicSearch.findCorrect(cp, self.__dest)]))
            expansion = self.expand(cp[0])
            cp = expansion + cp[1:]
        
        return []
    
    
    #busqueda en amplitud
    def amplitude(self):
        if(self.__printProcess):
            return self.__amplitudePrint()
        else:
            return self.__amplitudeNotPrint()
    
    def __amplitudePrint(self):
        cp = [[self.__origin]]
        lengthSeacrhinglist = []
        while cp:
            print("\n",cp)
            if(heuristicSearch.end(cp, self.__dest)):
                print("Length of SearchList: " + str(lengthSeacrhinglist))
                return list(reversed(cp[heuristicSearch.findCorrect(cp, self.__dest)]))
            expansion = self.expand(cp[0])
            cp = cp[1:] + expansion
            lengthSeacrhinglist.append(len(cp))
        return []
    def __amplitudeNotPrint(self):
        cp = [[self.__origin]]
        while cp:
            if(heuristicSearch.end(cp, self.__dest)):
                return list(reversed(cp[heuristicSearch.findCorrect(cp, self.__dest)]))
            expansion = self.expand(cp[0])
            cp = cp[1:] + expansion
        return []
    
    def __amplitudeNoPrint(self,firstNode, finalNode):
        cp = [[firstNode]]
        while cp:
            if(heuristicSearch.end(cp, finalNode)):
                return list(reversed(cp[heuristicSearch.findCorrect(cp, finalNode)]))
            expansion = self.expand(cp[0])
            cp = cp[1:] + expansion
        return []
    