import numpy as np
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
    latex_str += '\\end{tikzpicture}};'
    return latex_str

if __name__ == '__main__':
  w = [int(char) for char in sys.argv[1:]]
  print(draw_diagram(w))