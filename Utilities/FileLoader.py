import json

class FileLoader:

    _data = {}
    _fileName = ""
    
    def save(self, data):

        with open(self._fileName) as cache:
            _cache = json.load(cache)
            
            _cache = data

        with open(self._fileName, "w") as cache:
            json.dump(_cache, cache, indent=4)


    def fetch(self):

        with open(self._fileName) as cache:
            for line in cache.readlines():
                if(not line.strip()):
                    break
                key, value = line.rstrip("\n").split("=")
                self._data[key] = str(value).replace('"', '').strip() 
                
        return self._data
            
    def __init__(self, fileName) -> None:
        self._fileName = fileName
