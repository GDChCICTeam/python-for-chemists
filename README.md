# Python for Chemists [![Build Status](https://travis-ci.org/GDChCICTeam/python-for-chemists.svg?branch=master)](https://travis-ci.org/GDChCICTeam/python-for-chemists)
This repository stores the main resources of a workshop that was created to serve as
crash-course introduction to Python for natural scientists. More specificly,
chemists and pharmaceutical scientists on masters and graduate level.


# Ready to use with Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GDChCICTeam/python-for-chemists/master)
In case you are completely new to programming and want to play with the examples
used in the Jupyter Notebooks, it is recommended to check out the provided Binder (icon next to the title of this section).

When you click on the Binder icon a page is going to open where you can instantly use the notebooks of this repository.
It may take a while for Binder to set up the environment to use the Jupyter Notebooks. However, this is the easiest way
to use and play with the provided notebooks.

# Set up your environment with *conda* yourself.
The repository contains a file `environment.yml` that specifies all needed requirements for the *conda* environment to
run the Jupyter notebooks and to work through the exercises. The following steps are necessary to set up your *conda*
environment.
 - [install *Anaconda*](#install-anaconda)
 - [create a *conda* environment](#create-a-conda-environment)
 - [activate the environment](#activate-the-environment)
 - [start the Jupyter notebook server](#start-the-jupyter-notebook-server)

## Install *Anaconda*
For each operating system an installation manual can be found [on the *Anaconda* website](https://docs.anaconda.com/anaconda/install/).
For  *Debian* and derived distributions *Ubuntu* the following can be done:
### Install prerequisites for *Anaconda*
```bash
sudo apt-get install < anaconda_requirements.txt
```
### Install *Anaconda*
Get the installer for *Linux* [here](https://www.anaconda.com/distribution/#linux).
In case you downloaded the installer to the standard *Downloads* folder and for the installer
version `Anaconda3-2019.10`, type the following:
```bash
bash ~/Downloads/Anaconda3-2019.10-Linux-x86_64.sh
```
A few prompts will pop up. You can type `yes` in all cases. But be careful, one will modify your `bash` scripts. If you
select `no`, you can still let *Anaconda* change the `shell` variables later with:
```
source <path to conda>/bin/activate
conda init <type of shell> # bash, zsh, sh, ...
```
In case you affirmatively stepped through each prompt, you can now source your `bashrc` file:
```bash
source ~/.bashrc
```
and initialize *Anaconda* with:
```bash
conda init
```
For more information, other operating systems or troubleshooting please refer to the [*Anaconda*
installer site](https://www.anaconda.com/distribution/#linux).

## Create a *conda* environment
Now comes the provided `environment.yml` file into play. It lists all necessary packages needed
to use the Jupyter notebooks and the Python files in the Exercises and Solutions folders. Therefore,
you can simply type (assuming your `shell` has been set up properly by *Anaconda* in the step before):
```bash
conda env create -f environment.yml
```
This will download a bunch of packages and set up the *Anaconda* virtual environment.
## Activate the environment
As soon as the virtual environment is created properly (last step) you can start it with:
```bash
conda activate introductiontopython
```
## Start the Jupyter notebook server
Last but not least you will have to start the Jupyter notebook server with:
```bash
jupyter notebook
```

# Resources
The course that resides here in this repository is only the beginning of your journey. There are
many resources online that are a good reference point to dive deeper into programming with
Python. We have tried to compile a list of those resouces we find most reasonable.

### Software Carpentry
[Software carpentry](https://software-carpentry.org/) is a volunteer project aiming to teach
researchers the computing skills they need to get more done in less time and with less pain.
  * [Software Carpentry](https://software-carpentry.org/lessons/)

### Massive Open Online Courses (MOOCs)
MOOCs are online platforms that are designed to be like university courses with lectures and
assignments (sometimes graded).
  * [Coursera Python Courses](https://www.coursera.org/courses?query=python)
  * [edX Python Courses](https://www.edx.org/learn/python)

### Codeacademy
Codeacademy is an online resource for many programming languages and concepts. They provide an
interface with three columns (task | code | output) that makes coding fun and is easy to use.
Unfortunately, learning Python3 is a pro feature. Python2 is not supported anymore since
January 2020. Nonetheless, it is a good starting point and the differences can be learned pretty
quickly. Just make sure to not start a project in Python2 anymore!
  * [Codeacademy](https://www.codecademy.com/learn/learn-python)

###  Molecular Sciences Software Institute (MolSSI)
The [MolSSI](molssi.org) has prepared a Python course as well that goes a beyond the material that is part
of our workshop. It is a good location to start about best [practices](https://molssi.org/education/best-practices/),
[unit testing](https://molssi-education.github.io/python_scripting_cms/08-testing/index.html)
and [version control](https://molssi-education.github.io/python_scripting_cms/09-git/index.html).
  * [MolSSI Python Course](https://molssi-education.github.io/python_scripting_cms/)

### TeachOpenCADD
Is a teaching platform for computer-aided drug design (CADD), using open source packages and data.
Python is only a first step to computational chemistry. Besides data crunching chemical and biological
models are widely used to predict experimental outcomes or aid in exploring chemical mechanisms.
  * [TeachOpenCADD](https://github.com/volkamerlab/TeachOpenCADD)
