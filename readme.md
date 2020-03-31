# Astra non-stop Run

## Description
This file can be used for 1) mimicking the solenoid scan, and 2) looping all of the particle distribution `.ini` files under 
the same directory. 

This file is only functional on macOS. For Windows or LINUX, you need to download other astra programs from [Astra (Desy)](http://www.desy.de/~mpyflo/).


## Usage
The `astra_in.in` is the parent astra input file for further modifications.

**Arguments**

| Description                | Flag          | 
| ---------------------------|:-------------:| 
| Input file name            | -f --filename |
| Initial solenoid scan field| -s --start    |
| Final solenoid scan field  | -e --end      |
| Solenoid scan step size    | -st --step    |

 - To simulate all `.ini` files, use argument `-s` following with the fixed solenoid field [T], for example, 
    ```python
    $ python3 rec_run.py -s -0.025
    ```
 - To mimic the solenoid scan process, use argument `-f` following with the desired input file, `-s` following with the 
initial solenoid scan field [Gauss], `-e` with the final solenoid scan field [Gauss], and `-st` with the scan step size 
[Gauss].
    ```python
    $ python3 rec_run.py -f test.ini -s -250 -e -280 -st -20
    ```
   
