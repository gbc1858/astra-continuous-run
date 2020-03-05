# Astra non-stop Run

## Description
This file can be used for 1) mimicking the solenoid scan, and 2) looping all of the particle distribution `.ini` files under 
the same directory. 

This file is only functional on macOS. For Windows or LINUX, you need to download other astra programs from [Astra (Desy)](http://www.desy.de/~mpyflo/).



## Usage
The `astra_in.in` is the parent astra input file for further modifications.
 - To simulate all `.ini` files, use argument `-s` following with the fixed solenoid field [T], for example, 
    ```python
    python3 rec_run.py -s -0.025
    ```
 - To mimic the solenoid scan, use argument `-f` following with the desired input file, `-s` following with the 
start of the solenoid scan field [Gauss], `-e` with the end of the scan field [Gauss], and `-st` with the scan step size 
[Gauss].
    ```python
    python3 rec_run.py -s -250 -e -280 -st -20
    ```
   
