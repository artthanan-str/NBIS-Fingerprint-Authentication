# NBIS Fingerprint Authentication Demo
This program demonstrates fingerprint authentication using NBIS library as a part of Computer and Communication Security Project, Faculty of Information and Communication Technology, Mahidol University.

## Project Directory Structure
`./database` stores 10 example minutiae of fingerprints in the database for testing.
`./input/demo` store 5 examples input minutiae of fingerprints for different test cases.
`./input/eft` stores all input minutiae of fingerprints that can be used in this program.


## Prerequisites
Linux Operating System (Ubuntu is recommended)
If you don't have the OS, you can download `.vdi` file from [osboxes.org](https://drive.google.com/file/d/14ZZhRCvC2kaMEY1TI0hJUl6jygnLg4oJ/view) to use it on VirtualBox (the password is **`osboxes.org`**)

## Installation
Clone this repository to your local machine, or download this repository as a ZIP file and then extract anywhere on your local machine.

## Running the program
 1. Locate the file `demo.py` inside the folder
 3. Run `demo.py`
 2. An easy way to run is to right-click the root folder `NBIS-Fingerprint-Authentication-Demo` and click **Open in Terminal.** The terminal should open at the root directory.
 3. Type `python3 demo.py` or `python demo.py` to run the command. The interface will be shown.

> **Note:** If the error shows that 
> ``` ./library/bozorth3: Permission denied.```
> Please follow the direction below.

### Handling `Permission Denied` Error
1. If the program is still running, press `Ctrl+C` to exit the program. The terminal should be at the root directory.
2. Type `cd library` to go into **Library** folder.
3. Type `chmod 777 bozorth3` and `chmod 777 mindtct` to allow all permission to the file.
(**Note:** that this is not a good practice of allowing permissions; however, it works for demonstration purpose)
5. Type `cd ..` to go back to the root directory.
6. Run the file again using `python3 demo.py` or `python demo.py` command.

## Instructions
The program consists of two modes: **Identification** and **Verification**.
In the welcoming screen, you will have the option to choose between the modes. Follow the on-screen instructions to use the program, or read below for more detailed information.

### Identification
This mode tries to identify the input fingerprint with one of the fingerprints in the database.
The program will ask for the input file, which the default directory is in `./input/demo`.

#### Examples of fingerprints to try:
- `inDB_1` and `inDB_2` is a fingerprint that exists in the database.
- `noone` is a fingerprint that does not exist in the database

### Verification
This mode tries to verify if the input fingerprint is matched with the information given. For example, it could answer the question like "Does this fingerprint belong to this citizen ID?". In this demo program, file name is used as the information given.

#### Examples of fingerprints to try:
- `inDB_1` and `inDB_2` is a fingerprint that exists in the database, but the file names are not matched with its respective fingerprint.
- `2` is a fingerprint that exists in the database, and its name matches with its respective fingerprint.

## References
[NBIS documentation](https://www.nist.gov/publications/users-guide-nist-biometric-image-software-nbis)

[NBIS download](https://www.nist.gov/itl/iad/image-group/products-and-services/image-group-open-source-server-nigos#Releases)
