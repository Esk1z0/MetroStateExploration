class Node:
    def __init__(self):
        self.__int = 0
        self.__sucessors = [(Node)]
        self.__name = ""
        self.__line = [(str)]
        self.__costNextStation = [(int)]
        
    def getInt(self):
        return self.__int
    def setInt(self, val):
        self.__int = val
    
    def getSucessors(self):
        return self.__sucessors
    def addSucessor(self, node):
        self.__sucessors.append(node)
    def delSucessor(self, identifier):
        if(identifier is int):
            self.__delSucessorInt(identifier)
        elif(identifier is str):
            self.__delSucessorStr(identifier)
    def __delSucessorInt(self, identifier):
        for node in self.__sucessors:
            if node.getInt() == identifier:
                self.__sucessors.remove(node)