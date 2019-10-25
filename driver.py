import numpy as np
import os
import sys
from draw_rothe import draw_diagram, compile_latex
from reconstruct_permutation import reconstruct_permutation, reconstruct_permutation_complete
from make_transition import get_new_lehmer_code


def draw(lehmer, latex):
    w = reconstruct_permutation_complete(lehmer)
    latex = latex + draw_diagram(w) + '\n'
    compile_latex(latex)
    return latex

if __name__ == '__main__':
    latex = ''
    lehmer_code = [int(char) for char in sys.argv[1:]]
    latex = draw(lehmer_code, latex)

    while True:
        print('Please choose a pivot')
        pivot = int(input())
        lehmer_code = get_new_lehmer_code(lehmer_code, pivot)
        print(lehmer_code)
        latex = draw(lehmer_code, latex)

    print('Permutation is vexilliary')
