from heuristicSearch import heuristicSearch

if __name__ == "__main__":
    direccion = "."
    h = heuristicSearch()
    h.initGraph(direccion, "Vienna subway.csv", "Start", "Stop", sepa= ";")
    print(h)
    
    h.set_PrintProcess = False
    h.set_origin = "Oberlaa"
    h.set_dest = "Leopoldau"
    
    #print(h.origin)
    #print(h.dest)
    
    resul = h.depth()
    print(resul)
    resulStr = ""
    for i in resul:
        if (not i == resul[-1]):
            resulStr += h.getStation(i) + " --> "
        else:
            resulStr += h.getStation(i)
    print(resulStr)
    
    resul = h.amplitude()
    print(resul)
    resulStr = ""
    for i in resul:
        if (not i == resul[-1]):
            resulStr += h.getStation(i) + " --> "
        else:
            resulStr += h.getStation(i)
    print(resulStr)
    
    linea1 = [0, 9, 10, 11, 13, 94]
    h.insertMetroLines(linea1, "RED")