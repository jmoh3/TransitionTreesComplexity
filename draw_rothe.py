import os
import sys

BOX = 0
DOT = 1
HLINE = 2
VLINE = 3

def build_rothe_diagram(w):
  diagram = np.zeros((len(w), len(w)))

  for i in range(0, len(w)):
    diagram[i][w[i] - 1] = DOT
    # horizontal line next to dot
    for j in range(w[i], len(w)):
      diagram[i][j] = HLINE
    # vertical line next to dot
    for k in range(i + 1, len(w)):
      diagram[k][w[i] - 1] = VLINE
  return diagram

def draw_diagram(w):
  diagram = build_rothe_diagram(w)
  latex_str = '\\begin{tikzpicture}[scale=.4]\n\\draw (0,0) rectangle ('+str(len(w))+','+str(len(w))+');\n'

  for i in range(0, len(w)):
    x_loc = w[i] - 0.5
    y_loc = len(w) - i - 0.5

    dot_str = f'\\filldraw ({x_loc},{y_loc}) circle (.5ex);\n'
    latex_str += dot_str

    line_str = f'\\draw[line width = .2ex] ({x_loc},0) -- ({x_loc},{y_loc}) -- ({len(w)},{y_loc});\n'
    latex_str += line_str

    for j in range(0, len(w)):
      if diagram[i][j] == BOX:
        latex_str += f'\\draw ({j}, {len(w)-i-1}) rectangle ({j+1},{len(w)-i});\n'
    
  latex_str += '\\end{tikzpicture}'
  return latex_str

def compile_latex(rothe_string):
  doc_beginning = '\\documentclass[12pt]{amsart}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amsfonts, amssymb, latexsym, graphicx, hyperref, amsmath}\n%\\usepackage[linesnumbered,ruled]{algorithm2e}\n\\usepackage{tikz}\n\\title{rothe-diagram-template}\n\\date{October 2019}\n\\begin{document}\n'
  doc_end = '\\end{document}'

  with open('main.tex', 'w') as file:
    file.write(doc_beginning + rothe_string + doc_end)
  
  os.system('pdflatex main.tex')
  os.system('open main.pdf')
    
if __name__ == '__main__':
  print(sys.argv)
  w = [int(char) for char in sys.argv[1:]]
  print(w)
  latex = draw_diagram(w)
  print(latex)
  compile_latex(latex)