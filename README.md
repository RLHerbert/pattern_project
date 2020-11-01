# pattern_project

## CECS 550-01 | Project 1 - DTrees Ensemble

**Team Name**: Classy Fires

**Team Members** Members: Sophanna Ek, Melissa Hazlewood Rowan Herbert, Dennis La

Introduction: 
    The automated Ensemble Decision Tree (DTree) Builder was built by using a weighted vote of the two DTrees based on their accuracy. 
    The first DTree was built with an initial selection of the vectors. The second DTree was built with boosted feature vectors. The same data was used in both DTrees for training, testing and validating. The DTree builder used the standard Shannon-based Entropy and Information Gain mechanisms with a Training Set. This project implemented in Python. 

File Contents:
- Dtree.py: Decision tree class includes all neccessary functions to construct the decision tree. 
- DtreeNodes: Decision tree data structure includes question and leaf nodes. 
- Ensemble.py: Decision tree Ensemble class include all neccessary function to construct the decision tree.
- parse.py: Data input processing file.
- second_tree.py: Decision tree #2 construction.
- main.py: The entry of the application. It prints out all the output for this project. 
- TestDriver.py


External Requirements: 
- None

Setup and Installation:
- Download and install Python intepreter 
-- `pip install python`
- Unzip the project folder


Sample Invocation: 
- `Python3 main.py`

Features:
- Boosted Feacture Vectors
- Weight Voting Using accuracy rate

Issues:
- None so far