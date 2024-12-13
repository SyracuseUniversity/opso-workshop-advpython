# opso-workshop-advpython

# Introduction

This tutorial covers more advanced topics in Python for data analysis. It is aimed at people who have some familiarity with Python and want to expand their knowledge of the
language and learn about tools for data analysis.

- Session 1: Introduction to Python classes
- Session 2: Advanced function signature; Exceptions
- Session 3: Data handling & manipulation
- Session 4: Statistics; curve fitting

## Installation

**If the installation fails**, you can just run it in the cloud using Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/SyracuseUniversity/ospo-workshop-advpython/HEAD)

Clone the repository and install the required packages using the following commands (use `conda` instead of `mamba` if mamba is not installed):

```bash
git clone https://github.com/SyracuseUniversity/ospo-workshop-advpython.git
cd ospo-workshop-advpython
```

Create a new conda environment (or recreate an existing one) with the required packages:

```bash
mamba env create -f environment.yml
```

or if you don't have mamba installed:

```bash
conda env create -f environment.yml
```

If you already have the environment created, you can update it with:

```bash
mamba env update --file environment.yml --prune
```

Activate the environment by running:

```bash
mamba activate advanced-python
```

Finally, start Jupyter by running:

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

for a slightly different experience

### If all installs fail

Alternatively, you can also use colaboratory to run the notebooks. Therefore, open the link https://colab.research.google.com/ and select the "GitHub" tab. Enter the URL of this
repository (https://github.com/SyracuseUniversity/ospo-workshop-advpython) and select the notebook you want to run.

## Credits

Parts of this tutorial [LHCb analysis essentials](https://github.com/hsf-training/analysis-essentials) tutorials, from
the [Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) and from J.R.
Johansson [Python lectures](http://github.com/jrjohansson/scientific-python-lectures)
