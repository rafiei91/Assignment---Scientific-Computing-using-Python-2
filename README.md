# Assignment---Scientific Computing using Python-2 (PhD-Python-2)

The repository containing the project assignment for the PhD course “Scientific Computing using Python, part 2”, held at Aalborg University (June 2021)

Author: **Mehdi Rafiei Foroushani**

Repository's link: **https://github.com/rafiei91/Assignment---Scientific-Computing-using-Python-2**

## Program explanation

The program is developed to acheive the Mandelbrot set in a complex domain. 

The program did it for a range of input from -2 to 1 in real space and from -1.5 to 1.5 in imagenary space. Four different versions of implementations have been used in this regard (Naive, Parallel, Vectorized, and multi-processing).

## Files & Folders

As it can be seen in the tree view of the directory, the repository includes 3 files, 1 python code, and 2 text files.

The text files include the "requirement.txt" file that has the required tools to be installed for the main code execution and the "README.md" file that is these notes.

Among the folders, the implementation folder includes 4 version codes that represent the problem with different implementation methods.

The other folder is "code_f" one that has the functions to achieve the Mandelbrot set for all 4 implementation methods, and also has one "\__init__\" file which is used to import the defined function in naive on the testing phase.

Finally, the last folder contains the "test" code.

Also, in each folder, anoder README file is provided to explain the functions (inputs, outputs, and any other relevent explanation).

Also, in order to have an easy and straightforward execution, a "Main.py" code file is made to run it with the required input and achieve the Mandelbrot set on each implementation method or do the test.

```bash
│   Main.py
│   README.md
│   requirements.txt
├───code_f
│       funcs.py
│       README.md
│       __init__.py
├───Implementations
│       multiprocessing.py
│       naive.py
│       parallel.py
│       README.md
│       vectorized.py
└───test
        README.md
        test_calc.py
```

## Implementation

Firstly, it should be mentioned that the provided guide is for implementation on Linux. (Windows implementation might face problems in multi-process version)

### Preparation

1. Open a commond prompet (preferly Anaconda prompt)
2. Direct to your prefered direction:
```
cd path
```
3. Clone the code on the direction:
```
git clone https://github.com/rafiei91/Assignment---Scientific-Computing-using-Python-2.git
```
4. Go to the cloned repository
```
cd Assignment---Scientific-Computing-using-Python-2
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
python Main.py --version_select naive(or parallel or vectorized or multiprocessing) --core_number 1(up to 32 - if the multiciore is going to be executed)
```
