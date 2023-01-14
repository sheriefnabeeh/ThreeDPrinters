import json

class FileLoader:

    _fileName = ""
    
    def save(self, data):

        with open(self._fileName) as cache:
            _cache = json.load(cache)
            
            _cache = data

        with open(self._fileName, "w") as cache:
            json.dump(_cache, cache, indent=4)


    def fetchDataFromJsonFile(self):

        with open(self._fileName, "r") as cache:
             data = json.load(cache)               
        return data
    
    def fetchDataFromFile(self):
        data = {}
        with open(self._fileName) as cache:
            for line in cache.readlines():
                if(not line.strip()):
                    continue
                keyValueList = line.rstrip("\n").split("=")
                if(len(keyValueList) != 2):
                    print ("key value in txt file not correct, values: " + keyValueList[0])
                    break
                data[keyValueList[0]] = str(keyValueList[1]).replace('"', '').strip() 
                
        return data
            
    def __init__(self, fileName) -> None:
        self._fileName = fileName
