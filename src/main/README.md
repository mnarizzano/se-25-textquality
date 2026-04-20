Code is organized as follow:

- Root path contains main classes:
    - main.py - entry point of the program
    - word_file.py - class that models a .docx file and defines methods to read and load it
    - base_vocabulary.py - class that loads the bases vocabulary and stores it in different strructures

- VdB contains 3 text files that contain the words that belong to the base vocabulary divided in High disponibility words, High usage and Fundamental vocabulary.

- indexes contains classes that calculates the indexes. They take in input data from the file and returns the calculated index

- icons contains image resources for the program

- controls contains graphic controls that exploit the previous classes to represent data
