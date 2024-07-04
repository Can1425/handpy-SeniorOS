@echo off
echo Senior OS Build Runtime Quick Initialization Tool
echo    - By @CycleBai
echo    - Released Under MIT license.

:CREATE_VENV
set /p choice="Do you want to create a Python Virtual Environment? (Y/n): "
if /i "%choice%"=="y" (
    echo OK
    :PYTHON_VERSION
    set /p py_version="Are you using Python 2 or Python 3? (2/3): "
    if "%py_version%"=="2" (
        python -m venv .venv
    ) else if "%py_version%"=="3" (
        python3 -m venv .venv
    ) else (
        echo Invalid Input, please enter 2 or 3.
        goto PYTHON_VERSION
    )
    call .\.venv\Scripts\activate.bat
) else if /i "%choice%"=="n" (
    echo OK
) else (
    echo Invalid Input, please enter Y or N.
    goto CREATE_VENV
)

echo Python Virtual Environment creation finished or canceled, start installing Python libraries...

:INSTALL_LIB
set /p pip_version="Are you using Pip 2 or Pip 3? (2/3): "
if "%pip_version%"=="2" (
    pip install mpy-cross-v5
    pip install GitPython
) else if "%pip_version%"=="3" (
    pip3 install mpy-cross-v5
    pip3 install GitPython
) else (
    echo Invalid Input, please enter 2 or 3.
    goto INSTALL_LIB
)

echo [INFO] Successfully initialized SeniorOS Build Environment.
echo.
echo Now you can execute the following commands:
echo  - Build SeniorOS for Python 2: python ./tools/Build.py
echo  - Build SeniorOS for Python 3: python3 ./tools/Build.py

