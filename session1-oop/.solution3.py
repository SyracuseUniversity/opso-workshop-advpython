import json
import numpy

class JSONLoader:
    
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def load(self):
        with open(self.filename, 'r') as fp:
            data = json.load(fp)
        # convert to arrays
        for p in data:
            data[p] = numpy.array(data[p])
        self.data = data

    def writecsv(self, filename, delim=','):
        params = list(self.data.keys())
        numpy.savetxt(filename, numpy.vstack([self.data[p] for p in params]).T,
                      header=delim.join(params),
                      delimiter=delim, fmt='%.2f')


### Test:
js = JSONLoader('data.json')
js.load()
print(js.data)
js.writecsv('data.csv')
