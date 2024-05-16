import os
from pylatex import Document, Section, NoEscape, Command

def write_problems_to_latex(problems, filename, font_size='normalsize', num_columns=4, array_stretch=1.5, title='Math Problems'):
    doc = Document()
    doc.preamble.append(Command('usepackage', 'geometry'))
    doc.preamble.append(Command('geometry', 'margin=1in'))
    doc.preamble.append(Command('usepackage', 'array'))
    doc.preamble.append(Command('usepackage', 'tabularx'))

    # Increase vertical spacing in array environment
    doc.preamble.append(NoEscape(f'\\renewcommand{{\\arraystretch}}{{{array_stretch}}}'))

    with doc.create(Section(f'{title}')):
        doc.append(NoEscape(f'\\{font_size}'))

        num_problems = len(problems)
        num_rows = (num_problems + num_columns - 1) // num_columns  # ceiling division
        print(f'num_problems: {num_problems}, num_rows: {num_rows}, num_columns: {num_columns}')

        # Create the table manually as a LaTeX string
        table_content = []
        for i in range(num_rows):
            row = []
            for j in range(num_columns):
                index = i + j * num_rows
                if index < num_problems:
                    [operand1, operand2], _, operator = problems[index]
                    operator_latex = '\\times' if operator == '*' else operator
                    problem_str = f"\\begin{{array}}{{c}} {operand1} \\\\ {operator_latex} {operand2} \\\\ \\hline \\\\ \\\\ \\end{{array}}"
                    row.append(problem_str)
                else:
                    row.append('')
            table_content.append(" & ".join(row) + " \\\\")
        
        table_latex = (
            "\\begin{tabularx}{\\textwidth}{"
            ">{\\centering\\arraybackslash}X"
            ">{\\centering\\arraybackslash}X"
            ">{\\centering\\arraybackslash}X"
            ">{\\centering\\arraybackslash}X}\n"
            + "\n".join(table_content) +
            "\n\\end{tabularx}"
        )

        doc.append(NoEscape(table_latex))
    
    # Create output directory if it does not exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    doc.generate_pdf(filename, clean_tex=False)
