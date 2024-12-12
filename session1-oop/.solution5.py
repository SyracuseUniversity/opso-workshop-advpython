import json
import numpy
from abc import ABC, abstractmethod

### 5.a
class BaseData(ABC):
    
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    @abstractmethod
    def load(self):
        return

    def writecsv(self, filename, delim=','):
        params = list(self.data.keys())
        numpy.savetxt(filename, numpy.vstack([self.data[p] for p in params]).T,
                      header=delim.join(params),
                      delimiter=delim, fmt='%.2f')

    def weighted_mean(self):
        x = self.data['x']
        y = self.data['y']
        return (x*y).sum()/y.sum()



### 5.b
class JSONData(BaseData):

    def load(self):
        with open(self.filename, 'r') as fp:
            data = json.load(fp)
        # convert to arrays
        for p in data:
            data[p] = numpy.array(data[p])
        self.data = data


### Test
print('5.b test:')
jsdata = JSONData('data.json')
jsdata.load()
print(jsdata.weighted_mean())
jsdata.writecsv('data_from_json.csv')


### 5.c
class NPYData(BaseData):

    def load(self):
        data_array = numpy.load(self.filename)
        self.data = {'x': data_array[:,0], 'y': data_array[:,1]}


### Test
print('5.c test:')
npdata = NPYData('data.npy')
npdata.load()
print(npdata.weighted_mean())
npdata.writecsv('data_from_npy.csv')
