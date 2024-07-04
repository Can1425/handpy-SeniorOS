#!/bin/bash

echo "Senior OS Build Runtime Quick Initialization Tool"
echo "    - By @Mask:"
echo "    - Released Under MIT license."

while true; do
  read -p "Do you want to create Python Python Virtual Environments? (Y/n): " choice
  case "$choice" in
    y|Y ) 
      echo "OK"
      while true; do
	  read -p "Are you using Python 2 or Python 3? (2/3): " choice
	  case "$choice" in
	    "2" ) 
	      python -m venv .venv
	      break
	      ;;
	    "3" ) 
	      python3 -m venv .venv
	      break
	      ;;
	    * ) 
	      echo "Invalid Input, please enter 2 or 3."
	      ;;
	  esac
	done
      . .venv/Scripts/activate
      break
      ;;
    n|N ) 
      echo "OK"
      break
      ;;
    * ) 
      echo "Invalid Input, please enter Y or N."
      ;;
  esac
done

echo "Python Virtual Environments create finished or canceled, start install Python library..."

while true; do
  read -p "Are you using Pip 2 or Pip 3? (2/3): " choice
  case "$choice" in
    "2" ) 
      pip install mpy-cross-v5
      pip install GitPython
      break
      ;;
    "3" ) 
      pip3 install mpy-cross-v5
      pip3 install GitPython
      break
      ;;
    * ) 
      echo "Invalid Input, please enter 2 or 3."
      ;;
  esac
done

echo "[INFO] Successful initialization SeniorOS Build Environment."
echo "
Now can execute the following commands:
 - Build SeniorOS for Python 2: python ./tools/Build.py
 - Build SeniorOS for Python 3: python3 ./tools/Build.py"
