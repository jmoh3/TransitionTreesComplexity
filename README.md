# TransitionTreesComplexity

To set up, run:

```
pip install requirements.txt
```

Then, run the command:

```
make draw w='PERMUTATION'
```

To generate a pdf containing the rothe diagram for your permutation. The permutation should be a list of n numbers separated by whitespace, where the minimum element is 1 and the maximum is n. For example,

```
make draw w='5 4 2 7 8 3 1 6'
```

## Old Stuff

* original_tree_builder.py contains original one line notation approach as described by Brendan's email and Alex's amendments

* rothe_tree_builder.py contains approach based off of rothe diagrams

* tree_builder.py contains start to approach based off of one line notation, but it already has issues