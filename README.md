# An approach to slow event-related Flanker Task

Congratulations, you have found the repository in which you can now easily participate in the Flanker Task experiment and contribute data to our project!
This project is all about getting in contact with, participating in and understanding results of the ***slow event-related Flanker Task*** experiment as it was introduced and first run by Eriksen.

## Table of Files:
- README.md            -> this is what you are currently reading and which shall give you an overview about what to expect
- menu.py              -> the file in which all applications come together
- FlankerExperiment.py -> run the experiment on your own contribute data points to our data collection
- DataWrangling.py     -> collection of funtions to construct the plots you can also look at in DataSummary.ipynb
- PersonalSummary.py   -> another collection of functions to construct plots with which you can look at your own results
- DataSummary.ipynb    -> have a look at data tidying and some summary plots based on the data we have!
- data/data.csv        -> our whole data collection
- requirements.txt     -> helps you to check whether you have and, if necessary, download or update the packages required to run all code chunks in this repository's files


## Here is what we used
Apart from basic packages like python's numpy and pandas package for data wrangling, we used plotnine's `ggplot`, as well as `matplotlib` to construct the plots that you can check out in the file **DataSummary.ipynb**. If you are already familiar with the data science programming language ***R***, getting along with the code might be child's play for you! Bar plots, violin plots or jittering data points can all be very easy with ggplot, since it does a lot of things implicitly, which means you do not have to state how the program shall proceed. Forthermore, matplotlib was used for one specific stacked bar plot that we were reluctant to leave out, which is why matplotlib is included here as well.

Conducting the Flanker Task experiment is done with help of the package `expyriment` in the file **FlankerExperiment.py**. It comes in handy when including stimuli that are presented on screen and enables to obtain extremely precise reaction times with a fault range of roughly 20ms. For a nice user interface, we then used the package `psychopy` in Coder-Mode in order to make everything more accessible.

## Here is what you need
### In order to make use of this code, you need to have git installed. 

For Ubuntu Linux, you can open a terminal and run `sudo apt-get install git`.

For MacOS, first install Homebrew if you don't have it already from [here](https://brew.sh/). Then run `brew install git`.

For Windows, download the .exe from [here](https://git-scm.com/download/win) and run the installer. In the install wizard, make sure that git can be used from the command prompt. Other than that, you'll probably go for the openSSL as well as Windows default console as terminal emulator options.

### After that, you might want to install conda like this:
Download the correct installer for your system from [here](https://docs.conda.io/en/latest/miniconda.html). This will depend on your operating system and whether your have a 32-bit or 64-bit system (on Linux, this can be determined by running `getconf LONG_BIT`).

#### For Ubuntu Linux and Mac OS
To start the installer, navigate to the place where you downloaded the file to in the terminal and run  `bash Miniconda3-latest-Linux-x86_64.sh`. If the file you downloaded is named differently, type that file name after bash instead. Most options can just be answered with yes, however you should insist on adding conda to your PATH if the installer asks you.

#### For Windows
Start the graphical installer, it should guide through the installation process. If you don't have another Python installation already installed, you can safely add Python to your %PATH%, such that you can use it from your normal cmd-shell. In any case, you should have a program named ***"Anaconda prompt"*** installed afterward, which you can find with the start menu. If you didn't add it to your %PATH% as instructed above, you need to run all conda-commands in the Anaconda prompt, otherwise you can use the normal cmd. Make sure to not use the PowerShell, as some conda-commands won't work properly there.

If you decide to use an environment later on, make sure you have admin rights for the terminal you use. To do that, hit Win type cmd, right-click the first option Command Prompt, and select Open as Administrator.

### Updating conda
Before you continue the installation process, you need to update conda in order to install the environment. Do so by using the command `conda update conda`

### Testing your Conda and Python installations
Check that you now have a working Conda installation by running `conda --version`.

Check that you now have a working Python installation by running ` python --version`.

Now make sure that you use **Python version 3.7 or higher** on your machine and install the packages listed in the file **requirements.txt**. It is, therefore, best to run the installation of all packages via a command like `pip install -r requirements.txt`. This command reads out all the packages as well as the corresponding version you need in order to avoid encountering hardships and installs them right away. Apart from that, the only thing you need to know for working with this repository is what you can do with it, which is the next point.

## Here is how to use this repo
This repo gives you access to many different files, be they basic python code files(.py), python notebooks(.ipynb), data-files(.csv) and more. The data we obtained from an official run, as well as the data everybody contributes can be found in the csv-file of the folder /data. You might want to have a brief look at it or peak at the official files on the Internet (see [this](https://exhibits.stanford.edu/data/catalog/qc551wm3640)).

In order to run any python script in this repo, go to the directory in which the experiment script is saved and use the basic command `python SCRIPTNAME.py`. This works for runnng the experiment as well as running the psychopy interface.

## Here is what you can do
This respository, as already mentioned multiple times, gives you the chance to participate in theexperiment and contribute data to out project. What you might ask yourself now are questions like: `what is the slow event-related Flanker Task?` and `what knowledge gain does this experiment bring?`. The Flanker Task is a reaction task in which it is neccessary to press a button depending on the stimulus that is presented on the screen. These stimuli consist of arrays of "arrows" pointing to either the right or the left and can look like "<<<<<" (for which you would have to press the left-arrow key) or "<<><<" (for which you would have to press the right-arrow key). These stimuli can be categorized in the categories ***congruent*** and ***incongruent*** and you already combined very well that the key you have to press depends on whether the middle arrow points to the left or right.

In order to get a more detailed description of the Flanker Task experiment and see some plots about what results we can obtain, see the file **DataSummary.ipynb**. There, we include information about experiment conduction and present a showcase of data tidying and some basic summary statistics.
But there is more to discover! Run the experiment on your own or just look at the python script

## Data references / Credits

Kelly, A.M., Uddin, L.Q., Biswal, B.B., Castellanos, F.X., Milham, M.P. (2008). Competition between functional brain networks mediates behavioral variability. Neuroimage, 39(1):527-37


Mennes, M., Kelly, C., Zuo, X.N., Di Martino, A., Biswal, B.B., Castellanos, F.X., Milham, M.P. (2010). Inter-individual differences in resting-state functional connectivity predict task-induced BOLD activity. Neuroimage, 50(4):1690-701. doi: 

10.1016/j.neuroimage.2010.01.002. Epub 2010 Jan 15. Erratum in: Neuroimage. 2011 Mar 1;55(1):434

Mennes, M., Zuo, X.N., Kelly, C., Di Martino, A., Zang, Y.F., Biswal, B., Castellanos, F.X., Milham, M.P. (2011). Linking inter-individual differences in neural activation and behavior to intrinsic brain dynamics. Neuroimage, 54(4):2950-9. doi: 

10.1016/j.neuroimage.2010.10.046

## A last word about us
We are a group of three Cognintive Science students at the university of Osnabrueck and what you can discover in this repository is, in fact, the final project we did for the course `Scientific Programming in Python`. There might be a lot of things to be improved, but we would like to ask you to be not too hard on us, though we would love to get honest advice on how to improve our coding and documentation skills, of course! Thanks for sticking with us to the end of this README-file and we hope you can have an interesting time browsing around! :)

Greetings from our GitHub-profiles
- [fkirsch](https://github.com/Kirschberg32)
- [lahellmann](https://github.com/lahellmann)
- [mejansen](https://github.com/mejansen)

