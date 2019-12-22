# Python for Chemists [![Build Status](https://travis-ci.com/GDChCIC/python-for-chemists.svg?branch=master)](https://travis-ci.com/GDChCIC/python-for-chemists)
This repository stores the main resources of a workshop that was created to serve as
crash-course introduction to Python for natural scientists. More specificly,
chemists and pharmaceutical scientists on masters and graduate level.


# Ready to use with Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GDChCIC/python-for-chemists/master)
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
 - [create a *coda* environment](#create-a-conda-environment)
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
