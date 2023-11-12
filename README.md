# ccwc tool

## Table of contents
- [System Requirements](#system-requirements)
- [Project Structure](#project-structure)
- [Use of the Tool](#use-of-the-tool)
- [Tool Testing](#tool-testing)


### System Requirements

The ccwc tool has been build in Python, version 3.10.12.

There are three external libraries used, re (regular expressions), os (operating system) and unittest.

### Project Structure

```
.
├── ccwc_methods.py                  - the file contains static methods used in input file assessemnt.
├── main.py                          - the tool main entry.
├── test.py                          - tests applied in static methods assessment.
└── test.txt                         - the file used in ccwc tool assessment.

```

### Use of the Tool

The tools takes a file as input and outputs to the cli file measurements according the the chosen option. The filename input accepts a word.word form.

The tool tries to follow wc syntax, thus its application is as follows:

```
ccwc [option] filename
```

There are five options supported:

- generic: without an option, outputs the number of lines, words and bytes in a file.
- ```-c```: outputs the number of bytes in a file.
- ```-l```: outputs the number of lines in a file.
- ```-w```: outputs the number of words in a file.
- ```-m```: outputs the number of chars in a file.

The tool also supports a combination of std_out input, where the ccwc options are as given above, in the form:

```
cat filename | ccwc [option]
```

### Tool Testing

The test file can be run from the command line:

```
python3 -m unittest test.py
```