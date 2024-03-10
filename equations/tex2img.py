from sympy import preview

#preamble = "\\documentclass[1pt]{article}\n" \
#           "\\usepackage{amsmath,amsfonts}\\begin{document}"
basic_unit = r"$$o_i = w \cdot x$$"
preview(basic_unit, output='png', viewer='file', filename='basic_unit.png', dvioptions=['-D','150'])

#preview(basic_unit, viewer='file', filename='basic_unit.pdf', euler=False, fontsize=24)
