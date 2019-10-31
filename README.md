# Rothe Diagram Tree Builder

A tool that allows you to generate Rothe Diagrams for a given permutation and visualize the outcomes of Lascoux-Schützenburger transition moves. This is part of a research project with Anna Chlopecki and Alexander Yong through ICLUE, the Illinois Combinatorics Lab for Undergraduate Experience.

To set up, run:

```
pip install requirements.txt
```

## Lascoux-Schützenburger Trees

To see the result of transition moves for a permutation, run the command:

```
make tree code='CODE'
```

Where CODE is a Lehmer code in which the numbers are separated by whitespace. Once you get the initial drawing, you will be prompted to enter in the row of a pivot for the diagram. Type in the pivot you wish to see (1 indexed) and hit enter to see the next node of the tree. For example, running:

```
make tree code='4 2 0 3'
```
Then selecting 1 for the pivot will give you a diagram that looks like this:

![alt text](https://github.com/jmoh3/TransitionTreesComplexity/blob/master/images/tree_example.png)

In which the diagram on the left is the parent, and the diagram on the right is the child resulting from transitioning over the pivot in the first row. 

Still working on having this tool tell you what the pivots are and check when the permutation is vexilliary.

## Rothe Diagram

Run the command:

```
make draw w='PERMUTATION'
```

To generate a pdf containing the rothe diagram for your permutation. The permutation should be a list of n numbers separated by whitespace, where the minimum element is 1 and the maximum is n. For example,

```
make draw w='5 4 2 7 8 3 1 6'
```

Will generate a picture that looks like this:

![alt text](https://github.com/jmoh3/TransitionTreesComplexity/blob/master/images/rothe_example.png)

## Old Stuff

* original_tree_builder.py contains original one line notation approach

* rothe_tree_builder.py contains approach based off of rothe diagrams

* tree_builder.py contains start to approach based off of one line notation, but it already has issues