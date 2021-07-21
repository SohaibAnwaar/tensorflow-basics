[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](http://ansicolortags.readthedocs.io/?badge=latest)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![CircleCI](https://circleci.com/gh/google/pybadges.svg?style=svg)](https://circleci.com/gh/google/pybadges)
![versions](https://img.shields.io/pypi/pyversions/pybadges.svg)
![versions](https://camo.githubusercontent.com/7d880f217d558a5183c9af2332c2517b00a6c4ff0b29297bd6881dd5bf867887/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f726174696e672d2545322539382538352545322539382538352545322539382538352545322539382538352545322539382538362d627269676874677265656e)


<h2 style="color:#FFFF99"> Setup Things </h2>

So before diving into development lets first setup things, We need conda, jupyter-notebook (you can use other IDE'S), python, TensorFlow

<br>

<h2 style="color:#add8e6"> Linix Setup (18.04) </h2>
<br>
First, you need to install anaconda you can get help from this website

[Install anaconda](https://docs.anaconda.com/anaconda/install/linux/)

Okay! so after anaconda installation, confirm that your conda is working fine, run the bash command below on your terminal

<h3 style="color:#b284be"> Input </h3>

```bash
conda --version
```

<h3 style="color:#b284be"> Output </h3>

```
conda 4.6.11
```
Okay! If you get the expected output then I think you should move forward! lol :)
So! let's make our development environment and install the required packages init

<br>


<h3 style="color:#b284be"> Make conda Environment </h3>

```bash
conda create -n tf_ python=3.6 tensorFlow jupyter
```
In simple language above command is explaining to our hardware, that I need a conda version with name **tf_**, python version 3.6 with the latest TensorFlow package and a jupyter package 

<br>

<h3 style="color:#b284be"> Flags </h3>

```
1. -n          : represents the name
2. python=3.6  : Specify your python version here
3. tensorflow  : Install the latest tensorflow (as we didn't specify any version, by default conda will install the latest version)
4. jupyter     : Jupyter notebook package to run IDE
```

if the command is successfully executed then you will get some outputs like this

```
#
# To activate this environment, use
#
#     $ conda activate tf_
#
# To deactivate an active environment, use
#
#     $ conda deactivate

```
<br>

<h3 style="color:#b284be"> Adding our environment to jupyter notebook </h3>

This part is not required but it's good to add your environment in jupyter-notebook so you can switch between environments on runtime.


+ Install ipykernal

```bash
conda install -c anaconda ipykernel
```


+ Add conda environment to jupyter notebook


```bash
conda activate tf_
python -m ipykernel install --user --name=tf_
```

In the first command, we are activating our environment and in the second command, we are just asking the ipykernal package to add our conda environment to jupyter-notebook.

<br>

<h2 style="color:#00ff99">Success</h2>

If all the things went good. Then start your jupyter-notebook

```bash
jupyter notebook --port 0.0.0.0 --ip 8888 --allow-root
```