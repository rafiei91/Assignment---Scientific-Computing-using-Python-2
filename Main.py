import argparse
import sys
import os
import pickle

parser = argparse.ArgumentParser()
# Execution selection
parser.add_argument('--version_select', default='', type=str)
parser.add_argument('--core_number', default='1', type=str)

args = parser.parse_args()
ver = args.version_select
core = args.core_number
c = int(core)

if (ver == "naive" or "parallel" or "vectorized"):
  cwd = os.getcwd()
  cwd = cwd + "/" + "Implementations"
  os.chdir(cwd)
  file_to_open = ver + ".py"
  exec(open(file_to_open).read())
elif ver == "multiprocessing" and core <= 32:
  cwd = os.getcwd()
  cwd = cwd + "/" + "Implementations"
  os.chdir(cwd)
  pickle.dump(core, open("core", "wb"))
  file_to_open = ver + ".py"
  exec(open(file_to_open).read())
elif ver == "test":
  cwd = os.getcwd()
  cwd = cwd + "/" + ver
  os.chdir(cwd)
  os.system("python -m unittest -v")
else:
  print("Wrong input. \n ver_select (naive or parallel or vectorized or multiprocessing or test) \n core_number: 1 to 32")
