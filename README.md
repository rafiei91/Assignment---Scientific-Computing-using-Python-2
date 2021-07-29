# Assignment---Scientific Computing using Python-1 (PhD-Python-1)

The repository containing the project assignment for the PhD course “Scientific Computing using Python, part 1”, held at Aalborg University (June 2021)

Author: **Mehdi Rafiei Foroushani**

Repository's link: **https://github.com/rafiei91/Assignment---Scientific-Computing-using-Python-1**

## Program explanation

The program is developed to solve the Lorenz attractor model that is based on three coupled first order Ordinary Differential Equations (ODEs). 

The program solve it by use of simple Newton Euler algorithm for 5 different parameters values, known as case1 to case5. Also, a testing is provided for the code.

## Files & Folders

As it can be seen in the tree view of the directory, the repository includes 3 files, 1 python code, and 2 text files.

The text files include the "requirement.txt" file that has the required tools to be installed for the main code execution and the "README.md" file that is these notes.

Among the folders, the case folder includes 5 case codes that represent all 5 defined cases on the project with different parameters, and also has one "\__init__\" file which is used to import the defined function in case1 on the testing phase.

The other folder is "lorenz" one that includes the required lorenz related codes to solve the problem, save the results, and plot the outputs.

Finally, the last folder contains the "test" code.

Also, in each folder, anoder README file is provided to explain the functions (inputs, outputs, and any other relevent explanation).

Also, in order to have an easy and straightforward execution, a "Main.py" code file is made to run it with the required input and do the ODE solvation on each case or do the test.

```bash
│   Main.py
│   README.md
│   requirements.txt
│
├───case
│       case1.py
│       case2.py
│       case3.py
│       case4.py
│       case5.py
│       README.md
│       __init__.py
│
├───lorenz
│       filehandling.py
│       plot.py
│       README.md
│       run.py
│       solver.py
│       __init__.py
│
└───test
        README.md
        test.py
```

## Implementation

Firstly, it should be mentioned that the provided guide is for implementation on windows.

### Preparation

1. Open a commond prompet (preferly Anaconda prompt)
2. Direct to your prefered direction:
```
cd path
```
3. Clone the code on the direction:
```
git clone https://github.com/rafiei91/Assignment---Scientific-Computing-using-Python-1.git
```
4. Go to the cloned representory
```
cd Assignment---Scientific-Computing-using-Python-1
```
5. Make a conda environment:
```
conda create -n Name
```
Put your prefered environment name instead on "Name".
6. Activate the environment:
```
conda activate Name
```
7. Make sure to use python 3.8.
- Check:
```
python --version
```
- Install:
```
conda install -c anaconda python=3.8
```
8. Install the requirements:
```
conda install requirements.txt
```
### Execution

In order to execute the cases or the test, the below command must be used with some costomizations.
```
python Main.py --code_select case(or test) --case_number 1(or 2, 3, 4, 5 - if the cases are going to be executed)
```
