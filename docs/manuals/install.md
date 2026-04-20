# How to Install the program

## 1. Clone the repo

First you need to clone the repo in your local machine. Open a Terminal, change directory to the desire destination of the program and run 

`git clone https://github.com/mnarizzano/se-25-textquality.git`

then checkout to 'dev' branch (there there is the most updated code) with command

`git checkout dev`

Alternatively, you can download the .zip from github and extract it in the desire destination

## 2. Setup the environment

### 2.1 Install Python 3.12.x

Windows: Download the .[msi](https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe) and run it 

Linux: 
`sudo apt install python3.12`

`sudo apt install python3.12-venv`

### 2.2 Create the virtual environment

Open a terminal and change directory to the installation path. Then run:

`cd src/main`

`python3 -m venv venv`

and finally

`pip install -r requirements.txt`
