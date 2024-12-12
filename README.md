# opso-workshop-advpython


# Introduction

This tutorial covers more advanced topics in Python for data analysis. It is aimed at people who have some familiarity with Python and want to expand their knowledge of the language and learn about tools for data analysis.

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

Create a new conda environment with the required packages:

```bash
mamba env create -f environment.yml
```

If you already have the environment created, you can update it with:

```bash
mamba env update --file environment.yml --prune
```

or recreate it with:

```bash
mamba env create -f environment.yml -y
```

Activate the environment by running:

```bash
mamba activate advanced-python
```



## Credits

Parts of this tutorial [LHCb analysis essentials](https://github.com/hsf-training/analysis-essentials) tutorials and from the [Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/). Many thanks to the authors for making their work available.