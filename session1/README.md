# Object Oriented Programming with Python

The `tutorial.ipynb` provides an introduction to Python classes (we will do this together in the workshop). The exercises below illustrate some of the concepts discussed in the tutorial. If you get stuck, solutions for each problem can be found in the `.solution{X}.py` file where `{X}` corresponds to the problem number.

*Note:* exercises 3-5 require `numpy` to be installed. If you have not installed it yet, you can do so by running the following after activating your conda environment:

```bash
conda install -c conda-forge -y numpy
```

## Exercises

### 1. Scope practice

What's wrong with the following code? Fix it.

```python
x = 10

def f(m, b):
    return m*x + b

print(f(1, 2))

for x in [1, 2, '']:
    print(x)

print(f(3,4))
```

### 2. Simple class construction

Construct a class called `Simple` that takes in a single parameter at initialization and saves it as an attribute called `param`. Add to the class a function called `print` that when called prints to screen `The parameter is ` followed by the parameter. For example, you should be able to initialize the class and do the following:
```
>>> simple = Simple(10)
>>> simple.print()
'The parameter is 10'
```

### 3. Class construction

In this directory there is a JSON file called `data.json`. It contains two sets of data called `x` and `y`. The following function will load the data into memory as a dictionary of numpy arrays:
```python
import json
import numpy

def load(filename):
    with open(filename, 'r') as fp:
        data = json.load(fp)
    # convert to arrays
    for p in data:
        data[p] = numpy.array(data[p])
    return data
```

Once the data is loaded, the following function will write it back out to a CSV file:
```python
def writecsv(filename, data, delim=','):
    params = list(data.keys())
    numpy.savetxt(filename, numpy.vstack([data[p] for p in params]).T,
                  header=delim.join(params),
                  delimiter=delim, fmt='%.2f') 
```

Write a class called `JSONLoader` that takes the filename upon initialization and stores it as an attribute, along with a data attribute initially set to `None`. Add to the class a function similar to `load` that will load the stored filename and store the data dictionary to the `data` attribute. Also add to the class a function similar to `writecsv` that will write the stored data to a CSV file. When complete, you should be able to initialize and use the class like so:

```python
>>> js = JSONLoader('data.json')
>>> js.load()
>>> print(js.data)
{'x': array([-2. , -1.6, -1.2, -0.8, -0.4,  0. ,  0.4,  0.8,  1.2,  1.6]),
 'y': array([0.14, 0.28, 0.49, 0.73, 0.92, 1.  , 0.92, 0.73, 0.49, 0.28])}
>>> js.writecsv('data.csv')
```
The last line should result in a file called `data.csv` to be written containing the data with comma separated columns.

### 4. Inheritance

Write a class that called `JSONData` inherits from the `JSONLoader` class you created in the previous exercise and adds to it a function called `weighted_mean` that will calculate `sum(x*y)/sum(y)` on the data dictionary's `x` and `y` elements. When complete, you should be able to do the following:
```python
>>> jsdata = JSONData('data.json')
>>> jsdata.load()
>>> jsdata.weighted_mean()
np.float64(0.0)
```

### 5. Abstract base classes

In the directory there is another file called `data.npy`. This contains the same data as in `data.json`, but it's in a different file format. Here, we will write a class called `NPYData` that can load this type of file, and provide the same API as the `JSONData` class you wrote above. To do that, we'll first define an abstract base class that contains all the common methods between the `JSONData` and `NPYData`, except for the `load` function. We'll then redefine the `JSONData` class to use the abstract base class, and create the `NPYData` class to do the same.

**a.** Create an abstract base class called `BaseData` that has the same `__init__`, `writecsv` and `weighted_mean` functions you wrote for `JSONLoader` and `JSONData` above, and that makes `load` an `abstractmethod`. (You'll need to import `ABC` and `abstractmethod` from the `abc` module to do this.) When complete, it should not be possible to initialize this class. If you try it, you should get the following error:
```
TypeError: Can't instantiate abstract class BaseData without an implementation for abstract method 'load'
```

**b.** Recreate the `JSONData` class by inheriting from `BaseData` and adding to it the `load` function you created for `JSONLoader` above. When complete, you should be able to initialize and use `JSONData` in the same manner as in exercise 4 above, and get the same result.

**c.** Now create the `NPYData` class that also inherits from `BaseData` but implements it's own `load` function that can read the `data.npy` file and store it as a dictionary, as you did with `JSONData`. The `load` function should have the something like the following in it:
```python
data_array = numpy.load(filename)
data = {'x': data_array[:,0], 'y': data_array[:,1]}
```
Here, `filename` is `data.npy`. When complete, you should be able to initialize and use `NPYData` the same way you use `JSONData`:
```python
>>> npdata = NPYData('data.npy')
>>> npdata.load()
>>> npdata.weighted_mean()
np.float64(0.0)
>>> npdata.writecsv('data_from_npy.csv')
```
This is the advantage of using abstract base classes: you can define different classes that can do different things while maintaining the same API.
