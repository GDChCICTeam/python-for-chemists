# Python for Chemists [![Build Status](https://travis-ci.org/GDChCICTeam/python-for-chemists.svg?branch=master)](https://travis-ci.org/GDChCICTeam/python-for-chemists)
This repository contains the main resources of a workshop serving as a crash-course introduction to
Python for natural scientists. More specifically, for chemists and pharmaceutical scientists of
masters and graduate level.

## Ready to use with Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GDChCICTeam/python-for-chemists/master)
If you are completely new to programming and want to play with the examples used in the Jupyter
Notebooks, we recommend to check out the provided Binder (icon next to the title of this section).

When you click on the Binder icon, a page is going to open where you can immediately browse the
notebooks from this repository. It may take a while for Binder to set up the required environment,
but this is the easiest way to use and play with the provided notebooks.

## Set up your own environment with conda
The repository contains a file named `environment.yml`. It specifies all requirements for the
*conda* environment to run the Jupyter notebooks and everything you need to work on the exercises.
The following steps are necessary to set up your own *conda* environment:

 - [install Anaconda/Miniconda](#install-anacondaminiconda)
 - [create a *conda* environment](#create-a-conda-environment)
 - [activate the environment](#activate-the-environment)
 - [start the Jupyter notebook server](#start-the-jupyter-notebook-server)

### Install Anaconda/Miniconda
Anaconda and Miniconda are environment and package managers for Python. The difference between the
two is that Anaconda ships with a lot of commonly used packages out of the box, whereas Miniconda
only ships with the bare minimum required for environment and package management. The official
websites offer install guides for every operating system:

 - [Anaconda install guide](https://docs.anaconda.com/anaconda/install/)
 - [Miniconda install guide](https://conda.io/en/latest/miniconda.html#)

Since installing either of them on a Linux system requires some additional dependencies, we'll walk
through an example setup procedure of Anaconda for *Debian* and derived distributions like *Ubuntu*.

#### Install prerequisites for Anaconda
Download the `anaconda_requirements.txt` from this repository. Afterwards, open a terminal and enter
the following:

```bash
sudo apt-get install < anaconda_requirements.txt
```

This will install any system packages required by Anaconda. If you run a different distribution, you
will have to look up the correct package names for your package manager.

#### Install Anaconda
Get the installer for *Linux* [here](https://www.anaconda.com/distribution/#linux).

Assuming you downloaded the installer verson `Anaconda3-2019.10` to the standard *Downloads* folder,
type the following in your terminal (replace either the download folder or installer version with
the one you downloaded if necessary):

```bash
bash ~/Downloads/Anaconda3-2019.10-Linux-x86_64.sh
```

A few prompts will appear. You can type `yes` in all cases. But be careful, one of them will modify
the behavior of your `bash` scripts if you have any. If you select `no`, you can still let
Anaconda change the `shell` variables later with:

```
source <path to conda>/bin/activate
conda init <type of shell> # bash, zsh, sh, ...
```

If you accepted all prompts, you can now source your `bashrc` file:

```bash
source ~/.bashrc
```

and initialize Anaconda with:

```bash
conda init
```

For more information, other operating systems or troubleshooting, please refer to the [Anaconda installer site](https://www.anaconda.com/distribution/#linux).

### Create a conda environment
Now the provided `environment.yml` file comes into play. It lists all necessary packages needed to
use the Jupyter notebooks and the Python files in the Exercises and Solutions folders. Assuming you
set up your conda installation properly, you can create a new environment with all required packages
like this:

```bash
conda env create -f environment.yml
```

### Activate the environment
As soon as the virtual environment is created properly (see last step) you can activate it with:

```bash
conda activate introductiontopython
```

All the necessary packages should now be available.

### Start the Jupyter notebook server
Last but not least, you will have to start the Jupyter notebook server with:

```bash
jupyter notebook
```

# Resources
The workshop that resides in this repository is only the beginning of your journey. There are many
resources online that are a good reference point to dive deeper into programming with Python. We
have tried to compile a short, opinionated list of some resouces we think are a good start.

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
Codeacademy is an online resource for many programming languages and concepts. They
provide an interface with three columns (task | code | output) that makes coding fun and is easy to
use.  Unfortunately, learning Python3 is a pro feature and Python2 is officially deprecated since
January 2020. Nonetheless, it is a good starting point and the differences between the two language
versions can be learned pretty quickly. Just make sure to not start a project in Python2 anymore!

  * [Codeacademy](https://www.codecademy.com/learn/learn-python)

###  Molecular Sciences Software Institute (MolSSI)
The [MolSSI](molssi.org) has prepared a Python course as well. It goes beyond the material that is
part of our workshop. It is a good location to start learning about [best practices](https://molssi.org/education/best-practices/),
[unit testing](https://molssi-education.github.io/python_scripting_cms/08-testing/index.html)
and [version control](https://molssi-education.github.io/python_scripting_cms/09-git/index.html).

  * [MolSSI Python Course](https://molssi-education.github.io/python_scripting_cms/)

### TeachOpenCADD
Is a teaching platform for computer-aided drug design (CADD), using open source packages and data.
Python is only a first step to computational chemistry. Besides data crunching, chemical and
biological models are widely used to predict experimental outcomes or aid in exploring chemical
mechanisms.

  * [TeachOpenCADD](https://github.com/volkamerlab/TeachOpenCADD)
